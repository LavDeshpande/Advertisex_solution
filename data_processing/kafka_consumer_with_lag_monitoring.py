from confluent_kafka import Consumer, Producer, KafkaError
import logging
import time
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka consumer configuration
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'group1',
    'auto.offset.reset': 'earliest'
}

# Kafka producer configuration for feedback
producer_conf = {
    'bootstrap.servers': 'localhost:9092'
}

# Create Kafka consumer
consumer = Consumer(**consumer_conf)
consumer.subscribe(['ad_impressions_topic', 'clicks_conversions_topic', 'bid_requests_topic'])

# Create Kafka producer
producer = Producer(**producer_conf)

# Function to send feedback
def send_feedback(feedback_data):
    feedback_topic = 'feedback_topic'
    feedback_message = json.dumps(feedback_data).encode('utf-8')
    producer.produce(feedback_topic, feedback_message)
    producer.flush()

# Function to monitor Kafka consumer lag
def monitor_consumer_lag(consumer):
    while True:
        current_offsets = consumer.committed(consumer.assignment())
        end_offsets = consumer.end_offsets(consumer.assignment())
        lag_per_partition = {partition: end_offsets[partition] - (current_offsets[partition].offset if current_offsets[partition] else 0)
                              for partition in consumer.assignment()}
        total_lag = sum(lag_per_partition.values())
        logger.info(f"Total Lag: {total_lag}, Lag per Partition: {lag_per_partition}")

        if total_lag > 100:  # Example threshold
            logger.warning("Total lag exceeds threshold. Taking action...")
            send_feedback({'type': 'lag_anomaly', 'description': 'Total lag exceeds threshold.'})

        time.sleep(5)  # Check lag every 5 seconds

# Function to consume messages and handle errors
def consume_messages():
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                logger.error(msg.error())
                continue
        try:
            logger.info(f"Consumed message: {msg.value().decode('utf-8')}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")

# Start consuming and monitoring
try:
    # Run the consume_messages and monitor_consumer_lag functions concurrently
    import threading
    consumer_thread = threading.Thread(target=consume_messages)
    lag_monitor_thread = threading.Thread(target=monitor_consumer_lag, args=(consumer,))
    
    consumer_thread.start()
    lag_monitor_thread.start()

    consumer_thread.join()
    lag_monitor_thread.join()
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    producer.close()
