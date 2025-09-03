from kafka import KafkaProducer 
import json
import time 

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(100,1000):
    data={'event_id':i,'timestamp':time.time(),'value':f'value_{i}'}
    producer.send('real-time-data',value=data)
    print(f'Sent: {data}')
    time.sleep(1)
producer.flush()