# effect\_create\_layer

This function creates a simple particle effect at the given layer.

You supply a layer name or ID, and a particle kind, along with its position, size and colour. The size takes three possible values: 0 (small), 1 (medium), or 2 (large).

  The effect types ef\_rain and ef\_snow don't use the x/y position (although you must still provide them).

The available constants for the different particle kinds are: 

 
 

#### Syntax:

effect\_create\_layer(layer\_id, kind, x, y, size, colour)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](GameMaker_Language/GML_Overview/Data_Types.md) or [Layer ID](GameMaker_Language/GML_Reference/Asset_Management/Rooms/General_Layer_Functions/layer_get_id.md) | The layer at which to create the effect |
| kind | [Effect Type Constant](GameMaker_Language/GML_Reference/Drawing/Particles/effect_create_above.md) | The kind of effect to create |
| x | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x position to create the effect at (unused by ef\_rain and ef\_snow) |
| y | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y position to create the effect at (unused by ef\_rain and ef\_snow) |
| size | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The size of the effect (0 \= small, 1 \= medium, 2 \= large) |
| colour | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the effect |

 

#### Returns:

N/A

 

#### Example 1:

effect\_create\_layer("Particles", ef\_spark, x, y, 1, c\_yellow);

The code above creates a medium\-sized yellow spark particle effect (ef\_spark) at the (x, y) position of the calling [instance](../../../../Quick_Start_Guide/Objects_And_Instances.md), on an existing layer named "Particles". This code can be placed in a Step event of an object to create a continuous trail of sparks.
