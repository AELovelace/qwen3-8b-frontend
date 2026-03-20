# gpu\_get\_zfunc

This function can be used to retrieve the z comparison mode, i.e. the comparison to use for [The Depth Test](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md#the_depth_test).

The value returned will be one of the following constants (the default value is cmpfunc\_lessequal):

 
 

#### Syntax:

gpu\_get\_zfunc()

 

#### Returns:

[Comparison Function Constant](gpu_get_zfunc.md) (see table above)

 

#### Example:

if (gpu\_get\_zfunc() !\= cmpfunc\_greater)  

 {  

     gpu\_set\_zfunc(cmpfunc\_greater);  

 }

The above code checks to see if the z\-testing method is set to cmpfunc\_greater and if not then it is set to that constant.
