# Draw Gradient Ellipse

This action will draw an ellipse at a given position within the room, using a set of blend colours to create a gradient. You give the top left position and the bottom right position of the area that the ellipse is to "fit" into, and the ellipse will be drawn between them. The position can either be an absolute position within the room, or a position relative to the instance calling the action and you can set the colours to blend from the edge of the ellipse and from its center. The ellipse can be drawn filled or outlined by checking the **fill** box at the bottom.

  This action is only for use in the various [Draw Events](../../../The_Asset_Editors/Object_Properties/Draw_Events.md), and will not draw anything if used elsewhere.

 

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Left | The left position to start drawing from |
| Top | The top position to start drawing from |
| Right | The right position to end drawing from |
| Bottom | The bottom position to end drawing from |
| Center | The colour to blend from the center |
| Edge | The colour to blend from the edge |

 

#### Example:

The above action block code draws a gradient ellipse at the position of the instance of "obj\_Player".
