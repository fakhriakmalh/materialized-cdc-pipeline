from confluent_kafka import Consumer, KafkaException

# Kafka configuration
kafka_config = {
    "bootstrap.servers": "localhost:9092",  # Change if using a remote broker
    "group.id": "dummy_table_mv_consumer",  # Consumer group
    "auto.offset.reset": "earliest",  # Start from the beginning if no offset is stored
}

# Create Kafka Consumer
consumer = Consumer(kafka_config)

# Subscribe to the topic
topic = "dummy_table_mv_dt"
consumer.subscribe([topic])

print(f"Listening to topic: {topic}...")

try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Wait for a message
        if msg is None:
            continue  # No message, continue polling
        if msg.error():
            print(f"Kafka error: {msg.error()}")
            continue

        # Decode and print message (assumes JSON format)
        print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("\nStopping consumer...")
finally:
    consumer.close()
