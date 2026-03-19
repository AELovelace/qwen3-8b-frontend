# network\_set\_timeout

With this function you can set the timeout for reading and writing data to/from a server through the given socket. Note that the timeout does not generate any type of event, so you will need to deal with timeouts yourself using alarms (for example). Note that this value only affects the sending and receiving of data, and should you wish to change the connection timeout value then you should be using the function [network\_set\_config()](network_set_config.md).

 

#### Syntax:

network\_set\_timeout(socket, read\_timeout, write\_timeout)

| Argument | Type | Description |
| --- | --- | --- |
| socket | [Network Socket ID](GameMaker_Language/GML_Reference/Networking/network_create_socket.md) | The id of the socket to use. |
| read\_timeout | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The milliseconds in which a transfer from a server will timeout. |
| write\_timeout | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The milliseconds in which a transfer to a server will timeout. |

 

#### Returns:

N/A

 

#### Example:

network\_set\_timeout(sock, 3000, 3000\);

The above code will set the timeout for reading and writing data through the socket indexed in the variable "sock" to 3 seconds.
