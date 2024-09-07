from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Exemplo de envio de dados para o Kafka
for i in range(100):
    data = {'id': i, 'value': i*10, 'timestamp': time.time()}
    producer.send('datum_topic', value=data)
    print(f'Dados enviados: {data}')
    time.sleep(1)

producer.flush()
