# gpu\_get\_stencil\_func

This function gets the comparison function currently used for comparisons in the stencil buffer.

 

#### Syntax:

gpu\_get\_stencil\_func()

 

#### Returns:

[Comparison Function Constant](gpu_get_zfunc.md)

 

#### Example:

var \_func \= gpu\_get\_stencil\_func();

The above code calls gpu\_get\_stencil\_func to get the stencil function that's currently used and stores the result in a temporary variable \_func.
