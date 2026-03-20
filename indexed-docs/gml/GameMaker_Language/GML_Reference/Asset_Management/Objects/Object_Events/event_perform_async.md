# event\_perform\_async

This function is used to perform any one of the [Asynchronous Events](../../../../../The_Asset_Editors/Object_Properties/Async_Events.md) provided in GameMaker. You supply the Async event constant (shown in the table below) and a [DS Map](../../../Data_Structures/DS_Maps/ds_map_create.md) which will be available in the called Async event in the [async\_load](../../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) variable.

| [Async Event Type Constant](event_perform_async.md) | |
| --- | --- |
| Constant | Description |
| **ev\_async\_web\_image\_load** | Image Loaded event |
| **ev\_async\_web** | HTTP event |
| **ev\_async\_dialog** | Dialog event |
| **ev\_async\_web\_iap** | In\-App Purchase event |
| **ev\_async\_web\_cloud** | Cloud event |
| **ev\_async\_web\_networking** | Networking event |
| **ev\_async\_web\_steam** | Steam event |
| **ev\_async\_social** | Social event |
| **ev\_async\_push\_notification** | Push Notification event |
| **ev\_async\_save\_load** | Save/Load Event |
| **ev\_async\_audio\_recording** | Audio Recording event |
| **ev\_async\_audio\_playback** | Audio Playback event |
| **ev\_async\_audio\_playback\_ended** | Audio Playback Ended event |
| **ev\_async\_system\_event** | System event |

Non\-asynchronous events can be called using [event\_perform](event_perform.md).

  The DS map specified in the second argument does not have to be destroyed manually as it will automatically be destroyed by the function after the Async event has been performed.

 

#### Syntax:

event\_perform\_async(type, ds\_map)

| Argument | Type | Description |
| --- | --- | --- |
| type | [Async Event Type Constant](event_perform_async.md) | The type of event to perform (see the table above). |
| ds\_map | [DS Map](../../../Data_Structures/DS_Maps/ds_map_create.md) | The DS map to use as [async\_load](../../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) in the called event. |

 

#### Returns:

N/A

#### Example:

var \_map \= ds\_map\_create();  

  

 \_map\[? "id"] \= "custom\_async\_event";  

 \_map\[? "result"] \= true;  

 \_map\[? "data"] \= { a: 13, b: 16 };  

  

 event\_perform\_async(ev\_async\_social, \_map);
 

The above code creates a DS map and populates it with custom entries to be read in the Async event. It then performs the Async Social event with the newly created map passed in as [async\_load](../../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) for the called event.
