# http\_post\_string

This function posts a string using the HTTP POST method.

In computing, a **post** request is used when the client needs to send data to the server as part of the retrieval request, such as when uploading a file or submitting a completed form, and the same is true of this function in GameMaker. In contrast to the [http\_get](http_get.md) request method where only a [URL](HTTP.md#urls) is sent to the server, http\_post\_string also includes a string that is sent to the server and may result in the creation of a new resource on the server, the update of an existing one, or both.

 
## Async Callback

This event will generate a "callback" which is picked up by any [HTTP Events](../../../../The_Asset_Editors/Object_Properties/Async_Events/HTTP.md), in which case it will generate a [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) (more commonly known as a "dictionary") that is exclusive to this event and is stored in the special variable [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md). This DS map will contain different values depending on whether there is data being returned or not. For example, if you have requested a file, the event will trigger multiple times as each packet of data is received so that you can show a progress bar, for example.

 
 

#### Syntax:

http\_post\_string(url, string)

| Argument | Type | Description |
| --- | --- | --- |
| url | [String](../../../GML_Overview/Data_Types.md) | The web address of the server that you wish to get information from. See [URLs](HTTP.md#urls) |
| string | [String](../../../GML_Overview/Data_Types.md) | The string you wish to send to the specified URL |

 

#### Returns:

[Async Request ID](../Asynchronous_Functions.md) (or \-1 if something went wrong)

 

#### Example:

The http\_post\_string function can be called from any event, and since it is asynchronous the callback can be almost instantaneous or could take several seconds. Calling the function is simple and would look something like this:

var \_str \= $"name\={player\_name}\&score\={player\_score}";  

 request\_id \= http\_post\_string("http://www.angusgames.com/game?game\_id\={global.game\_id}", \_str);

The above code sends a retrieval request to the specified URL with the given parameters as well as sending the additional data (player name and score in URL\-encoded form) stored in the variable \_str. This will trigger all defined asynchronous **Http Events** if a callback is received, and you can check the "id" returned against that stored in the variable request\_id to make sure that you run the correct code should you have used various http\_post\_string functions. The following example code shows how this would be done:

Async HTTP Event

var \_r\_str \= "null";  

 if (async\_load\[? "id"] \=\= request\_id)  

 {  

     if (async\_load\[? "status"] \=\= 0\)  

     {  

         \_r\_str \= async\_load\[? "result"];  

     }  

 }

The above code will first check the ID of the request, then check the status of the callback. If the value is equal to 0 (signalling completed) the result from the callback will then be stored in a variable for future use, otherwise the variable will simply hold a default value (in this case "null").
