# gpu\_set\_stencil\_read\_mask

This function sets the stencil read mask.

 
 

#### Syntax:

gpu\_set\_stencil\_read\_mask(mask)

| Argument | Type | Description |
| --- | --- | --- |
| mask | [Real](../../../GML_Overview/Data_Types.md) | The bitmask to use, a value in the range \[0, 255], or, \[0x00, 0xFF]. |

 

#### Returns:

N/A

 

#### Example:

gpu\_set\_stencil\_read\_mask(0b11111111\);

The code above sets the stencil read mask to all ones by passing the binary literal 0b11111111 as the parameter to the function.
