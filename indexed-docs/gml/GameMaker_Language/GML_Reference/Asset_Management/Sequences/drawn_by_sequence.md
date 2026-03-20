# drawn\_by\_sequence

This is a **built\-in variable** that is part of the [Built\-In Instance Variables](../Instances/Instance_Variables/Instance_Variables.md) created for every object instance in your game. It returns true if the instance is drawn by a sequence, or false if the instance draws itself.

If this variable is set to true, the instance isn't drawn where it normally would in the draw order but is drawn as part of a sequence, which sorts the instance correctly with other elements of that sequence.

You can also change this variable to control whether the drawing is done by the sequence or the instance itself.

 

#### Syntax:

drawn\_by\_sequence

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

Draw Event

draw\_self();  

 if (drawn\_by\_sequence)  

 {  

     draw\_circle\_colour(x, y, 3, c\_red, c\_red, false);  

 }

The code above shows a Draw event in which the current instance first draws itself using [draw\_self](../../Drawing/Sprites_And_Tiles/draw_self.md). The instance additionally draws a red circle if it's drawn by a sequence, as indicated by its drawn\_by\_sequence variable.
