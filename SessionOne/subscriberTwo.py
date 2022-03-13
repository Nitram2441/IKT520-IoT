import paho.mqtt.client as mqtt
# Up to and including task 5
def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received default callback -> " + msg.topic + " " + str(msg.payload))  # Print a received msg


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Sensor/Temp", 0) #turns out one can actually subscribe using wildcards too. Should one? idk
    

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscription mid: " + str(mid))
    print("granted qos: " + str(granted_qos))


client = mqtt.Client(client_id="12345678", clean_session = False)
client.max_inflight_messages_set(20)
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io")
client.loop_forever()

