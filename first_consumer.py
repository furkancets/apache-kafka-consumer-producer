from kafka import KafkaConsumer

consumer = KafkaConsumer(
    topic="topic1",
    group_id="group1",
    bootstrap_servers=["localhost:9092"]
)

for message in consumer:
    print("{} - {}".format(message.key.decode('utf-8'),
                           message.value.decode('utf-8')))