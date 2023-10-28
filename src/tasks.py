from celery import shared_task

@shared_task
def my_task(arg1, arg2):
    # Your background task logic here
    return arg1, arg2