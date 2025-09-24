#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
from time import time
import pandas as pd
from sqlalchemy import create_engine
import argparse
import pyarrow.parquet as pq




def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    # Determine file type from URL
    if url.endswith('.parquet'):
        file_name = "output.parquet"
        is_parquet = True
    else:
        file_name = "output.csv"
        is_parquet = False
    
    # Download the file
    download_command = f"wget {url} -O {file_name}"
    result = subprocess.run(download_command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error downloading file from {url}:\n{result.stderr}")
        exit(1)
    
    print(f"Successfully downloaded {file_name}")
    
    # Create database engine
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # Read file in chunks
    if is_parquet:
        # For parquet files, read the entire file first (parquet is already compressed)
        df = pd.read_parquet(file_name)
        # Create iterator-like chunks manually
        chunk_size = 100000
        total_rows = len(df)
        chunks = [df[i:i+chunk_size] for i in range(0, total_rows, chunk_size)]
        df_iter = iter(chunks)
    else:
        df_iter = pd.read_csv(file_name, iterator=True, chunksize=100000)

    df = next(df_iter)



    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


    df.head(n=0).to_sql(name=table_name,con=engine,if_exists='replace')
    df.to_sql(name=table_name,con=engine,if_exists='append')
    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=table_name,con=engine,if_exists='append')
            t_end = time()
            # do your inserts here
        except StopIteration:
            print("Finished reading all chunks.")
            break




if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    #user,password,host,pot,db,table_name,csv_file
    parser.add_argument('--user',help='username for postgres')
    parser.add_argument('--password',help='password for postgres')
    parser.add_argument('--host',help='host for postgres')
    parser.add_argument('--port',help='port for postgres')              
    parser.add_argument('--db',help='database name for postgres')
    parser.add_argument('--table_name',help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    main(args)
