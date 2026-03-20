# gpu\_set\_stencil\_enable

This function enables or disables the stencil test.

The stencil test is a test performed on every pixel that's affected by the current draw command. It compares the stencil reference value set with [gpu\_set\_stencil\_ref](gpu_set_stencil_ref.md) to the value in the stencil buffer at that pixel, using the comparison set with [gpu\_set\_stencil\_func](gpu_set_stencil_func.md): 

ref cmp\_func stencil

Depending on the result of the comparison, the stencil test either passes or fails. The operation to perform when it passes is set with [gpu\_set\_stencil\_pass](gpu_set_stencil_pass.md), the one to perform when it fails with [gpu\_set\_stencil\_fail](gpu_set_stencil_fail.md). The operation can be to keep the current stencil value (stencilop\_keep, the default both on pass and on fail), to replace it (stencilop\_replace) or to apply a mathematical operation on it (set to 0, increment/decrement, invert bitwise).

See [The Depth And Stencil Buffer](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md) for detailed information.

 

#### Syntax:

gpu\_set\_stencil\_enable(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to enable the stencil test for subsequent draw commands |

 

#### Returns:

N/A

 

#### Example:
