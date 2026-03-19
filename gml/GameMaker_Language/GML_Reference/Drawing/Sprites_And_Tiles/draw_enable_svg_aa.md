# draw\_enable\_svg\_aa

With this function you can enable or disable anti\-aliasing (AA) for SVG format vector sprites. AA simply smooths the edges of vector images to give them a nicer look. The amount of AA used will depend on the value set using the function [draw\_set\_svg\_aa\_level](draw_set_svg_aa_level.md). By default this is disabled.

 

#### Syntax:

draw\_enable\_svg\_aa(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Enable (true) or disable (false) AA for all SVG sprites. |

 

#### Returns:

N/A

 

#### Example:

if (draw\_get\_svg\_aa\_level() \=\= 0\)  

 {  

     draw\_enable\_svg\_aa(true);  

     draw\_set\_svg\_aa\_level(0\.5\);  

 }

The above code will check the AA value for SVG format sprites, and if it is 0 it enables AA and sets the value to 0\.5\.
