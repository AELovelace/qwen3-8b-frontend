# draw\_getpixel

With this function you can get the colour value of any pixel that is being drawn to the current render target. This means that the results will depend on the event in which the function is called, and also on the target surface being used. Note that this will *not* return any alpha values, for that you should use [draw\_getpixel\_ext()](draw_getpixel_ext.md).

IMPORTANT This function will cause a huge performance hit and so should only be used when absolutely necessary.

 

#### Syntax:

draw\_getpixel(x, y)

| Argument | Type | Description |
| --- | --- | --- |
| x |  | The x coordinate of the pixel to check |
| y |  | The y coordinate of the pixel to check |

 

#### Returns:

Colour Constant

 

#### Example:

draw\_set\_colour(draw\_getpixel(500,200\));

The above code will set the drawing colour for all text, forms and primitives to the colour of the pixel at (500,200\) on the game screen.
