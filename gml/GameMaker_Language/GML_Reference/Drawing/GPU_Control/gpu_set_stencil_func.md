# gpu\_set\_stencil\_func

This function sets the comparison function to use for the stencil test.

The default is cmpfunc\_always, i.e. the stencil test always passes.

The stencil ref value is compared to the stencil value as follows: 

ref cmp\_func stencil

  The stencil ref value can be set with [gpu\_set\_stencil\_ref](gpu_set_stencil_ref.md).

 

#### Syntax:

gpu\_set\_stencil\_func(cmp\_func)

| Argument | Type | Description |
| --- | --- | --- |
| cmp\_func | [Comparison Function Constant](gpu_get_zfunc.md) | The comparison function to use for comparing the stencil reference value to the stencil value at the current pixel, i.e. ref cmp\_func stencil |

 

#### Returns:

N/A

 

#### Example:
