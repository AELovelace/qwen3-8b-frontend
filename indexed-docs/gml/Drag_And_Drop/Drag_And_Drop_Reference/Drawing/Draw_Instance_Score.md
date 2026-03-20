# Draw Instance Score

With this action you can draw the score value of the instance. When you use *any* score action in GameMaker the instance that calls it will have a new instance scope variable called score added. This variable can then be checked and set as you would any other variable. In the case of this action, the variable will be drawn to the screen at the given position, along with any caption text that you wish to provide. Caption text will be drawn preceding the score value and if it is text it should be wrapped with "", and both will be formatted using the current draw font , colour and alignment.

  This action is only for use in the various [Draw Events](../../../The_Asset_Editors/Object_Properties/Draw_Events.md), and will not draw anything if used elsewhere.

 

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Caption | The string to draw along with the score value (preceding and can be left blank) |
| x | The x position to draw the score at |
| y | The y position to draw the score at |

 

#### Example:

The above action block code draws the score using the given draw formatting.
