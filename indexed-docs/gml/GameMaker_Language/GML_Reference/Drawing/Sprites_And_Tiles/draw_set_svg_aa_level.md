# draw\_set\_svg\_aa\_level

This function can be used to set the anti\-aliasing (AA) level for SVG format vector sprites. This can be a real value from 0 to 1 and will "smooth" the edges of these sprites. Note that to see this effect, you must first have enabled AA using the function [draw\_enable\_svg\_aa](draw_enable_svg_aa.md).

 

#### Syntax:

draw\_set\_svg\_aa\_level(AA)

| Argument | Type | Description |
| --- | --- | --- |
| AA | [Real](../../../GML_Overview/Data_Types.md) | The anti\-aliasing value to use from 0 to 1\. |

 

#### Returns:

N/A

 

#### Example:

if (draw\_get\_svg\_aa\_level() \=\= 0\)  

 {  

     draw\_enable\_svg\_aa(true);  

     draw\_set\_svg\_aa\_level(0\.5\);  

 }

The above code will check the AA value for SVG format sprites, and if it is 0 it enables AA and sets the value to 0\.5\.
