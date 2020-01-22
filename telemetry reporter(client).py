#This file is designed to be run by Mission planner, using their provided means for running python scripts.
# it reads the rate at which to send, the ip address, and port number from telemconfig.txt, which is stored in the same directory as the script.
#this file takes the telemetry data from missionplanner, and sends it via tcp to the server, which will run on the client image provided by the judges.
#code by Elwood Simpson(Trey)

#THIS FILE IS MEANT TO BE RUN IN MISSION PLANNER. RUNNING IT DIRECTLY VIA A STANDARD INTERPRETER WILL FAIL

#socket is used for the tcp socket programming.
import socket
#pickle is used to send a python list over tcp
import pickle
#time is used for delay functions in particular, time.sleep
import time

#im pasting the entire class. Fight me.
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



#NumPy is used in place of pickle for Serialization/Deserialization
#import NumPy


#TODO add error checking


#The following code block is for configuration purposes
#add the ip and port to connect to(the current port number is arbitrary
#rate is in hertz, localhost refers to local computer. Substitute with actual ip.
rate = 2
ip = socket.gethostbyname("localhost")
port = 38452


#debug statement
#print("Rate: " + rate + " ip: " + ip + " port: " + port)

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:  
    mysocket.connect((ip,int(port)))
except:
    print("Error, could not make connection with server side.")

#period in full seconds.
period = 1/float(rate)
breakcondition = 1

#test variable
iterator = 1

while(breakcondition):
    #note that cs is used to communicate with mission planner. The error bars are fine.
    #this is used to delay execution
    time.sleep(period)
    latitude = cs.lat
    longitude = cs.lng
    altitude = cs.alt

    #check that this actually gets the heading. Cameron says it does, but check.
    heading = cs.groundcourse
    print([latitude,longitude,altitude,heading])
    #altitude = 6
    iterator += 1
    #print(str(type(latitude)))

    print(str(type(latitude)))
    print(str(type(longitude)))
    print(str(type(altitude)))
    print(str(type(heading)))
    altitude = float(altitude)
    heading = float(heading)
    print(str(type(altitude)))
    print(str(type(heading)))

    #print(str(type(latitude)))


    #pickle is being a dick lets try
    #print("normal: "+str([latitude,longitude,altitude,heading]))
    #print("chad string: " + [float(latitude),float(longitude),float(altitude),int(heading)])
    #print("Get altitude type: " +  str(type(altitude)))

    #convertedlist = [float(longitude),float(latitude),float(altitude),float(heading)]
    #currentpack = telemetry(float(longitude),float(latitude),float(altitude),float(heading),time.time())
    #currentpack = [float(longitude),float(latitude),float(altitude),float(heading),time.time()]
    #currentpack = [iterator,iterator+1,iterator+2, iterator +3]
    currentpack = [latitude,longitude,altitude, heading]
    payload = pickle.dumps(currentpack)
    mysocket.send(payload)
    #breakcondition = mysocket.recv(1024)

mysocket.close()