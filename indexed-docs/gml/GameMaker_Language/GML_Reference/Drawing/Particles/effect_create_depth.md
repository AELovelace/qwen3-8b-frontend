# effect\_create\_depth

This function creates a simple particle effect at the given depth.

You supply a depth value and a particle kind, along with its position, size and colour. The size takes three possible values: 0 (small), 1 (medium), or 2 (large).

  The effect types ef\_rain and ef\_snow don't use the x/y position (although you must still provide them).

 
The available constants for the different particle kinds are: 

 
 

#### Syntax:

effect\_create\_depth(depth, kind, x, y, size, colour)

| Argument | Type | Description |
| --- | --- | --- |
| depth | [Real](../../../GML_Overview/Data_Types.md) | The depth at which to create the effect |
| kind | [Effect Type Constant](effect_create_above.md) | The kind of effect to create |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position to create the effect at (unused by ef\_rain and ef\_snow) |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position to create the effect at (unused by ef\_rain and ef\_snow) |
| size | [Real](../../../GML_Overview/Data_Types.md) | The size of the effect (0 \= small, 1 \= medium, 2 \= large) |
| colour | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the effect |

 

#### Returns:

N/A

 

#### Example:

effect\_create\_depth(depth, ef\_explosion, x, y, 2, c\_dkgray);

The code above creates a large, dark gray coloured explosion particle effect (ef\_explosion) at the [depth](../../Asset_Management/Instances/Instance_Variables/depth.md) and x, y position of the calling [instance](../../../../Quick_Start_Guide/Objects_And_Instances.md).
