# Batch Processing handling csv data

import os
import time
import logging
import pandas as pd
from kafka import KafkaProducer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka producer configuration
bootstrap_servers = 'localhost:9092'
csv_topic = 'clicks_conversions_topic'
csv_producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Function to send CSV data to Kafka
def send_csv_to_kafka(file_path):
    try:
        data = pd.read_csv(file_path)
        for index, row in data.iterrows():
            message = row.to_json().encode('utf-8')
            csv_producer.send(csv_topic, message)
            logger.info(f'Sent message: {message}')
            time.sleep(1)  # Simulate real-time ingestion
    except Exception as e:
        logger.error(f'Error in sending CSV data to Kafka: {e}')

# Batch process CSV file
csv_file_path = 'path/to/clicks_conversions.csv'
send_csv_to_kafka(csv_file_path)
csv_producer.flush()
csv_producer.close()
