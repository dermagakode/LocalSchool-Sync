import os
import shlex
import subprocess

from celery import Celery
from dotenv import load_dotenv

load_dotenv()
app = Celery('sync_new_materials', broker=os.getenv('REDIS_URL'))


def run(self, command):
    try:
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
        output, error = process.communicate()

        assert error == b'' and process.returncode == 0, error.decode('utf-8')
        return (output.decode('utf-8'), error.decode('utf-8'))

    except subprocess.CalledProcessError as e:
        celery_logger.error(f'Error CMD: {e.output}')
        raise ValueError(e.output)

    except AssertionError as e:
        celery_logger.error(f'Error CMD: {e.output}')
        raise ValueError(e)

@app.task
def sync(school, grade):
    teaching_materials = f'{school}/{grade}'
    print(f'syncing {teaching_materials}...')

    run(f'mkdir -p /home/pi/teaching_materials/{teaching_materials}') # folder must be exist
    return run(f'gsutil rsync -d -r "gs://teaching-materials/{teaching_materials}" "/home/pi/teaching_materials/{teaching_materials}/"')
