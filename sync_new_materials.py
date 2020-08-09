import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()
app = Celery('sync_new_materials', broker=os.getenv('REDIS_URL'))

@app.task
def sync(school, grade):
    return f'syncing {school}/{grade}...'