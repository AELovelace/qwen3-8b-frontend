# view\_xport

With this built\-in array you can get or set the x position of the given viewport. The viewport is the area on the screen where the view is drawn, and you can have up to 8 active at any one time (the array is values from 0 to 7 inclusive to give 8 ports). Now, the default for GameMaker is that the game window (or background canvas) is the same size as the room, however when you activate viewports and cameras, this behaviour changes and the *total size of the bounding box for all viewports* is used. So, if you have two different viewports at two different positions, the total area that they cover defines the size of the game window. The following image illustrates this:

If you only have *one* viewport setting the x or y value of the viewport can have some interesting effects but is not normally practical (see the image below) and so it is better to maintain the x and y position as (0, 0\).

#### Syntax:

view\_xport\[0 .. 7]

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

view\_xport\[0] \= 0;  

 view\_yport\[0] \= 0;

The above code resets the position of viewport\[0] to the (0, 0\) position (top left hand corner) of the display.
