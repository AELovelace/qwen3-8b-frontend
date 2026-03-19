# gpu\_get\_texfilter

With this function you can check to see whether texture filtering (linear interpolation) is enabled (returns true) or not (returns false). For more information on texture filtering, see the function [gpu\_set\_texfilter()](gpu_set_texfilter.md).

**NOTE**: On the HTML5 target, this function will only work with WebGL enabled.

 

#### Syntax:

gpu\_get\_texfilter()

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (gpu\_get\_texfilter())   

 {  

     gpu\_set\_texfilter(false);  

 }  

 else  

 {  

     gpu\_set\_texfilter(true);  

 }

The above code checks to see if texture filtering is on or off and switches it accordingly.
