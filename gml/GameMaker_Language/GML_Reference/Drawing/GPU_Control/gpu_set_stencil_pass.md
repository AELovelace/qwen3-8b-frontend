# gpu\_set\_stencil\_pass

This function sets the stencil operation to perform when the stencil test passes.

The default operation when the stencil test passes is stencilop\_keep. You can change it to one of the following:

 
 

#### Syntax:

gpu\_set\_stencil\_pass(stencil\_op)

| Argument | Type | Description |
| --- | --- | --- |
| stencil\_op | [Stencil Op Constant](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md#stencil_op_constant) | A constant indicating the stencil operation to perform on pixels for which the stencil test passes. |

 

#### Returns:

N/A

 

#### Example:

gpu\_set\_stencil\_pass(stencilop\_incr\_wrap);

The above code sets the stencil operation to the [Stencil Op Constant](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md#stencil_op_constant) stencilop\_incr\_wrap, i.e. increment the stencil value for the pixel at every pass of the stencil test and wrap from the maximum value of 255 to 0 when it is reached.
