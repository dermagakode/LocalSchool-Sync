import os
from dotenv import load_dotenv
load_dotenv()

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
  
  print(f'Active as device num {cpuserial}')
  return cpuserial
  
MQTT_HOST=os.getenv('MQTT_HOST')
MQTT_PORT=os.getenv('MQTT_PORT')
MQTT_USER=os.getenv('MQTT_USER')
MQTT_PASS=os.getenv('MQTT_PASS')
MQTT_TOPIC_PREFIX=os.getenv('MQTT_TOPIC_PREFIX')
MQTT_UPDATE_TOPIC= f'{MQTT_TOPIC_PREFIX}/update/{getserial()}' if MQTT_TOPIC_PREFIX else f'update/{getserial()}'
