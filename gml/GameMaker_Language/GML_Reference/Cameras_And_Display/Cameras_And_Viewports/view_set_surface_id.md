# view\_set\_surface\_id

This function sets the surface to draw the contents of the given viewport to.

When working with surfaces, it is often required to capture the *whole* visible region of the screen on the surface, and so you would assign it to a viewport using this function. This means that everything that is shown in the chosen viewport will now be drawn to the assigned surface and the contents of that viewport will no longer be displayed, meaning that you will need to either:

- Enable a new view and draw the surface only in that view (using [view\_current](view_current.md) to check which view is being drawn).
- Draw the surface in the Draw GUI or Post Draw event of an instance, since these events are independent of views.

When using this function you give the viewport index (from 0 to 7\) and a surface (either the [application\_surface](../../Drawing/Surfaces/application_surface.md) or the handle returned by the function [surface\_create](../../Drawing/Surfaces/surface_create.md)) or, if a surface has previously been assigned and you want to remove it, a value of \-1. For more examples on setting the viewport to a surface see the variable [view\_surface\_id](view_surface_id.md).

 
 

#### Syntax:

view\_set\_surface\_id(viewport, surf)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |
| surf | [Surface](../../Drawing/Surfaces/surface_create.md) | The surface to draw the viewport's contents to |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (view\_get\_surface\_id(0\) \=\= \-1\)  

 {  

     view\_set\_surface\_id(0, global.vSurf);  

 }

The above code will check to see if a surface has been assigned to the viewport\[0] and if it has not then one is assigned.
