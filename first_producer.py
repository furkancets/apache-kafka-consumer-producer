from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

for key in range(100):
    time.sleep(0.1)
    producer.send(topic="topic1",
                  key=str(key).encode(),
                  value=("Hi i am from pyhton producer - " + str(key)).encode())

producer.flush()