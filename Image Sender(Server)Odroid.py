# This is a server application intended to run on the Odroid. It recieves a connection from the client application run on the groundstations, and then sends every image found, so far or forthcoming.

# socket is used for the tcp socket programming
import socket
import watchdog.observers

#The directory where it looks for images.
import base64
clientport = 5334

#initialize a socket, and set it to listen on 38452(arbitrary port)
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
knownimages = {}

#while the script is active, accept inputs on
while(1):

    #bind from any client.
    mysocket.bind(('',int(clientport)))
    mysocket.listen(1)
    connection, client_address = mysocket.accept()

    breakcondition = False

    #The connection is thisconnection.
    while(not breakcondition):
        #MONITOR DIRECTORY
        #SEND ALL EXISTING IMAGES TO CLIENT
        #MONITOR DIRECTORY, SEND ALL NEW IMAGES TO CLIENT
        #NOTE, USE ! marks to indicate end of images
        print()



    #TODO ADD CODE TO CONNECT TO JUDGES SERVER
    mysocket.close()