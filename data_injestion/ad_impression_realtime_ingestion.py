# Json Data Handling

import os
import time
import json
import logging
from kafka import KafkaProducer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka producer configuration
bootstrap_servers = 'localhost:9092'
json_topic = 'ad_impressions_topic'
json_producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Function to send JSON data to Kafka
def send_json_to_kafka(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                message = json.loads(line.strip())
                json_producer.send(json_topic, message)
                logger.info(f'Sent message: {message}')
                time.sleep(1)  # Simulate real-time ingestion
    except Exception as e:
        logger.error(f'Error in sending JSON data to Kafka: {e}')

# Real-time process JSON file
json_file_path = 'path/to/ad_impressions.json'
send_json_to_kafka(json_file_path)
json_producer.flush()
json_producer.close()
