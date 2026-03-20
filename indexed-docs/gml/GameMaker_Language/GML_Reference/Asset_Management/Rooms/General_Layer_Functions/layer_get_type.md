# layer\_get\_type

This function returns the type of the given layer. You supply either the name of the layer as a string or the [Layer](layer_get_id.md) handle, and the function returns one of the following constants:

| [Layer Type Constant](layer_get_type.md) | |
| --- | --- |
| Constant | Description |
| layer\_type\_unknown | An unknown layer. Returned for invalid layer names/handles. |
| layer\_type\_room | A room layer. |
| layer\_type\_ui\_viewports | A UI layer with "Game View" set to "Viewports". |
| layer\_type\_ui\_display | A UI layer with "Game View" set to "Display". |

 

#### Syntax:

layer\_get\_type(layer\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The handle of the layer to get the type of (or the layer name as a string) |

 

#### Returns:

[Layer Type Constant](layer_get_type.md)

 

#### Example:

if (layer\_get\_type(layer) \=\= layer\_type\_ui\_display)  

 {  

     layer\_set\_visible(layer, false);  

 }

This checks if the layer that the instance is on is a Display UI layer. In that case, it makes the layer invisible.
