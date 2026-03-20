# gpu\_set\_stencil\_depth\_fail

This function sets the stencil operation that's executed when the stencil test passes but the depth test fails. You can use one of the following constants:

 
 

#### Syntax:

gpu\_set\_stencil\_depth\_fail(stencil\_op)

| Argument | Type | Description |
| --- | --- | --- |
| stencil\_op | [Stencil Op Constant](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md#stencil_op_constant) | A constant indicating the stencil operation to perform on pixels for which the stencil test passes but the depth test fails. |

 

#### Returns:

N/A

 

#### Example:

gpu\_set\_stencil\_depth\_fail(stencilop\_keep);

The code above sets the stencil operation to use when the stencil test passes but the depth test fails to stencilop\_keep, i.e. for every pixel for which this is the case the value in the stencil buffer remains unchanged.
