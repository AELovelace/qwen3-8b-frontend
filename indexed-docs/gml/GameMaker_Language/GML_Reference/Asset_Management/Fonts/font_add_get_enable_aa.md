# font\_add\_get\_enable\_aa

This function can be used to check whether anti\-aliasing (AA) is enabled for fonts added using [font\_add()](font_add.md). The function will return true if AA is enabled, and false if it is not. Note that AA is enabled by default, but you can change the AA state for added fonts using the function [font\_add\_enable\_aa()](font_add_enable_aa.md), as long as it is called *before* adding the font.

 

#### Syntax:

font\_add\_get\_enable\_aa()

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (!font\_add\_get\_enable\_aa())   

 {  

     font\_add\_enable\_aa(true);  

 }

The above code checks the status of anti\-aliasing for added fonts and if it not enabled, then we enable it.
