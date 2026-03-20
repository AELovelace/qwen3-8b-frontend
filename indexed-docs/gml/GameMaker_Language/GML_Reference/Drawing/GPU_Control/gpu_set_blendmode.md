# gpu\_set\_blendmode

This function permits you to set the blend mode to one of the basic blend modes in GameMaker.

When GameMaker goes to draw a pixel there is a source colour (the colour of the pixel we're going to draw) and a destination colour (the colour that's already in the pixel we're drawing to), so when determining the new colour of the pixel, the source and destination colours are calculated according to the chosen blend mode.

Each component of the colours is stored as a floating point value between 0 and 1, and the new colour is calculated by multiplying each component of the source colour by some factor and by multiplying each component of destination colour by some other factor and then adding the results together component by component. The source and destination can also be mixed differently depending on the selected [equation](gpu_set_blendequation.md).

The blend mode can be set to one of the following constants:

 
As you can see from the above table, these blend modes are really composites of *extended* blend modes which can be found on the page describing [gpu\_set\_blendmode\_ext](gpu_set_blendmode_ext.md). Some of them also make use of a different [blend equation](gpu_set_blendequation.md).

To help you get the most from blend modes and to help understand how they work and how they affect the final image being drawn to the screen, we recommend that you read the following guide:

- [Guide To Using Blendmodes](../../../../Additional_Information/Guide_To_Using_Blendmodes.md)

 

#### Syntax:

gpu\_set\_blendmode(mode)

| Argument | Type | Description |
| --- | --- | --- |
| mode | [Blend Mode Constant](gpu_get_blendmode.md) | The blend mode to use (see the table above) |

 

#### Returns:

N/A

 

#### Example:

gpu\_set\_blendmode(bm\_add);  

 draw\_circle\_colour(100, 100, 50, c\_white, c\_black, 0\);  

 gpu\_set\_blendmode(bm\_normal);

This will turn the black into transparency, creating a 'glow' effect from the white being strong on the outside and gradually weakening further from the circle centre. The blend mode is reset after the circle is drawn to ensure additive blending is not also applied to everything else after it.
