# mouse\_y

This **read\-only** variable returns the current y axis position of the mouse within the room.

 
 

#### Syntax:

mouse\_y

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

y \= median(64, mouse\_y, room\_height \- 64\);

The above code will maintain the instance at the mouse y position as long as it is within the limits of 64 pixels from the top and bottom of the room.
