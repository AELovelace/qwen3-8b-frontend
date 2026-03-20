# http\_get\_file

This function connects to the specified URL in order to retrieve information in the form of a file.

As this is an asynchronous function, GameMaker will not block while waiting for a reply, but will keep on running unless it gets callback information. This information will be in the form of a string and will trigger an **Async HTTP Event** in any instance that has one defined in their object events.

 
## Async Callback

This event will generate a "callback" which is picked up by any [HTTP Events](../../../../The_Asset_Editors/Object_Properties/Async_Events/HTTP.md), in which case it will generate a [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) (more commonly known as a "dictionary") that is exclusive to this event and is stored in the special variable [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md). This DS map will contain different values depending on the data being returned, i.e.: the event will trigger multiple times as each packet of data is received so that you can show a progress bar, for example.

 
 

#### Syntax:

http\_get\_file(url, local\_target)

| Argument | Type | Description |
| --- | --- | --- |
| url | [String](../../../GML_Overview/Data_Types.md) | The web address of the server that you wish to get the file from. See [URLs](HTTP.md#urls) |
| local\_target | [String](../../../GML_Overview/Data_Types.md) | The local storage path to save the file to |

 

#### Returns:

[Async Request ID](../Asynchronous_Functions.md) (or \-1 if something went wrong)

 

#### Example:

The http\_get\_file function can be called from any event, and since it is asynchronous the callback can be almost instantaneous or could take several seconds. Calling the function is simple and would look something like this:

request\_id \= http\_get\_file("http://www.macsweeneygames.com/downloads/upgrade.zip", "\\Downloads\\Upgrade.zip");

The above code will request a file from the given URL and set it to be downloaded to the local storage area (as specified in the HTML5 Game Options), in a directory "Downloads" with the given file name (this does not have to be the same as the source file name, but should use the same file extension). The [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) map's "id" will be stored in the variable request\_id so you can check for the correct callback in the Asynchronous Event, and if the save directory does not exist, it will be created. The Asynchronous Event triggered would be the [HTTP](../../../../The_Asset_Editors/Object_Properties/Async_Events/HTTP.md) sub\-event, and in that event you would have something like the following:

Async HTTP Event

if (async\_load\[? "id"] \=\= request\_id)  

 {  

     var \_status \= async\_load\[? "status"];  

     if (\_status \=\= 0\)  

     {  

         var \_path \= async\_load\[? "result"];  

         var \_files \= zip\_unzip(path, "/NewContent/");  

         if (\_files \> 0\)  

         {  

             global.extra\_content \= true;  

         }  

     }  

 }

The above code will first check the "id" of the request, then check the status of the request. If the value is equal to 0 (signalling completed), the result will then be used along with the [zip\_unzip](../../File_Handling/Encoding_And_Hashing/zip_unzip.md) function to unzip the downloaded file to the given directory. If the unzip succeeds a global variable is set to true.
