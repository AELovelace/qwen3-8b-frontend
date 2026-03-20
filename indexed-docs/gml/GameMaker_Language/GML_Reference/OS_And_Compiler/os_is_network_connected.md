# os\_is\_network\_connected

With this function you can check if your device currently has an internet connection.

It will return true if it does, or false if it does not. Depending on the value of the attempt\_connection argument and the OS, it may attempt to make a connection before returning a value.

The function has an optional argument to enable/disable it attempting to make a connection when called. When set to anything other than network\_connect\_none the function will attempt to make a connection, and when set to network\_connect\_none it will simply be limited to checking the connection. Note that attempting to make a connection using network\_connect\_blocking may cause the OS to hang for a few seconds.

You can pass one of the following constants into the attempt\_connection argument:

[Attempt Connection Constant](../../../../GameMaker_Language/GML_Reference/OS_And_Compiler/os_is_network_connected.md)

| Constant | Description |
| --- | --- |
| network\_connect\_none / false | This does not attempt to connect. |
| network\_connect\_blocking / true | This attempts to connect and blocks execution while trying. |
| network\_connect\_active / network\_connect\_nonblocking | This will actively prompt the user to fix the connection, if it failed. |
| network\_connect\_passive | This will try to connect and silently fail if no successful connection could be established. |

If the function returns false when using network\_connect\_active or network\_connect\_passive, the actual result is returned later in the Async [Networking](../../../The_Asset_Editors/Object_Properties/Async_Events/Networking.md) event. See: [Attempting Connection](../../../The_Asset_Editors/Object_Properties/Async_Events/Networking.md#h)

  This function checks the internal device API that controls connections and so may return true if there is a Bluetooth connection, a Wi\-Fi connection, or even just a normal network connection that permits internet access. This means it may not always be accurate on all platforms.

#### Syntax:

os\_is\_network\_connected(\[attempt\_connection])

| Argument | Type | Description |
| --- | --- | --- |
| attempt\_connection | [Attempt Connection Constant](../../../../GameMaker_Language/GML_Reference/OS_And_Compiler/os_is_network_connected.md) | Set this parameter to a value other than network\_connect\_none to attempt an OS level connection when called. |

 

[Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if os\_is\_network\_connected()  

 {  

     global.connected \= true;  

 }

The above code checks to see if the device has a connection to the internet and if so it sets a global variable.
