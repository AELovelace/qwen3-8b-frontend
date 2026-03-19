# gpu\_get\_sprite\_cull

This function returns whether (frustum) culling of sprites and tile maps is enabled or not. It is enabled by default.

 

#### Syntax:

gpu\_get\_sprite\_cull()

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_cull\_sprites \= gpu\_get\_sprite\_cull();

The above code calls gpu\_get\_sprite\_cull to retrieve whether sprites are currently culled against the view frustum when they're drawn. The value is stored in a temporary variable \_cull\_sprites.
