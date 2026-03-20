# draw\_enable\_swf\_aa

With this function you can enable or disable anti\-aliasing (AA) for SWF format vector sprites. AA simply smooths the edges of vector images to give them a nicer look. The amount of AA used will depend on the value set using the function [draw\_set\_swf\_aa\_level](draw_set_swf_aa_level.md). By default this is disabled.

 

#### Syntax:

draw\_enable\_swf\_aa(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Enable (true) or disable (false) AA for all SWF sprites. |

 

#### Returns:

N/A

 

#### Example:

if (draw\_get\_swf\_aa\_level() \=\= 0\)  

 {  

     draw\_enable\_swf\_aa(true);  

     draw\_set\_swf\_aa\_level(0\.5\);  

 }

The above code will check the AA value for SWF format sprites, and if it is 0 it enables AA and sets the value to 0\.5\.
