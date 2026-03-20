# gpu\_set\_blendmode\_ext\_sepalpha

This function permits you to set the different component parts that should be factored together to create a custom blend mode, selecting different blend mode factors for the RGB components and the alpha component.

When GameMaker goes to draw a pixel there is a source colour (the colour of the pixel we're going to draw) and a destination colour (the colour that's already in the pixel we're drawing to), so when determining the new colour of the pixel, the source and destination colours are calculated according to the chosen blend mode.

Each component of the colours is stored as a floating point value between 0 and 1, and the new colour is calculated by multiplying each component of the source colour by some factor and by multiplying each component of destination colour by some other factor and then adding the results together component by component (or using a different [equation](gpu_set_blendequation.md)).

With this function you can set the different component parts that should be factored together to create a custom blend mode, selecting different blend mode factors for the RGB components and the alpha component. So the src and dest argument will use the first 3 blend mode values (RGB) and the alphasrc and alphadest arguments will take the last part of the blend mode factor. For example, if you have the RGB source as bm\_zero, then (0, 0, 0\) will be used. If you then set the Alpha source as bm\_one then (1\) will be used, giving a final source blend mode of (0, 0, 0, 1\).

The following chart shows the RGBA values for each blend mode, where (Rs, Gs, Bs, As) are considered the source values and (Rd, Gd, Bd, Ad) are the destination values. The eleven constants that are available for use can be either source or destination (or both) when used in this function.

 
  HTML5 without WebGL enabled will **not** be able to display following modes correctly:

- bm\_src\_colour
- bm\_inv\_src\_colour
- bm\_dest\_colour
- bm\_inv\_dest\_colour
- bm\_src\_alpha\_sat

 

Note that you can either supply four individual arguments to this function or you can supply an array of arguments (as returned by the function [gpu\_get\_blendmode\_ext\_sepalpha](gpu_get_blendmode_ext_sepalpha.md) for example). If supplying an array, it should have the following four elements:

- \[0] \= Source blend mode minus the alpha component (default is bm\_src\_alpha (As, As, As))
- \[1] \= Destination blend mode minus the alpha component (default is bm\_inv\_src\_alpha (1\-As, 1\-As, 1\-As))
- \[2] \= Source alpha component (default is bm\_src\_alpha (As))
- \[3] \= Destination alpha component (default is bm\_inv\_src\_alpha (1\-As))

To help you get the most from blend modes and to help understand how they work and how they affect the final image being drawn to the screen, we recommend that you read the following guide:

- [Guide To Using Blendmodes](../../../../Additional_Information/Guide_To_Using_Blendmodes.md)

 

#### Syntax:

gpu\_set\_blendmode\_ext\_sepalpha(src, dest, alphasrc, alphadest)

| Argument | Type | Description |
| --- | --- | --- |
| src | [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) | Source blend mode factor for RGB (see constants above) |
| dest | [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) | Destination blend mode factor for RGB (see constants above) |
| alphasrc | [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) | Source blend mode factor for Alpha (see constants above) |
| alphadest | [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) | Destination blend mode factor for Alpha (see constants above) |

 

#### Returns:

N/A

 

#### Example:

var \_bm \= gpu\_get\_blendmode\_ext\_sepalpha();  

 \_bm\[0] \= bm\_src\_alpha;  

 \_bm\[1] \= bm\_inv\_src\_alpha;  

 gpu\_set\_blendmode\_ext\_sepalpha(\_bm);

The above code creates a local array and gets the current extended blend mode with separate alpha values. This array is then manipulated and returned to set the blend mode.
