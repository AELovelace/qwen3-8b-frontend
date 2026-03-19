# network\_send\_broadcast

This function broadcasts the data from a buffer locally to a range of IP addresses (for more information on buffers see [Buffers](../Buffers/Buffers.md)).

The range is limited to that of the device running the server, such that if the device has an IP of 92\.168\.11\.130, then the data will be broadcast over the range 92\.168\.11\.\*. The function will return the number of bytes of data sent, or a number less than 0 if the send has failed.

  This function will only work when used with UDP \- your server needs to be UDP and your client needs to have a UDP client socket created with [network\_create\_socket\_ext](network_create_socket_ext.md) in order to receive any broadcasts sent from the server.

  This function will not work when used in a project running on the HTML5 target.

 
#### Syntax:

network\_send\_broadcast(socket, port, bufferid, size)

| Argument | Type | Description |
| --- | --- | --- |
| socket | [Network Socket ID](network_create_socket.md) or [Network Server ID](network_create_server.md) | The ID of the socket to use. |
| port | [Real](../../GML_Overview/Data_Types.md) | The port that the server will use. |
| bufferid | [Buffer](../Buffers/buffer_create.md) | The buffer to get the data from. |
| size | [Real](../../GML_Overview/Data_Types.md) | The size (in bytes) of the data. |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

buffer\_seek(broadcast\_buffer, buffer\_seek\_start, 0\);  

 buffer\_write(broadcast\_buffer, buffer\_string, global.server\_name);  

 network\_send\_broadcast(server, 6511, broadcast\_buffer, buffer\_tell(broadcast\_buffer));

The above code writes the name string of the current server (stored in global.server\_name), then writes it to a buffer stored in broadcast\_buffer. This data is then broadcast locally to a range of IPs (the device IP is currently implied as the broadcast base range) to port 6511\.
