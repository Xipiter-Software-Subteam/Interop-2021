#This file is designed to be run by Mission planner, using their provided means for running python scripts.
# it reads the rate at which to send, the ip address, and port number from telemconfig.txt, which is stored in the same directory as the script.
#this file takes the telemetry data from missionplanner, and sends it via tcp to the server, which will run on the client image provided by the judges.
#code by Elwood Simpson(Trey)

#THIS FILE IS MEANT TO BE RUN IN MISSION PLANNER. RUNNING IT DIRECTLY VIA A STANDARD INTERPRETER WILL FAIL

#socket is used for the udp socket programming.
import socket
#pickle is used to send a python list over tcp
import pickle
#time is used for delay functions in particular, time.s
from time import clock


#TODO add error checking


#The following code block is for configuration purposes
#add the ip and port to connect to(the current port number is arbitrary
#rate is in hertz, localhost refers to local computer. Substitute with actual ip.
rate = 2
ip = "localhost"
port = 38452
#verbose controls if status messages play, for debugging.
verbose = True


ip = socket.gethostbyname("localhost")

def reporter():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        mysocket.connect((ip,int(port)))
    except:
        print("Error, could not make connection with server side.")

    #period in full seconds.
    period = 1/float(rate)
    breakcondition = False
    timestamp = clock()
    while(not breakcondition):
        #note that cs is used to communicate with mission planner. The error bars are fine.
        if((clock()-timestamp)>=period):
            timestamp = clock()
            latitude = cs.lat
            longitude = cs.lng
            altitude = cs.alt
            heading = cs.groundcourse
            #currentpack = [latitude, longitude, altitude, heading]
            #payload = pickle.dumps(currentpack)
            payload = '{"latitude":'+str(latitude)+',"longitude":' + str(longitude)+',"altitude":' + str(altitude)+',"heading":'+ str(heading)+'}'
            mysocket.send(payload)
            if(verbose):
                print("latitude: "+ str(cs.lat))
                print("Longitude: " + str(cs.lng))
                print("Altitude: "+str(cs.alt))
                print("Heading: "+ str(cs.groundcourse))

        #breakcondition = mysocket.recv(1024)
def main():
    while(1):
        try:
            reporter()
        except:
            print("Error, unexpected end of connection.")
main()
