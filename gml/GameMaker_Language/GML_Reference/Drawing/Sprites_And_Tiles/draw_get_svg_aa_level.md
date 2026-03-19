# draw\_get\_svg\_aa\_level

This function can be used to get the anti\-aliasing (AA) level for SVG format vector sprites. The return value will between 0 and 1 and shows how "smooth" the edges of these sprites will be drawn. You can set the AA level using the function [draw\_set\_svg\_aa\_level](draw_set_svg_aa_level.md).

 

#### Syntax:

draw\_get\_svg\_aa\_level()

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (draw\_get\_svg\_aa\_level() \=\= 0\)  

 {  

     draw\_enable\_svg\_aa(true);  

     draw\_set\_svg\_aa\_level(0\.5\);  

 }

The above code will check the AA value for SVG format sprites, and if it is 0 it enables AA and sets the value to 0\.5\.
