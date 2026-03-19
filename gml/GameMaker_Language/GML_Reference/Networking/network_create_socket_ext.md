# network\_create\_socket\_ext

This function creates a new client socket for your game to communicate over the network.

You must define the socket type (see the list of constants below) and give a port to use, and the function will return a unique *id* which should be used in all further function calls for that socket, or a value of less than 0 if the connection fails. When you no longer need the socket, remove it from memory with [network\_destroy](network_destroy.md).

 
 
 

#### Syntax:

network\_create\_socket\_ext(protocol, port)

| Argument | Type | Description |
| --- | --- | --- |
| protocol | [Socket Type Constant](network_create_socket.md) | The network protocol to use |
| port | [Real](../../GML_Overview/Data_Types.md) | The port to use |

 

#### Returns:

[Network Socket ID](network_create_socket.md)

 

#### Example:

client \= network\_create\_socket\_ext(network\_socket\_udp, 6510\);

The above code will create a new UDP socket on port 6510\.
