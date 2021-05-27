from celery import shared_task


@shared_task
def hello_task(name):
    return f"hello celery to {name}"
