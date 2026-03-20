# gpu\_set\_stencil\_fail

This function sets the stencil operation to perform when the stencil test fails.

The default operation when the stencil test fails is stencilop\_keep. You can set it to one of the following:

 
 

#### Syntax:

gpu\_set\_stencil\_fail(stencil\_op)

| Argument | Type | Description |
| --- | --- | --- |
| stencil\_op | [Stencil Op Constant](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md#stencil_op_constant) | A constant indicating the stencil operation to perform on pixels for which the stencil test fails. |

 

#### Returns:

N/A

 

#### Example:

gpu\_set\_stencil\_fail(stencilop\_replace);

The above code sets the stencil operation to replace for pixels that fail the stencil test. This operation replaces the current value in the stencil buffer with the currently set stencil reference value (set earlier with [gpu\_set\_stencil\_ref](gpu_set_stencil_ref.md)).
