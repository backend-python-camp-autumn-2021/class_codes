import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange="gol_zadan", exchange_type="fanout")

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange="gol_zadan", queue=queue_name)


def gol_web(ch, method, properties, body):
    print(f"[{time.asctime()}]: gol web receiver called")
    time.sleep(10)
    print(f"[{time.asctime()}]: received {body.decode()}")


channel.basic_consume(
    queue=queue_name, on_message_callback=gol_web, auto_ack=True)

print(f"[{time.asctime()}]: receiver start")

channel.start_consuming()
