#this is a program that takes telemetry packets from the client side application using tcp, and sends them using the tools provided by the judges
#it take input from telemserverconfig, which takes the ip address, username, password for connection to the judges server, as well as the port number, for connection with the client side program
#code written by Elwood Simpson(Trey)

#socket is used for the tcp socket programming
import socket

#pickles is used for deserializing the information sent from the client side
import pickle

#the interop module I spent too many hours of my life writing.
from interopmodule import *

import json
#time, for timestamps
import time


#TODO reformat telemetry as JSON and send it to Ishans application. Also, get the information for Ishan's program from the config file. I guess.
judgesip = "192.168.1.102"
judgesport = 8000

clientaddress = "localhost"
clientport = 38452

username = "testuser"
password = "testpass"



#initilialize connection with server.
thisconnection = connection(judgesip,judgesport,username, password, True)

#initialize a socket, and set it to listen on 38452(arbitrary port)
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#THIS HAS BEEN ALTERED
#mysocket.bind((socket.gethostbyname(clientaddress),int(clientport)))
mysocket.bind(('',int(clientport)))
mysocket.listen(1)
connection, client_address = mysocket.accept()

breakcondition = False

#The connection is thisconnection.
while(not breakcondition):
    data = connection.recv(1024)
    telemetrypack = json.loads(data)
    latitude = telemetrypack["latitude"]
    longitude = telemetrypack["longitude"]
    altitude = telemetrypack["altitude"]
    heading = telemetrypack["heading"]
    thisconnection.posttelemetry(latitude,longitude,altitude,heading)



#TODO ADD CODE TO CONNECT TO JUDGES SERVER
mysocket.close()