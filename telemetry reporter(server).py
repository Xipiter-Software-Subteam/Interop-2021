#this is a program that takes telemetry packets from the client side application using tcp, and sends them using the tools provided by the judges
#it take input from telemserverconfig, which takes the ip address, username, password for connection to the judges server, as well as the port number, for connection with the client side program
#code written by Elwood Simpson(Trey)

#socket is used for the tcp socket programming
import socket

#pickles is used for deserializing the information sent from the client side
import pickle

import marshal

#TODO reformat telemetry as JSON and send it to Ishans application. Also, get the information for Ishan's program from the config file. I guess.

#custom telemetry class
class telemetry:
    def __init__(self,longitude,latitude,altitude,heading,timeof):
        self._longitude = longitude
        self._latitude = latitude
        self._altitude = altitude
        self._heading = heading
        self._timeof = timeof

        def getLong():
            return self._longitude

        def getLat():
            return self._latitude

        def getAlt():
            return self._altitude

        def getHead():
            return self._heading

        def getTime():
            return self._timeof


import time

config = open("telemserverconfig.txt","r")
fullconfig = config.read()
config.close()

#split along the newline characters, and then take each individual line and parse out the data
configlines = fullconfig.split("\n")

string1 = configlines[0]
string1 = string1.split(":")
judgesip = string1[1]

string1 = configlines[1]
string1 = string1.split(":")
judgesport = string1[1]

string1 = configlines[2]
string1 = string1.split(":")
clientport = string1[1]

string1 = configlines[3]
string1 = string1.split(":")
username = string1[1]

string1 = configlines[4]
string1 = string1.split(":")
password = string1[1]

#initialize a socket, and set it to listen on 38452
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind((socket.gethostbyname("localhost"),int(clientport)))
mysocket.listen(1)
connection, client_address = mysocket.accept()

breakcondition = True
while(breakcondition):
    data = connection.recv(1024)
    #print(data)
    payload = pickle.loads(data)
    print(payload)

#TODO ADD CODE TO CONNECT TO JUDGES SERVER
mysocket.close()