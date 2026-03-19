# network\_send\_udp\_raw

This function sends data over the network using UDP to a server.

The function takes the [Network Socket ID](network_create_socket.md) to connect through, the URL to connect to and the port to use. You must then supply the [Buffer](../Buffers/buffer_create.md) which contains the data to be sent (for more information on buffers see [Reference \- Buffers](../Buffers/Buffers.md)) and finally the size (in bytes) of the data. The function returns the number of bytes of data sent, or a number less than 0 if the send has failed.

The data sent is not formatted by GameMaker in any way and the receiving devices will get the packets in the exact form they were sent in.

UDP is "connectionless" in that you don't actually do a connect, you just send a packet directly to an IP, and the server gets incoming data from an IP address and has to deal with it "as is".

NOTE This function will not work when used in a project running on the HTML5 target, and neither will HTML5 projects be able to receive UDP.

 
 

#### Syntax:

network\_send\_udp\_raw(socket, url, port, bufferid, size)

| Argument | Type | Description |
| --- | --- | --- |
| socket | [Network Socket ID](network_create_socket.md) or [Network Server ID](network_create_server.md) | The id of the socket to use. |
| url | [String](../../GML_Overview/Data_Types.md) | The URL or IP to connect to (a string, can be IPv4 or IPv6\). |
| port | [Real](../../GML_Overview/Data_Types.md) | The port to connect to. |
| bufferid | [Buffer](../Buffers/buffer_create.md) | The buffer to get the data from. |
| size | [Real](../../GML_Overview/Data_Types.md) | The size (in bytes) of the data. |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

network\_send\_udp\_raw(sock, "www.macsweeneygames.com", 6510, buff, buffer\_tell(buff));

The above code will send a raw UDP packet to the server defined by the URL on the port 6510\. The data is taken from the buffer in the variable buff.
