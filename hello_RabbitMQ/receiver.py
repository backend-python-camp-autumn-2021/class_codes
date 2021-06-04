import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange="gol_zadan", exchange_type="fanout")

subscribers_list = ["tv", "web", "radio"]

queue_list = {}

for subscriber in subscribers_list:
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange="gol_zadan", queue=queue_name)
    queue_list.update({subscriber: queue_name})


def gol_tv(ch, method, properties, body):
    print(f"[{time.asctime()}]: gol tv receiver called")
    time.sleep(10)
    print(f"[{time.asctime()}]: received {body.decode()}")


def gol_web(ch, method, properties, body):
    print(f"[{time.asctime()}]: gol web receiver called")
    time.sleep(10)
    print(f"[{time.asctime()}]: received {body.decode()}")


def gol_radio(ch, method, properties, body):
    print(f"[{time.asctime()}]: gol radio receiver called")
    time.sleep(10)
    print(f"[{time.asctime()}]: received {body.decode()}")


for worker_name, queue_name in queue_list.items():
    if worker_name == "tv":
        channel.basic_consume(
            queue=queue_name, on_message_callback=gol_tv, auto_ack=True)
    elif worker_name == "radio":
        channel.basic_consume(
            queue=queue_name, on_message_callback=gol_radio, auto_ack=True)
    elif worker_name == "web":
        channel.basic_consume(
            queue=queue_name, on_message_callback=gol_web, auto_ack=True)

# channel.basic_qos(prefetch_count=1)

print(f"[{time.asctime()}]: receiver start")

channel.start_consuming()
