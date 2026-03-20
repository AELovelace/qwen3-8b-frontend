# gpu\_get\_stencil\_read\_mask

This function gets the stencil read mask.

 
 

#### Syntax:

gpu\_get\_stencil\_read\_mask()

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_read\_mask \= gpu\_get\_stencil\_read\_mask();  

 \_read\_mask \|\= 0b11000000;  

 gpu\_set\_stencil\_read\_mask(\_read\_mask);

The above code gets the current stencil read mask with a call to gpu\_get\_stencil\_read\_mask and stores it in a temporary variable \_read\_mask. It then sets the highest two bits to 1 by binary OR\-ing the value with 0b11000000. Finally, the stencil read mask is set to the new value with [gpu\_set\_stencil\_read\_mask](gpu_set_stencil_read_mask.md). Note that the new mask value may be the same as the old value if the two highest bits were already set.
