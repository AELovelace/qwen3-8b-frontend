# gpu\_set\_zfunc

This function sets the z\-buffer testing comparison mode (see [gpu\_set\_ztestenable](gpu_set_ztestenable.md) for more information).

The values available for use are any of the following constants (the default value is cmpfunc\_lessequal):

 
 

#### Syntax:

gpu\_set\_zfunc(cmp\_func)

| Argument | Type | Description |
| --- | --- | --- |
| cmp\_func | [Comparison Function Constant](gpu_get_zfunc.md) | The comparison mode to use (see list above) |

 

#### Returns:

N/A

 

#### Example:

gpu\_set\_ztestenable(true);  

 gpu\_set\_zfunc(cmpfunc\_always);  

 draw\_sprite(spr\_Background, 0, 0, 0\);  

 gpu\_set\_ztestenable(false);

The above code switches on z\-buffer testing and sets its comparison mode before drawing a background sprite and then switches it back off again to continue drawing.
