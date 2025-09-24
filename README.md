# NY Taxi Data Pipeline

A containerized data engineering pipeline for processing NYC Taxi trip data using Docker, PostgreSQL, and Python. This project demonstrates ETL processes, database management, and data analysis workflows.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Source   │───▶│  Docker Stack   │───▶│   PostgreSQL    │
│  (NYC Taxi)     │    │  (Python ETL)   │    │   Database      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │    pgAdmin      │
                       │ (Web Interface) │
                       └─────────────────┘
```

## 🚀 Features

- **Dockerized Environment**: Complete containerized setup with PostgreSQL and pgAdmin
- **Flexible Data Ingestion**: Supports both CSV and Parquet file formats
- **Chunked Processing**: Efficiently handles large datasets through chunked reading
- **Database Management**: PostgreSQL with pgAdmin web interface for easy management
- **Automated ETL**: Command-line interface for data extraction, transformation, and loading

## 📋 Prerequisites

- Docker and Docker Compose installed
- Python 3.9+ (if running locally)
- At least 2GB of available disk space for data processing

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Brianhonest/ny_taxi_pipeline.git
   cd ny_taxi_pipeline
   ```

2. **Start the Docker services:**
   ```bash
   docker-compose up -d
   ```

   This will start:
   - PostgreSQL database on port `5433`
   - pgAdmin web interface on port `8080`

3. **Verify services are running:**
   ```bash
   docker-compose ps
   ```

## 🎯 Usage

### Access pgAdmin
- Open your browser and go to: http://localhost:8080
- Login credentials:
  - Email: `admin@admin.com`
  - Password: `root`

### Connect to PostgreSQL in pgAdmin
- Host: `pgdatabase` (service name)
- Port: `5432`
- Username: `root`
- Password: `root`
- Database: `ny_taxi`

### Run Data Ingestion

#### Using Docker (Recommended)
Build the ingestion container:
```bash
docker build -t taxi_ingest .
```

Run the ingestion process:
```bash
docker run -it \
  --network=2_docker_sql_default \
  taxi_ingest \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
```

#### Using Local Python
```bash
python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5433 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
```

## 📊 Data Sources

This pipeline is designed to work with NYC Taxi & Limousine Commission (TLC) Trip Record Data:
- **Yellow Taxi Trip Records**: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Supports both CSV and Parquet formats
- Automatically handles datetime conversion for pickup and dropoff times

### Sample Data URLs
- Parquet: `https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet`
- CSV: `https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz`

## 🗃️ Database Schema

The pipeline creates a table with the following structure:
- `tpep_pickup_datetime`: Pickup timestamp
- `tpep_dropoff_datetime`: Dropoff timestamp
- `passenger_count`: Number of passengers
- `trip_distance`: Distance traveled
- `fare_amount`: Base fare
- `tip_amount`: Tip amount
- And other NYC taxi trip attributes...

## 🔧 Configuration

### Docker Compose Services

#### PostgreSQL Database
- **Image**: `postgres:17`
- **Port**: `5433:5432`
- **Database**: `ny_taxi`
- **Credentials**: root/root

#### pgAdmin
- **Image**: `dpage/pgadmin4`
- **Port**: `8080:80`
- **Credentials**: admin@admin.com/root

### Python Dependencies
- `pandas`: Data manipulation and analysis
- `sqlalchemy`: Database toolkit
- `psycopg2-binary`: PostgreSQL adapter
- `pyarrow`: Parquet file support

## 📁 Project Structure

```
├── docker-compose.yaml      # Docker services configuration
├── Dockerfile              # Python ingestion container
├── ingest_data.py          # Main ETL script
├── pipeline.py             # Pipeline utilities
├── upload_data.ipynb       # Jupyter notebook for analysis
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🐛 Troubleshooting

### Common Issues

1. **Port conflicts**: If port 5433 or 8080 are in use, modify the ports in `docker-compose.yaml`

2. **Memory issues**: For large datasets, the chunked processing should handle memory efficiently

3. **Network issues**: Ensure Docker containers can communicate by using the correct network name

4. **Database connection**: When using Docker ingestion, use `pgdatabase` as host; when running locally, use `localhost`

### Useful Commands

```bash
# View container logs
docker-compose logs pgdatabase
docker-compose logs pgadmin

# Stop all services
docker-compose down

# Remove volumes (CAUTION: This deletes all data)
docker-compose down -v

# Rebuild containers
docker-compose build --no-cache
```

## 🚧 Future Enhancements

- [ ] Add data validation and quality checks
- [ ] Implement incremental data loading
- [ ] Add monitoring and logging
- [ ] Create automated testing suite
- [ ] Add support for multiple taxi types (green, uber, etc.)
- [ ] Implement data transformation pipelines

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- NYC Taxi & Limousine Commission for providing the dataset
- DataTalksClub for data engineering resources and tutorials