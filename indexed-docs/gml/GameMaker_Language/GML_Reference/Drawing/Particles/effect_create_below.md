# effect\_create\_below

This function creates a simple effect below all instances of your room (it is actually created at a depth of 50\).

 
The effect types ef\_rain and ef\_snow don't use the x/y position (although you must provide them). The size can be a value of 0, 1, or 2, where 0 is small, 1 is medium and 2 is large.

 

The available constants for the different particle kinds are: 

 
 

#### Syntax:

effect\_create\_below(kind, x, y, size, colour)

| Argument | Type | Description |
| --- | --- | --- |
| kind | [Effect Type Constant](GameMaker_Language/GML_Reference/Drawing/Particles/effect_create_above.md) | The kind of effect (use one of the constants listed above). |
| x | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x positioning of the effect if relevant. |
| y | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y positioning of the effect if relevant. |
| size | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The size of the effect. |
| colour | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the effect. |

 

#### Returns:

N/A

 

#### Example:

if (speed \> 0\)   

 {  

     effect\_create\_below(ef\_smoke, x, y, 0, c\_gray);  

 }

The above code will create a small puff of gray smoke every step that the instance speed is greater than 0 at the instance x,y coordinates.
