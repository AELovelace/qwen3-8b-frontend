# draw\_get\_enable\_skeleton\_blendmodes

This function returns whether per\-slot blend modes for skeletal sprites are enabled (true) or disabled (false).

 

#### Syntax:

draw\_get\_enable\_skeleton\_blendmodes()

 

#### Returns:

[Boolean](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (!draw\_get\_enable\_skeleton\_blendmodes())  

 {  

     draw\_enable\_skeleton\_blendmodes(true);  

 }

The above code enables per\-slot blend modes for skeletal sprites, if they are disabled.
