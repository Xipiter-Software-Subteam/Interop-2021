# This file provides two classes(Object and connection) in order to facilitate transmission of data to the server.
# Code by Elwood Simpson

import json
import requests
import ipaddress
import time


# object is an object as described in the rules
class odlc():
    # initializer. sets character,character color,shape, color, and orientation
    # note that an object doesn't get an id until it is uploaded.
    # getters and setters are a pain. just reinitialize it lol.
    def __init__(self, missionid, alphanumeric, alphanumeric_color, shape, color, characterorientation, latitude,
                 longitude, autonomous, objecttype, description=""):
        # id is the id of the mission this was obtained on. the documentation is sketchy on this subject, but its almost certainly an integer
        self.missionid = missionid
        # alphanumeric is the character.
        self.alphanumeric = alphanumeric
        # alphanumeric_color is the color of the alphanumeric
        self.alphanumeric_color = alphanumeric_color
        # shape is the shape of the object should be a string, in all caps of the shape. The documentation does not provide all the possible shapes
        self.shape = shape
        # color is the color of the shape. Should be a string. in all caps of the color. The documentation does not provide all the possible colors
        self.color = color
        # orientation refers to the orientation of the character relative to the cardinal directions. According to the documentation
        # this can be a string N, E , S , W
        self.characterorientation = characterorientation
        # latitude refers to the latitude of the object
        self.latitude = latitude
        # longitude refers to the longitude should be  dloat
        self.longitude = longitude
        # rather or not the object was obtained using obvious means. Should be a boolean.
        self.autonomous = autonomous
        # type either emergent or standard
        self.objecttype = objecttype
        # description. only used for emergent options
        self.description = description


# an emergent object.


# This is the class definition of a telemetry packet. in addition to the longitude, latitude, altitude and heading required by the judges, it also includes time, so that packets can be determined.
# a class inheriting from this could be used to make a general data pack, for getting other info such as the state of batteries, speed, etc.

# takes latitude, longitude, altitude, heading, and time
# time should be seconds passed since the epoch, to ensure in order delivery of packets
class telemetry:
    def __init__(self, longitude, latitude, altitude, heading, timeof):
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


# connection is the specific connection. is used to do all interactions with the server.

# TODO verify get objects
# TODO verify get list of objects

# TODO modify objects
# TODO get mission
# TODO get teams
# TODO post emergent objects

class connection():
    # this shouldn't be doing anything. if it does, comment it back in.
    # http.client.HTTPConnection

    # Initialization logs in to server when given the address,port, username, and password.
    # all attributes are strings.
    # address and port should just be the ip address in dot notation as a string, i.e.("127.0.0.1") and the port should just be the integer port as a string, it will virtually always be "8000", according to the specifiication.
    # Verbose controls the various status report mesages. Useful if debugging.
    def __init__(self, address, port, username, password, verbose=False):
        # firstly, create  a python dictionary, then convert it to json
        payload = {"username": username, "password": password}
        payload = json.dumps(payload)
        self._address = "http://" + address + ":" + port
        self._verbose = verbose
        # status = requests.post(url = (address + port + "/api/login"),data = payload)
        status = requests.post(url=(self._address + "/api/login"), data=payload)
        if (status.status_code == 200):
            # http is technically stateless. cookies are used to maintain state. Therefore, this must be sent in everything to the server.
            self._sessionid = status.cookies["sessionid"]

        if (self._verbose):
            # debug statements
            print(status.status_code)
            print(status.text)

        return

    # all data types should be floatsa
    def posttelemetry(self, latitude, longitude, altitude, heading):
        # initializes the telemetry as a python dictionary and then uses the JSON library to convert it to JSON, and then it posts it to the server.
        payload = {
            "latitude": latitude,
            "longitude": longitude,
            "altitude": altitude,
            "heading": heading
        }
        payload = json.dumps(payload)
        status = requests.post(url=(self._address + "/api/telemetry"), data=payload,
                               cookies={"sessionid": self._sessionid})
        if (self._verbose):
            print(status.status_code)
            print(status.text)
        return status

    # submission object should be an object of object, as described above. It did not occur to me that object as an instance of a class and object as the things we're looking for are the same word until just now.
    def postobject(self, objectobject):
        # initialize a python dictionary of the object.
        mission = objectobject.missionid
        objecttype = "STANDARD"
        latitude = objectobject.latitude
        longitude = objectobject.longitude
        orientation = objectobject.characterorientation
        shape = objectobject.shape
        shapecolor = objectobject.color
        autonomous = objectobject.autonomous
        alphanumeric = objectobject.alphanumeric
        alphanumeric_color = objectobject.alphanumeric_color
        thisobject = {
            "mission": mission,
            "type": objecttype,
            "latitude": latitude,
            "longitude": longitude,
            "orientation": orientation,
            "shape": shape,
            "shapeColor": shapecolor,
            "autonomous": autonomous,
            "alphanumeric": alphanumeric,
            "alphanumeric_color": alphanumeric_color
        }

        # convert the dictionary to json
        thisobject = json.dumps(thisobject)
        status = requests.post(url=(self._address + "/api/odlcs"), data=thisobject,
                               cookies={"sessionid": self._sessionid})
        if (self._verbose):
            print(status.status_code)
            print(status.text)
        return status

    # object id corresponds to the object that you're querying.
    # if object id is not known, it returns a python list of the first 100 objects. There will be less than that, so edge cases shouldn't happen
    def getobject(self, objectid=False):
        # if objectid has not been set, get a list of the first 100 and return it.
        if (not objectid):
            objectlist = requests.get(url=(self._address + "/api/odlcs"), cookies={"sessionid": self._sessionid})

            if (self._verbose):
                # no fucking clue what this will return, so this tests that.
                print(objectlist.status_code)
                print(type(objectlist.text))
                # This SHOULD return a json formatted object. convert it to an object.
                print(objectlist.text)
                # TODO convert json formatted object to object formatted object. Or a list of objects, as the case may be.
            return objectlist.text
