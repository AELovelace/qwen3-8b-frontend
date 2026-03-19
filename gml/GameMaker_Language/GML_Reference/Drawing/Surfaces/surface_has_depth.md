# surface\_has\_depth

This function returns whether the given surface has a depth buffer (and by relation, a stencil buffer, as depth buffer creation needs to be enabled for stencil buffers to also be created).

  You can use [surface\_depth\_disable](surface_depth_disable.md) to enable/disable whether surfaces are [created](surface_create.md "surface_create()") with a depth buffer or not.

 

#### Syntax:

surface\_has\_depth(surface)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](surface_create.md) | The surface to check |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_has\_depth \= surface\_has\_depth(surf\_colour);  

 if (!\_has\_depth)  

 {  

     show\_debug\_message("surf\_colour has no depth buffer.");  

 }

The above code calls surface\_has\_depth to check if the surface held in a variable surf\_colour has a depth buffer and stores the result in a local variable \_has\_depth. If the surface has no depth buffer, a debug message is shown.
