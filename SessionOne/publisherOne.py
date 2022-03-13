from paho.mqtt import client as mqtt
# Up to and including task 5
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
    #just having fun with the wildcard subscriptions and callbacks
    client.publish("CyberSec/IKT/520", "i am from IKT and should be handled by IKT callback") # cause i have aa multi level wildcard called /IKT/#
    client.publish("CyberSec/IKT/540", "i am from IKT and should be handled by IKT callback, and 540 callback") # fulfills both wildcards
    client.publish("CyberSec/SEC/540", "i am from SEC and should be handled by 540 callback") # cause i have a single level wildcard called /+/540
    client.publish("CyberSec/SEC/570", "i am from SEC and should be handled by default callback") # cause it does not fulfill any wildcard, it defaults
    client.publish("CyberSec/DEF/540", "i am from DEF and should be handled by 540 callback")

client = mqtt.Client("Example")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect("mqtt.eclipseprojects.io")
client.loop_forever()


