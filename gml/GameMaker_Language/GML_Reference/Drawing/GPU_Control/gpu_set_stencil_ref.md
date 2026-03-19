# gpu\_set\_stencil\_ref

This function sets the stencil test reference value used for draw functions.

The stencil ref value is compared to the stencil value as follows: 

ref cmp\_func stencil

  The comparison function can be set with [gpu\_set\_stencil\_func](gpu_set_stencil_func.md).

 

#### Syntax:

gpu\_set\_stencil\_ref(ref)

| Argument | Type | Description |
| --- | --- | --- |
| ref | [Real](../../../GML_Overview/Data_Types.md) | The stencil test reference value, clamped within range 0 to 255 (inclusive) |

 

#### Returns:

N/A

 

#### Example:
