# network\_send\_packet

This function sends a data "packet" through the network.

The function takes the [Network Socket ID](../../../../GameMaker_Language/GML_Reference/Networking/network_create_socket.md)to connect through and then you supply the [Buffer](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) which contains the data to be sent (for more information on buffers see [Reference \- Buffers](../Buffers/Buffers.md)) and finally the size (in bytes) of the data packet.

Packets sent with this function are formatted such that the GameMaker game receiving the data can "split" the packets correctly, and the function will return the number of bytes of data sent, or a number less than 0 if the send has failed. It is worth noting that the final size of the data being sent that is returned by this function will also include the GameMaker header information, which is an additional 12 bytes.

   

 
 

#### Syntax:

network\_send\_packet(socket, bufferid, size)

| Argument | Type | Description |
| --- | --- | --- |
| socket | [Network Socket ID](../../../../GameMaker_Language/GML_Reference/Networking/network_create_socket.md) | The id of the socket to use. |
| bufferid | [Buffer](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) | The buffer to get the data from. |
| size | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The size (in bytes) of the data. |

 

#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

buff \= buffer\_load("player\_save.dat");  

 network\_send\_packet(sock, buff, buffer\_get\_size(buff));

The above code loads previously saved data into a buffer in memory and stores the newly created buffer in the variable buff. This complete buffer is then send as a packet over the network using the socket identified by the variable sock.
