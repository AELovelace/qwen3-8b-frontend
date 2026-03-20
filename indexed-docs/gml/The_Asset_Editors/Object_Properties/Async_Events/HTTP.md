# HTTP

### 

The Async HTTP Event is triggered by the [callback](#) from one of the [http\_\*() functions](../../../GameMaker_Language/GML_Reference/Asynchronous_Functions/HTTP/HTTP.md), like [http\_post\_string](../../../GameMaker_Language/GML_Reference/Asynchronous_Functions/HTTP/http_post_string.md). It isn't triggered for every single data packet that is received, but rather updates within the main game loop during the download.

A [DS Map](../../../GameMaker_Language/GML_Reference/Data_Structures/DS_Maps/DS_Maps.md) that is exclusive to this event is stored in the special variable [async\_load](../../../GameMaker_Language/GML_Overview/Variables/Builtin_Global_Variables/async_load.md) and can be accessed in this event (please see the individual functions for code examples that explain the use of this event in further detail).
