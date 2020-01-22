# TreyInteropContributions
Trey's(Elwoods) Contributions to Interop.

Their are two additions so far, the most substantial of which is the interop module. It provides a class with methods that can interact with the server in any way necessary.
Completed functions within it:
  *post telemetry
  *post object
  *login to the server.
Pending:
  *get objects(all objects submitted or by ID
  *get Teams(Including the most recent telemetry of teams.
  *modify existing objects(no method exists in the API to delete, but any number of objects can be posted, and erroneous submissions don't hurt us)
  
To interact with the server using this module, create an instance of connection using the username, password, and ip and port, then use the methods to interact with the server. Additional information can be found in the comments.

The second is a program to take telemetry data from Mission Planner and then submit it. It is divided in to two halves, client and server, because Mission Planner uses a deprecated version of python that doesn't play nice with any modern tools. It is currently in an alpha state.
  
