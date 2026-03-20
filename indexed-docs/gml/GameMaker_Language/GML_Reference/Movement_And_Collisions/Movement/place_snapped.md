# place\_snapped

With this function you can check and see if the origin of an instance (its x and y position) is aligned to a grid with the hsnap and vsnap values specified by you.

 

#### Syntax:

place\_snapped(hsnap, vsnap)

| Argument | Type | Description |
| --- | --- | --- |
| hsnap | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The horizontal snapping to check. |
| vsnap | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The vertical snapping to check. |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

with (obj\_Pieces)  

 {  

     if (!place\_snapped(32, 32\))   

     {  

         move\_snap(32, 32\);  

     }  

 }

The above code checks all instances of "obj\_Pieces" to see if they are snapped to a grid of 32x32 pixels, and if they are not it snaps them to the nearest position in that grid.
