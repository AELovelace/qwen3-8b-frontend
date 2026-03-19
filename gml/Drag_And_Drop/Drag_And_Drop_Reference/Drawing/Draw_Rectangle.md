# Draw Rectangle

This action will draw a rectangle at a given position within the room. You give the top left position and the bottom right position and the rectangle will be drawn between them, and the position can either be an absolute position within the room, or a position relative to the instance calling the action. You can also set whether the rectangle can be filled or outlined by checking the **fill** box at the bottom.

 
 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Left | The left position to start drawing from |
| Top | The top position to start drawing from |
| Right | The right position to end drawing from |
| Bottom | The bottom position to end drawing from |

 

#### Example:

The above action block code draws two rectangles, one green and filled, and one yellow and outline only, at a position relative to the instance calling the actions.
