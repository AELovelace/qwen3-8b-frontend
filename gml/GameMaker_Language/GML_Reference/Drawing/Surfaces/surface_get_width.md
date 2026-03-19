# surface\_get\_width

This function simply returns the width, in pixels, of the given surface.

It should be noted that if you call this to check the [application\_surface](application_surface.md) immediately after having changed its size using [surface\_resize](surface_resize.md), it will not return the new value as the change needs a step or two to be fully processed. After waiting a step it should return the new size correctly.

 
 

#### Syntax:

surface\_get\_width(surface\_id)

| Argument | Type | Description |
| --- | --- | --- |
| surface\_id | [Surface](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md) | The surface to get the width of. |

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

sw \= surface\_get\_width(surf);

The above code will store the width of the surface indexed in the variable surf in the variable sw.
