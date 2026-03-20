# surface\_free

This function frees a surface from memory.

When you are working with surfaces, you should always use this function whenever you are finished using them. Surfaces take up space in memory and so need to be removed, normally at the end of a room, but it can be done at any time depending on the use you put them to. Failure to do so can cause memory leaks which will eventually slow down and crash your game.

 
 

#### Syntax:

surface\_free(surface)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md) | The surface to be freed. |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_escape))   

 {  

     surface\_free(surf);  

     room\_goto(rm\_Menu);  

 }

The above code checks for a key press and if it detects one it frees the memory reserved for the surface indexed in the variable surf and then changes room.
