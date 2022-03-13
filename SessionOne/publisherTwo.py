from paho.mqtt import client as mqtt
# Task 6 - 8
def on_publish(client, userdata, mid):
    print("client = " + str(client))
    print("userdata = " + str(userdata))
    print("mid = " + str(mid))
    client.disconnect()

def on_connect(client, userdata, flags, rc):
    print("Client: " + str(client))
    print("Userdata: " + str(userdata))
    print("Connected with result code "+str(rc))
    print("Flags: " + str(flags))
    client.publish("Sensor/Temp", "I AM GROOT", 2) 

client = mqtt.Client("Example")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect("mqtt.eclipseprojects.io")
client.loop_forever()


