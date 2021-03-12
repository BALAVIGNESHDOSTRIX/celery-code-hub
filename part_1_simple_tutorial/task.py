from celery import Celery
import time

app = Celery('tasks')


@app.task(ignore_result=True)
def HelloWorld():
    time.sleep(10)
    print("Hello Balavignesh.......")

@app.task
def multiply(x,y):
    time.sleep(60)
    return x*y