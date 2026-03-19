# surface\_save

This function will save a surface to disc using the given filename.

The surface *must* be saved as a \*.png format file.

 
 

#### Syntax:

surface\_save(surface\_id, fname)

| Argument | Type | Description |
| --- | --- | --- |
| surface\_id | [Surface](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md) | The surface to set as the drawing target. |
| fname | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of the saved image file. |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(ord("S")))   

 {  

     surface\_save(surf, "test.png");  

 }

The above code will check to see if the user presses the "S" key on the keyboard and if they do it will save the surface indexed in the variable surf to disc.
