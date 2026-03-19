# gpu\_get\_blendmode\_destalpha

This function can be used to retrieve the current *destination* extended blend mode alpha factor. The value returned will be one of the following constants ("s" denotes a value taken from the source while a "d" denotes a value from the destination) with only the "A" component being used when drawing:

 
 

#### Syntax:

gpu\_get\_blendmode\_destalpha()

 

#### Returns:

[Blend Mode Factor Constant](gpu_get_blendmode_ext.md) (see above table)

 

#### Example:

var bm;  

 bm\[0] \= gpu\_get\_blendmode\_srcalpha();  

 bm\[1] \= gpu\_get\_blendmode\_destalpha();  

 gpu\_set\_blendmode\_ext\_sepalpha(bm\_inv\_src\_alpha, bm\_inv\_dest\_colour, bm\[0], bm\[1]);

The above code creates a local array and gets the current source and destination blending factors for the alpha component. This array is then used to manipulate the RGB component of the blending factors.
