# network\_create\_server\_raw

This function creates a new network server for your game, using one of the permitted connection protocols (see the constants listed below).

You supply the server type, then give it a port to use, and finally the number of maximum connections that should be permitted at any one time to the server (note that this number is up to you, but too many connected clients will saturate the network or the device CPU won't be able to handle the processing of that number of players, so use with care). The function returns a unique *id* which should be used stored in a variable and used to identify the server in all further network functions, or a value of less than 0 if the connection fails.

When you no longer need the server, remove it from memory with [network\_destroy](network_destroy.md).

 
As this creates a "raw" server, it will not accept nor use any of the built\-in GameMaker data headers for communication, and so you should be using the functions [network\_send\_raw()](network_send_raw.md) and [network\_send\_udp\_raw()](network_send_udp_raw.md) to send unformatted data to the server created.

 

#### Syntax:

network\_create\_server\_raw(type, port, max\_client)

| Argument | Type | Description |
| --- | --- | --- |
| type | [Socket Type Constant](network_create_socket.md) | The type of server to create (see the constants listed below). |
| port | [Real](../../GML_Overview/Data_Types.md) | The port that the server will use. |
| max\_client | [Real](../../GML_Overview/Data_Types.md) | The maximum number of clients that can connect at once. |

 

#### Returns:

[Network Server ID](network_create_server.md)

 

#### Example:

var port \= 6510;  

 server \= network\_create\_server\_raw(network\_socket\_tcp, port, 32\);  

 while (server \< 0 \&\& port \< 65535\)  

 {  

     port\+\+  

     server \= network\_create\_server\_raw(network\_socket\_tcp, port, 32\);  

 }

The above code will try and create a server using TCP through port 6510\. If that port is unavailable, it will then loop through the ports to find one that is.
