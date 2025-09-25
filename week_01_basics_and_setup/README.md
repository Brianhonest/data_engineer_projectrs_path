# Week 1: Basics and Setup

## Overview
This week covers the fundamental setup and basic tools for the data engineering course.

## Activities

### Terraform (Infrastructure as Code)
- **Location**: `./terraform/`
- **Description**: Terraform configuration for setting up cloud infrastructure
- **Files**:
  - `main.tf` - Main Terraform configuration
  - `.terraform.lock.hcl` - Terraform lock file

### Docker + PostgreSQL Pipeline (Integrated System)
- **Locations**: `./docker/` and `./postgres/`
- **Description**: Complete containerized data processing pipeline with PostgreSQL database
- **Docker Components** (`./docker/`):
  - `docker-compose.yaml` - Multi-container setup (PostgreSQL + pgAdmin)
  - `Dockerfile` - Python ETL container definition
- **PostgreSQL & ETL Components** (`./postgres/`):
  - `ingest_data.py` - Python script for ingesting NY taxi data into PostgreSQL
  - `pipeline.py` - Data pipeline utilities
  - `upload_data.ipynb` - Jupyter notebook for data analysis
- **How they work together**: 
  - Docker Compose spins up PostgreSQL database and pgAdmin interface
  - Python ETL scripts connect to the containerized database to process NYC taxi data
  - Complete end-to-end data pipeline from raw data to queryable database

### Homework
- **Location**: `./homework/`
- **Description**: Week 1 homework assignments and solutions

## Learning Objectives
- [ ] Set up development environment
- [ ] Learn Terraform basics
- [ ] Understand Docker fundamentals
- [ ] Set up PostgreSQL database
- [ ] Complete homework assignments

## Notes
Add your notes and learnings from this week here.