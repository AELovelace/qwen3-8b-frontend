# gpu\_get\_blendequation

This function can be used to retrieve the current [blend equation](gpu_set_blendequation.md) being used for drawing. The returned value will be one of the following constants (the default value is bm\_eq\_add):

 
 

#### Syntax:

gpu\_get\_blendequation()

 

#### Returns:

[Blend Mode Equation Constant](gpu_set_blendequation.md) (see above for constants)

 

#### Example:

if (gpu\_get\_blendequation() !\= bm\_eq\_add)  

 {  

     gpu\_set\_blendequation(bm\_eq\_add);  

 }

The above code gets the current blend equation and if it is not bm\_eq\_add it is set to that constant.
