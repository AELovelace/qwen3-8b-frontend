# gpu\_get\_stencil\_depth\_fail

This function gets the stencil operation that's executed when the stencil test passes but the depth test fails.

 

#### Syntax:

gpu\_get\_stencil\_depth\_fail()

 

#### Returns:

[Stencil Op Constant](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md#stencil_op_constant)

 

#### Example:

var \_op\_stencil\_depth\_fail \= gpu\_get\_stencil\_depth\_fail();

The above code gets the stencil operation that's performed when the stencil test passes but the depth test fails.
