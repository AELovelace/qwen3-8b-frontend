# application\_get\_position

This function returns the position of the application surface in an [array](../../../GML_Overview/Arrays.md) with four elements, where elements 0 and 1 are the (x, y) position of the top left\-hand corner of the surface, and elements 2 and 3 are the x and y of the bottom right\-hand corner of the surface, all relative to the size of the display or window.

When you have "maintain aspect ratio" ticked in the Game Options for a target platform, GameMaker will automatically set the draw position for the application surface so that it is displayed correctly centered and scaled on the given display. However, if you are manipulating this surface and wish to draw it yourself, then this function gives you an easy way to find exactly *where* within the display or window that the surface was being drawn so that you can then draw it there yourself, or align GUI images or post draw images to it.

 

#### Syntax:

application\_get\_position()

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md)

 

#### Example:

var \_pos \= application\_get\_position();  

 xx \= \_pos\[0];  

 yy \= \_pos\[1];  

 ww \= \_pos\[2] \- \_pos\[0];  

 hh \= \_pos\[3] \- \_pos\[1];

The above code will get the position of the application surface, as well as the absolute width and height in relation to the display window, and store them in four variables for future use.
