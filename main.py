import time
import re
import paho.mqtt.client as paho

from sync_new_materials import sync
from settings import (
    MQTT_HOST, MQTT_PORT,
    MQTT_USER, MQTT_PASS,
    MQTT_TOPIC_PREFIX, MQTT_UPDATE_TOPIC
)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print('Connected with result code ' + str(rc))
        result = client.subscribe(MQTT_UPDATE_TOPIC)
        print(f'Subscribing to: {MQTT_UPDATE_TOPIC} with mid: {result[1]}')

        try:
            with open("/home/pi/registered_user") as file:
                # should read all line and subscribe it 
                pass 
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)

    else:
        print("Not connected")

def on_message(client, userdata, msg):
    try:
        print(f'[{time.time()}] Receiving from : {msg.topic}')
        if msg.topic == MQTT_UPDATE_TOPIC:
            new_topic = f'ntm/{msg.payload.decode("utf-8")}'
            new_topic = f'{MQTT_TOPIC_PREFIX}/{new_topic}' if MQTT_TOPIC_PREFIX else new_topic
            print(f'Subscribe new: {new_topic}')
            client.subscribe(new_topic)
        elif msg.payload is not None:
            print(msg.payload)
            parse_data(
                msg.topic, 
                msg.payload.decode('utf-8')
            )
    except Exception as e:
        print(e)

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"mid {mid} successfully subscribed with QOS: {granted_qos[0]}")

def parse_data(topic, payload):
    topic_format = 'ntm/([^/]+)/([^/]+)' # ntm/school/grade
    topic_format = f'{MQTT_TOPIC_PREFIX}/{topic_format}' if MQTT_TOPIC_PREFIX else topic_format
    match = re.match(topic_format, topic)

    if match:
        school = match.group(1)
        grade = match.group(2)
        sync.delay(school, grade)
    else:
        print('Not match!')
        return None   

if __name__ == "__main__":

    paho.Client.connected_flag=False
    mqtt = paho.Client()

    mqtt.on_connect = on_connect
    mqtt.on_message = on_message
    mqtt.on_subscribe = on_subscribe
    mqtt.username_pw_set(
        MQTT_USER, 
        MQTT_PASS
    )

    mqtt.connect(MQTT_HOST, int(MQTT_PORT))

    print('Doing loop forever')
    mqtt.loop_forever()
