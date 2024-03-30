# Se importa KafkaProducer desde la librería kafka-python, 
# que se utiliza para enviar mensajes a los brokers de Kafka.
from kafka import KafkaProducer
# Importa el módulo json, que permite la serialización de objetos Python a JSON y viceversa.
import json

# Se crea una instancia de KafkaProducer. 
# bootstrap_servers: Especifica la lista de brokers a los que el productor debe conectarse inicialmente.
# value_serializer: Función utilizada para convertir los datos que se enviarán a Kafka en bytes. 
# En este caso, se serializa el mensaje como JSON y luego se codifica a utf-8.
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Define un mensaje a enviar. Aquí, es un simple diccionario Python.
data = {'key': 'value'}

# Envia el mensaje al topic 'test-topic'. 
# 'value=data' indica que el diccionario 'data' se serializará como JSON y luego se enviará como el cuerpo del mensaje.
producer.send('test-topic', value=data)

# Llama a flush para asegurar que todos los mensajes pendientes sean enviados a Kafka antes de cerrar el productor.
# Esto es particularmente útil para garantizar que no haya mensajes en buffer esperando ser enviados.
producer.flush()
