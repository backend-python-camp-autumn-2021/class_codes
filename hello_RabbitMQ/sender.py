import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange="gol_zadan", exchange_type="fanout")

message = "Messi gol zad"

channel.basic_publish(exchange="gol_zadan", routing_key="", body=message)

time.asctime
print(f"{time.asctime()}: sender send {message}")

connection.close()
