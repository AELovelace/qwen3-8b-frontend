# view\_surface\_id

With this variable you can set the contents of a given viewport to draw to a surface, or get a reference to the current surface if one has been assigned to a viewport. When working with surfaces, it is often required that you capture the *whole* visible region of the screen on the surface, and so you would assign it to a viewport using this variable. This means that everything that is shown in the chosen view will now be drawn to the assigned surface. The view will now *not* be drawn to the screen, meaning that you will need to either:

- Enable a new view and draw the surface only in that view (using [view\_current](view_current.md) to check which view is being drawn)
- Draw the surface in the Draw GUI or Post Draw event of an instance, since these events are independent of views.

You can also read this variable to get the surface that has been assigned to the chosen view or it will return an invalid handle (\-1) if no surface has been assigned, and generally the surface used for this function should be the size of the view camera itself (not the viewport). The extended example below shows a basic setup for capturing a view and drawing it in the **Draw GUI** event, and for more information on surfaces see the section [Surfaces](../../Drawing/Surfaces/Surfaces.md).

Note that you can also set a viewport to a surface using the function [view\_set\_surface\_id](view_set_surface_id.md).

 
 
 

#### Syntax:

view\_surface\_id\[0\...7]

 

#### Returns:

[Surface](../../Drawing/Surfaces/surface_create.md)

 

#### Extended Example:

In this extended example, we will create a surface and assign it to viewport\[0] so it captures the camera view assigned to that viewport, then draw that to the screen in the Draw GUI event. To start with we need to initialise our surface variable in the **Create Event** of a controller instance:

surf \= \-1;

We set the surface variable to \-1, as all surface functions should really be used in the **Draw** events to prevent odd errors or undefined behaviours. So, with that done, we would then have this in the main **Draw** event:

if !surface\_exists(surf)  

 {  

     surf \= surface\_create(camera\_get\_view\_width(view\_camera\[0]), camera\_get\_view\_height(view\_camera\[0]));  

     view\_surface\_id\[0] \= surf;  

 }

Surfaces are *volatile* meaning that they could be removed from memory at any time due to OS memory management and other things, so here we check to see if our surface exists and if it doesn't we create it and assign it to the view 0\. With that done, everything that would appear in view 0 will now be drawn to the surface we have created instead. If you do nothing else at this point, when you run your game you will simply get a blank screen as all drawing is being done on the surface, but the surface itself is not being drawn anywhere. Therefore we now need to draw the surface to the screen in the **Draw GUI** event like this:

if surface\_exists(surf)  

 {  

     draw\_surface\_stretched(surf, 0, 0, display\_get\_gui\_width(), display\_get\_gui\_height());  

 }

This code will now draw the surface that we have created from the view camera stretched to fill the entire GUI layer.
