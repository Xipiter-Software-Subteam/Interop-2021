from interopmodule import *
import requests
import time

def main():
    address = "127.0.0.1"
    port = "8000"
    username = "testuser"
    password = "testpass"

    thisconnection = connection(address, port, username, password, True)
    objectobject = odlc(missionid=1,alphanumeric="A",alphanumeric_color="ORANGE",shape = "RECTANGLE",color = "RED",characterorientation= "N",latitude = 30.592811944444442, longitude = 75.81308972222222,autonomous= True,objecttype = "STANDARD")
    thisconnection.postobject(objectobject)
    thisconnection.posttelemetry(30.592811944444442,75.81308972222222,275.5,90)
    thisconnection.getobject()












main()
