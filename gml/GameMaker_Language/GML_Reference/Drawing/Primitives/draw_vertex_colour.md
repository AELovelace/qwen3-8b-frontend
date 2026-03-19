# draw\_vertex\_colour

This function defines the position of a vertex for a primitive, with its own colour and alpha setting. The final look of the primitive will depend on the primitive type chosen to draw and the order with which you add the vertexes to it (see [draw\_primitive\_begin()](draw_primitive_begin.md) for more information) and the vertexes with different colours and alphas will blend smoothly from one to the other. To end and draw the primitive you must call [draw\_primitive\_end()](draw_primitive_end.md).

 

#### Syntax:

draw\_vertex\_colour(x, y, col, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| x |  | The x coordinate of the vertex. |
| y |  | The y coordinate of the vertex. |
| col |  | The colour to draw this vertex with. |
| alpha |  | The alpha to draw this vertex with (0\-1\). |

 

#### Returns:

 

#### Example:

draw\_primitive\_begin(pr\_trianglelist);  
 draw\_vertex\_colour(100, 100, c\_blue, 0\.1\);  
 draw\_vertex\_colour(100, 200, c\_red, 0\.1\);  
 draw\_vertex\_colour(150, 150, c\_green, 1\);  
 draw\_primitive\_end();
 

The above code will draw a semi\-transparent triangle with each vertex coloured a different colour.
