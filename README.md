# TreyInteropContributions
Trey's(Elwoods) Contributions to Interop.

Their are two additions so far, the most substantial of which is the interop module. It provides a class with methods that can interact with the server in any way necessary.

To interact with the server using this module, create an instance of connection using the username, password, and ip and port, then use the methods to interact with the server. Additional information can be found in the comments.

The second is a program to take telemetry data from Mission Planner and then submit it. It is divided in to two halves, client and server, because Mission Planner uses a deprecated version of python that doesn't play nice with any modern tools. It is currently in an alpha state.

To import the interop module(If its in the same directory as your code):
from interopmodule import *

To use the interop module, first initialize it in the following manner:

myconnection = connection(addresss, port,username, password, verbose)
  
Where:
    Address -The IP address of the judges server, as a string.
    Port - The port the judges server is running on, as an int or string. Will almost certainly be 8000
    Username - Username, as a string
    Password - Password, as a string
    Verbose - A boolean. Determines if the module prints status messages. Defaults to false
    
From there, you can use the various methods of the class to interact with the Judges Server. The exact specifications of each method are listed in comments in the module. 
In general, however:
    *Functions that get things return a python dictionary or a list of python dictionaries, that match the JSON version of the data.
    *The telemetry post function takes in the values "normally," while postodlc and postemergent take in objects of classes odlc and emergentobject,respectively. These classes are defined in the module as well.
    *s
    