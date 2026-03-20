# surface\_copy

This function simply takes the image from one surface and copies it onto another one at the specified local position within that surface (where the (0, 0\) position is the top left corner of the destination surface). If the destination surface already has information this will be overwritten by the copy, and the function does *not* change the source surface in any way.

 
 

#### Syntax:

surface\_copy(destination, x, y, source)

| Argument | Type | Description |
| --- | --- | --- |
| destination | [Surface](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md) | The surface to copy the other surface to. |
| x | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The x position to copy to. |
| y | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The y position to copy to. |
| source | [Surface](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md) | The surface to be copied. |

 

#### Returns:

N/A

 

#### Example:

if (view\_current \=\= 0\)   

 {  

     surface\_copy(surf, 0, 0, temp\_surf);  

 }  

 else  

 {  

     draw\_surface(surf, 0, 0\);  

 }

The above code checks the current view being drawn. If it is view\[0] it copies the surface stored in the variable temp\_surf onto the surface in the variable surf. If the current view is anything other than view\[0] the surface surf is drawn to the screen.
