# surface\_get\_target

This function gets the surface that's currently set as the drawing target.

The function will return one of the following: 

- If the currently set surface was manually created using [surface\_create](surface_create.md), then that custom surface will be returned.
- If no custom surface is set, but the default application surface is still enabled, then the function will return the application surface.
- If no custom surface is set and the default application surface has also been disabled, then the function will return \-1.

 
 

#### Syntax:

surface\_get\_target()

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md) (\-1 if no target surface is set)

 

#### Example:

if (surface\_get\_target() !\= \-1\)  

 {  

     surface\_reset\_target();  

 }  

  

 draw\_surface(surf, 0, 0\);
 

The above code checks to see if the current render target is a surface or not, resetting the drawing target if it is. The surface stored in the variable surf is then drawn.
