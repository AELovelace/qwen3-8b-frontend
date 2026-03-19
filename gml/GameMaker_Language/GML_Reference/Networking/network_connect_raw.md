# network\_connect\_raw

This function sends a request to connect to a server.

It takes the *socket id* to connect through (see [network\_create\_socket](network_create_socket.md)) and requires you to give the IP address to connect to (a string, can be IPv4 or IPv6\) as well as the port to connect through. If the connection fails a value of less than 0 will be returned.

The difference between this function and [network\_connect](network_connect.md) is that this function can connect to any server and does nothing to the raw data, so you have to implement the protocols yourself at the server end.

Note that by default the function is synchronous, so your game may appear to "hang" as the connection is made. You can set a timeout value for connection, or alternatively make the creation asynchronous, using the function [network\_set\_config](network_set_config.md), or alternatively use the function [network\_connect\_raw\_async](network_connect_raw_async.md) instead.

NOTE You cannot use this function on HTML5\. For WebSockets, use the [Async function](network_connect_raw_async.md).

 
 

#### Syntax:

network\_connect\_raw(socket, url, port)

| Argument | Type | Description |
| --- | --- | --- |
| socket | [Network Socket ID](GameMaker_Language/GML_Reference/Networking/network_create_socket.md) | The id of the socket to use. |
| url | [String](GameMaker_Language/GML_Overview/Data_Types.md) | The URL or IP to connect to (a string). |
| port | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The port to connect to. |

 

#### Returns:

[Real](GameMaker_Language/GML_Overview/Data_Types.md) or [Network Socket ID](GameMaker_Language/GML_Reference/Networking/network_create_socket.md)

 

#### Example:

client \= network\_create\_socket(network\_socket\_tcp);  

 network\_connect\_raw(client, "www.macsweeneygames.com", 6510\);

The above code will create a new TCP socket then attempt to create a "raw" connection through that to the given URL on port 6510\.
