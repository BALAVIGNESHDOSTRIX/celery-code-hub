# Create Virtualenv by using Following Command
    > virtualenv --python=/user/bin/python3 celery-task

# Install Requirements
    > pip3 install requirements.txt

# Run the Celery with worker1 with concurrency is 7
    > celery -A task worker --loglevel=info --concurrency=7 -n wkr1@hostname

# Run the Celery with worker2 with concurrency is 7
    > celery -A task worker --loglevel=info --concurrency=7 -n wkr2@hostname

# Run the Celery with Flower
    > celery -A task flower --loglevel=info

# Executions
    > from task import HelloWorld
    > d = HelloWorld.delay()
    > result = d.AsyncResult(d.task_id)
    > result
