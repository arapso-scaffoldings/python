from kafka import KafkaConsumer

consumer = KafkaConsumer('events')
for msg in consumer:
    print msg