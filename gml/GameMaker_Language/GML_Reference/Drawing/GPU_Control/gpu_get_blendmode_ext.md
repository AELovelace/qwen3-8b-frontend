# gpu\_get\_blendmode\_ext

This function can be used to retrieve the current extended blend mode being used for drawing. The function returns a 2 element 1D array with the following elements in it:

- \[0] \= Source [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) (default is bm\_src\_alpha)
- \[1] \= Destination [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) (default is bm\_inv\_src\_alpha)

The values of the array will be one of the following constants ("s" denotes a value taken from the source while a "d" denotes a value from the destination):

 
Note that you can change these values and pass the full array to the [gpu\_set\_blendmode\_ext()](gpu_set_blendmode_ext.md) function as a single argument.

 

#### Syntax:

gpu\_get\_blendmode\_ext()

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md) (2 elements only; see above for constants)

 

#### Example:

var bm \= gpu\_get\_blendmode\_ext();  

 bm\[0] \= bm\_src\_alpha;  

 gpu\_set\_blendmode\_ext(bm);

The above code gets the current extended blend mode, modifies the source, and then sets the extended blend mode again.
