# surface\_get\_height

This function simply returns the height, in pixels, of the given surface.

It should be noted that if you call this to check the [application\_surface](application_surface.md) immediately after having changed its size using [surface\_resize](surface_resize.md), it will not return the new value as the change needs a step or two to be fully processed. After waiting a step it should return the new size correctly.

 
 

#### Syntax:

surface\_get\_height(surface\_id)

| Argument | Type | Description |
| --- | --- | --- |
| surface\_id | [Surface](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md) | The surface to get the height of. |

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

sh \= surface\_get\_height(surf);

The above code will store the height of the surface indexed in the variable surf in the variable sh.
