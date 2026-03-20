# draw\_text\_transformed

This function will draw text in a similar way to [draw\_text()](draw_text.md) only now you can choose to scale the text along the horizontal or vertical axis (effectively stretching or shrinking it) and also have
 GameMaker draw it at an angle (where 0 is normal and every degree over 0 rotates the text anti\-clockwise).

 

#### Syntax:

draw\_text\_transformed(x, y, string, xscale, yscale, angle)

| Argument | Type | Description |
| --- | --- | --- |
| x |  | The x coordinate of the drawn string. |
| y |  | The y coordinate of the drawn string. |
| string |  | The string to draw. |
| xscale |  | The horizontal scale (default 1\). |
| yscale |  | The vertical scale(default 1\). |
| angle |  | The angle of the text. |

 

#### Returns:

 

#### Example:

draw\_set\_halign(fa\_center);  
 draw\_set\_valign(fa\_middle);
   
 image\_angle \+\= 1;  
 draw\_text\_transformed(room\_width / 2, room\_height / 2, "GAME OVER!", 2, 2, image\_angle);

The above code will draw the given text in the middle of the room, spinning round and scaled to twice its original size.
