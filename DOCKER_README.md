# AdvertiseX Data Engineering Solution

## Overview

This project provides a complete data engineering solution for AdvertiseX, a digital advertising technology company. It includes data ingestion, preprocessing, monitoring, anomaly detection, and data storage in HDFS and Hive. The solution handles various data formats: JSON, CSV, and Avro.

## Project Structure

- `data_ingestion/`
  - `csv_ingestion.py`
  - `json_ingestion.py`
  - `avro_ingestion.py`
- `data_processing/`
  - `kafka_consumer.py`
  - `preprocessing.py`
  - `sample_query_hive.py`
- `config/`
  - `config.env`
  - `config.yaml`
- `README.md`
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`

## Prerequisites

- Python 3.8+
- Docker
- Docker Compose

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/LavDeshpande/Advertisex_solution.git
    cd Advertisex_solution
    ```

2. **Set up the environment:**
    ```sh
    cp config/config.env.example config/config.env
    cp config/config.yaml.example config/config.yaml
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Start Docker Compose:**
    ```sh
    docker-compose up -d
    ```

5. **Run Data Ingestion:**
    ```sh
    docker-compose up -d ingestion-csv
    docker-compose up -d ingestion-json
    docker-compose up -d ingestion-avro
    ```

6. **Run Data Processing:**
    ```sh
    docker-compose up -d consumer
    docker-compose up -d preprocessing
    docker-compose up -d feedback
    ```
