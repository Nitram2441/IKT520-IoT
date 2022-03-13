import paho.mqtt.client as mqtt
# Up to and including task 5
def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received default callback -> " + msg.topic + " " + str(msg.payload))  # Print a received msg

def on_message_one(client, userdata, msg):
    print("Message received cybersec/IKT/# callback -> " + msg.topic + " " + str(msg.payload))  # Print a received msg

def on_message_two(client, userdata, msg):
    print("Message received cybersec/+/540 callback -> " + msg.topic + " " + str(msg.payload))  # Print a received msg



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #client.subscribe("CyberSec/IKT520")
    #client.subscribe("CyberSec/IKT530")
    #client.subscribe("CyberSec/IKT540")
    #client.subscribe("CyberSec/IKT550")
    #client.subscribe("CyberSec/IKT550")
    client.subscribe("CyberSec/#") #turns out one can actually subscribe using wildcards too. Should one? idk
    

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscription mid: " + str(mid))
    print("granted qos: " + str(granted_qos))


client = mqtt.Client("example")
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.message_callback_add("CyberSec/IKT/#", on_message_one) #Overrides on_message if within wildcard
client.message_callback_add("CyberSec/+/540", on_message_two) #Overrides on_message if within wildcard
client.connect("mqtt.eclipseprojects.io")
client.loop_forever()

