# audio\_get\_master\_gain

With this function you can get the absolute value for the global volume of all sounds and music for a specific listener.

The default listener index is 0, but you can use the function [audio\_get\_listener\_info](Audio_Listeners/audio_get_listener_info.md) to get the different indices available for the target platform. The gain value returned is based on a linear scale from 0 (silent) to 1 (full volume).

  On some platforms you can have a gain of greater than 1, although a value of 1 is considered "full volume" and anything greater may introduce audio clipping.

 
 

#### Syntax:

audio\_get\_master\_gain(listenerIndex)

| Argument | Type | Description |
| --- | --- | --- |
| listenerIndex | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) or [Audio Listener ID](../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Listeners/Audio_Listeners.md) | The index of the listener to get the gain of. |

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var num \= audio\_get\_listener\_count();  

 for(var i \= 0; i \< num; \+\+i)  

 {  

     var info \= audio\_get\_listener\_info(i);  

     var ind \= info\[? "index"];  

     if audio\_get\_master\_gain(ind) !\= 1  

     {  

         audio\_set\_master\_gain(info\[? "index"], 1\);  

     }  

     ds\_map\_destroy(info);  

 }

The above code loops through the available listeners, checking to see if their gain is 1 or not, and if it is not it sets it to 1 for each of them.
