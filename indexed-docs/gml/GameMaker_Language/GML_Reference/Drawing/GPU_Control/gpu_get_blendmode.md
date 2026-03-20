# gpu\_get\_blendmode

This function can be used to retrieve the current blend mode being used for drawing. The returned value will be one of the following constants (the default value is bm\_normal):

 
 

#### Syntax:

gpu\_get\_blendmode()

 

#### Returns:

[Blend Mode Constant](gpu_get_blendmode.md) (see above for constants)

 

#### Example:

if (gpu\_get\_blendmode() !\= bm\_normal)  

 {  

     gpu\_set\_blendmode(bm\_normal);  

 }

The above code gets the current blend mode and if it is not bm\_normal it is set to that constant.
