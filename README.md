# AdvertiseX Data Engineering Solution

## Overview

This project provides a complete data engineering solution for AdvertiseX, a digital advertising technology company. It includes data ingestion, preprocessing, monitoring, anomaly detection, and data storage in HDFS and Hive. The solution handles various data formats: JSON, CSV, and Avro.

Solution Design.png displays the workflow of the solution/Architecture used


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
- Apache Kafka
- Apache Spark
- HDFS
- Hive
- Confluent Kafka 
- Necessary Python packages (see `requirements.txt`)

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/LavDeshpande/Advertisex_solution.git
    cd advertisex-data-engineering
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

4. **Configure Kafka and HDFS:**
    Ensure Kafka and HDFS are properly set up and running. Update the `config/config.env` file with the correct settings.

## Data Ingestion

### CSV Ingestion (`data_ingestion/ad_impression_realtime_ingestion.py`)

Ingests CSV data (Ad impressions) into Kafka.

```python
python data_ingestion/ad_impression_realtime_ingestion.py

### Json Ingestion (`data_ingestion/clicks_and_conversions_batch_ingestion.py`)

Ingests json data (clicks and conversions) into Kafka.

```python
python data_ingestion/clicks_and_conversions_batch_ingestion.py

### Avro Ingestion (`data_ingestion/bid_request.py`)

Ingests Avro data (Bid Requests) into Kafka.

```python
python data_ingestion/bid_request.py

### Kafka Onsumer with monitoring and anomaly detection (`data_preprocessing/kafka_consumer_with_lag_monitoring.py`)

Run Kafka Consumer.

```python
python data_preprocessing/kafka_consumer_with_lag_monitoring.py


### Data Preprocessing using Pyspark (`data_preprocessing/pyspark_data_preprocessing.py`)

Data Preprcessing and Insight derivative Consumer along with data dump into hdfs and hive.

```python
python data_preprocessing/pyspark_data_preprocessing.py

### Sample query  (`data_preprocessing/pyspark_data_preprocessing.py`)

Sample query to pull out insights between ad impressions and clicks and conversion from hive

```python
python data_preprocessing/pyspark_data_preprocessing.py



