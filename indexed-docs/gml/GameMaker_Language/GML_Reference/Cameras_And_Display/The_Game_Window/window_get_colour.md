# window\_get\_colour

This function returns the background colour of the game window.

This colour represents that which will be used for those areas of the game window that are not occupied by any views. The following image illustrates this:

The above image has two views with two viewports, each one drawn at a different position. This stretches the game window to accommodate both ports and uses the window colour to colour the background where no view is shown.

 

#### Syntax:

window\_get\_colour()

 

#### Returns:

[Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md)

 

#### Example:

if (window\_get\_colour() !\= c\_black)  

 {  

     window\_set\_colour(c\_black);  

 }

The above code will check the window colour to see if it is set as black or not, and if it is not it sets it to black.
