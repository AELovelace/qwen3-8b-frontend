# surface\_copy\_part

This function simply takes the image from one surface and copies part of it onto another one at the specified local position within that surface (where the (0, 0\) position is the top left corner of the destination surface). You can specify a local x and y position to copy from as well as the width and height of the section. Please note that these are coordinates based on the *surface size* and not on the position at which the surface is being drawn in the room. If the destination surface already has information this will be overwritten by the copy, and the function does *not* change the source surface in any way.

 
 

#### Syntax:

surface\_copy\_part(destination, x, y, source, xs, ys, ws, hs)

| Argument | Type | Description |
| --- | --- | --- |
| destination | [Surface](surface_create.md) | The surface to copy the other surface to. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position to copy to. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position to copy to. |
| source | [Surface](surface_create.md) | The surface to be copied. |
| xs | [Real](../../../GML_Overview/Data_Types.md) | The x position in the source surface to copy from. |
| ys | [Real](../../../GML_Overview/Data_Types.md) | The y position in the source surface to copy from. |
| ws | [Real](../../../GML_Overview/Data_Types.md) | The width of the area in the source surface to copy from. |
| hs | [Real](../../../GML_Overview/Data_Types.md) | The height of the area in the source surface to copy from. |

 

#### Returns:

N/A

 

#### Example:

if (view\_current \=\= 0\)  

 {  

     var \_cam1\_x \= camera\_get\_view\_x(view\_camera\[1]);  

     var \_cam1\_y \= camera\_get\_view\_y(view\_camera\[1]);  

  

     surface\_copy\_part(surf, 0, 0, temp\_surf, 0, 0, \_cam1\_x \- mouse\_x, \_cam1\_y \- mouse\_y);  

 }  

 else  

 {  

     draw\_surface(surf, 0, 0\);  

 }
 

The above code checks the current view being drawn. If it's view\[0] it copies the surface indexed in the variable temp\_surf onto the surface indexed in the variable surf. The area copied corresponds to a rectangle formed by the relative position of the mouse within the surface as it would be drawn in view\[1]. If the current view is anything other than view\[0] the surface surf is drawn to the screen.
