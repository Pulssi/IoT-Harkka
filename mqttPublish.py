'''
Module for mqtt messaging. Handles all the publishing
of received data to the mqtt broker using the
correct topic.
'''

import paho.mqtt.client as mqtt
import time


def publishMsg(msg):
    # Setup all the nescessary topic, broker and client values
    PUB_TOPIC_1="/iotharkka"
    broker="localhost"
    port=1883
    alive=60
    client_id="testi"

    # Create a MQTT client
    client = mqtt.Client(client_id,True)
    client.connect(broker,port,alive)
    client.loop_start()

    # Publish the message
    (rc,mid) = client.publish(PUB_TOPIC_1,msg,0,True)
    time.sleep(1)

    # Close the client
    print("Viesti julkaistu\n")
    client.loop_stop()
    client.disconnect()



