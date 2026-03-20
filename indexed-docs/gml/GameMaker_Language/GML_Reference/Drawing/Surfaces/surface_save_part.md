# surface\_save\_part

This function saves part of a surface to disc using the given filename.

The surface *must* be saved as a \*.png format file, and the (x, y) position must be given as local coordinates to the surface, bearing in mind that the top left corner of the surface is always (0, 0\).

 
 

#### Syntax:

surface\_save\_part(surface\_id, fname, x, y, width, height)

| Argument | Type | Description |
| --- | --- | --- |
| surface\_id | [Surface](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md) | The surface to set as the drawing target. |
| fname | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of the saved image file. |
| x | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The starting x position within the surface. |
| y | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The starting y position within the surface. |
| width | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The width of the part to save. |
| height | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The height of the part to save. |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(ord("S")))   

 {  

     surface\_save\_part(surf, "test.png", 0, 0, 100, 100\);  

 }

The above code will check to see if the user presses the "S" key on the keyboard and if they do it will save a part of the surface indexed in the variable surf to disc.
