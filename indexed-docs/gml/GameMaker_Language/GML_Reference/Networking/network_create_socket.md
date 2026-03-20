# network\_create\_socket

This function creates a new client socket for your game to communicate over the network.

You must define the socket type (see the list of constants below) and the function will return a unique *id* for that socket, which should be used in all further function calls for that socket, or a value of less than 0 if the connection fails. When you no longer need the socket, remove it from memory with [network\_destroy](network_destroy.md).

TIP You can use the IP "127\.0\.0\.1" to connect back to the same device that is running the game.

 
 
 
 

 

#### Syntax:

network\_create\_socket(type)

| Argument | Type | Description |
| --- | --- | --- |
| type | [Socket Type Constant](network_create_socket.md) | The type of socket connection to create (see the constants listed above). |

 

#### Returns:

[Network Socket ID](network_create_socket.md)

 

#### Example:

if (os\_browser \=\= browser\_not\_a\_browser)  

 {  

     client \= network\_create\_socket(network\_socket\_tcp);  

     network\_connect( client, "192\.134\.0\.1", 6510 );  

 }  

 else  

 {  

     client \= network\_create\_socket(network\_socket\_ws);  

     network\_connect\_raw\_async( client, "192\.134\.0\.1", 6520 );  

 }

The above code will check whether the game is running in a browser or not and create a new TCP or Web socket before attempting to connect through that to the given IP address on the given port.
