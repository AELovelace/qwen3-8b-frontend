# http\_get

This function sends a GET request to the specified URL in order to retrieve information.

This is an asynchronous function, so GameMaker will not block while waiting for a reply, but will keep on running unless it gets callback information. This information will be in the form of a string and will trigger an **Async HTTP Event** in any instance that has one defined in its object events.

 
## Async Callback

This function will generate multiple "callbacks" which are picked up by any [HTTP Events](../../../../The_Asset_Editors/Object_Properties/Async_Events/HTTP.md). These will generate a [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) (more commonly known as a "dictionary") that is exclusive to this event and is stored in the special variable [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md). This DS map will contain different values depending on whether there is data being returned or not. For example, if you have requested a file, the event will trigger multiple times as each packet of data is received so that you can show a progress bar, for example.

 
 

#### Syntax:

http\_get(url)

| Argument | Type | Description |
| --- | --- | --- |
| url | [String](../../../GML_Overview/Data_Types.md) | The web address of the server that you wish to get information from. See [URLs](HTTP.md#urls) |

 

#### Returns:

[Async Request ID](../Asynchronous_Functions.md) (or \-1 if something went wrong)

 

#### Example:

The http\_get function can be called from any event, and since it's asynchronous the callback can be almost instantaneous or could take several seconds. Calling the function is simple and looks something like this:

request\_id \= http\_get($"http://www.macsweeneygames.com/logon?username\={name}");

The above code will pass the string held in the variable name to the given server as well as retrieve the data from that URL, triggering an Async Event which will contain the [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) DS map (the async\_load map index will be stored in the variable request\_id so you can check for the correct callback). The Async Event triggered would be the [HTTP](../../../../The_Asset_Editors/Object_Properties/Async_Events/HTTP.md) sub\-event, and in that event you would have the following:

Async HTTP Event

if (async\_load\[? "id"] \=\= request\_id)  

 {  

     var \_status \= async\_load\[? "status"];  

     var \_r\_str \= (\_status \=\= 0\) ? async\_load\[? "result"] : "null";  

 }

The above code first checks the ID of the async request, then assigns a value to \_r\_str depending on the "status" of the callback. If the value is equal to 0 (signalling the request completed), the result from the callback is stored in a variable for future use, otherwise the variable is set to a default value (in this case "null").
