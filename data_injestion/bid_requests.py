# Real Time Ingesion Avro

import os
import time
import avro.schema
import avro.io
import io
import logging
from kafka import KafkaProducer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka producer configuration
bootstrap_servers = 'localhost:9092'
avro_topic = 'bid_requests_topic'
avro_producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Load Avro schema
schema_path = 'path/to/bid_request_schema.avsc'
schema = avro.schema.parse(open(schema_path, "r").read())

# Function to send Avro data to Kafka
def send_avro_to_kafka(file_path):
    try:
        with open(file_path, 'rb') as file:
            for line in file:
                bytes_reader = io.BytesIO(line)
                decoder = avro.io.BinaryDecoder(bytes_reader)
                reader = avro.io.DatumReader(schema)
                message = reader.read(decoder)
                avro_producer.send(avro_topic, value=message)
                logger.info(f'Sent message: {message}')
                time.sleep(1)  # Simulate real-time ingestion
    except Exception as e:
        logger.error(f'Error in sending Avro data to Kafka: {e}')

# Real-time process Avro file
avro_file_path = 'path/to/bid_requests.avro'
send_avro_to_kafka(avro_file_path)
avro_producer.flush()
avro_producer.close()
