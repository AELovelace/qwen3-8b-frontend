# network\_send\_raw

This function sends a "raw" data packet through the network.

The function takes the [Network Socket ID](network_create_socket.md) to connect through and then you must supply the [Buffer](../Buffers/buffer_create.md) which contains the data to be sent (for more information on buffers see [Reference \- Buffers](../Buffers/Buffers.md)) and finally the size (in bytes) of the data packet.

The data sent is not formatted by GameMaker in any way and the receiving devices will get the data as a stream which means you will have to handle it yourself. See: [Packet Separation](Networking.md#h)

The function will return the number of bytes of data sent, or a number less than 0 if the send has failed.

   

 
## Options Argument

The last argument is optional, and is only used with WebSockets. It allows you to choose between sending binary or text data. Either of these constants can be specified in this argument:

| [Network Send Type Constant](network_send_raw.md) | |
| --- | --- |
| Constant | Description |
| network\_send\_binary | Send a binary message |
| network\_send\_text | Send a text message |

The APIs for some platforms only accept text messages when using WebSockets (e.g. Twitch), so the network\_send\_text constant can be used in such cases. If this argument is not specified, binary data is sent by default.

 

#### Syntax:

network\_send\_raw(socket, bufferid, size, \[options])

| Argument | Type | Description |
| --- | --- | --- |
| socket | [Network Socket ID](network_create_socket.md) | The id of the socket to use. |
| bufferid | [Buffer](../Buffers/buffer_create.md) | The buffer to get the data from. |
| size | [Real](../../GML_Overview/Data_Types.md) | The size (in bytes) of the data. |
| options | [Network Send Type Constant](network_send_raw.md) | Used for WebSockets to choose between text and binary data; if not specified, binary data is sent. |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

buff \= buffer\_load("player\_save.dat");  

 network\_send\_raw(sock, buff, buffer\_get\_size(buff));

The above information loads previously saved data into a buffer in memory and stores the buffer in the variable buff. This complete buffer is then send as a raw data packet over the network using the socket identified by the variable sock.
