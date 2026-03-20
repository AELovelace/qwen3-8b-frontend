# gpu\_get\_blendmode\_src

This function can be used to retrieve the current *source* extended blend mode factor being used for drawing. The value returned will be one of the following constants ("s" denotes a value taken from the source while a "d" denotes a value from the destination):

 
s

 

#### Syntax:

gpu\_get\_blendmode\_src()

 

#### Returns:

[Blend Mode Factor Constant](gpu_get_blendmode_ext.md) (see above table)

 

#### Example:

var bm;  

 bm\[0] \= gpu\_get\_blendmode\_src();  

 bm\[1] \= gpu\_get\_blendmode\_dest();  

 gpu\_set\_blendmode\_ext\_sepalpha(bm\[0], bm\[1], bm\_inv\_src\_alpha, bm\_inv\_dest\_colour);

The above code creates a local array and gets the current source and destination blending factors. This array is then used to manipulate the alpha component of the blending factors.
