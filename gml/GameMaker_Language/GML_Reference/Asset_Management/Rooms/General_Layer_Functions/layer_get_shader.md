# layer\_get\_shader

This function can be used to check if the given layer has a shader assigned to it. You supply the layer handle (which you get when you create the layer using [layer\_create](layer_create.md)) or the layer name (as a string \- this will have a performance impact), and the function will return either the shader assigned, or an invalid shader handle (\-1\) if no shader is assigned.

 

#### Syntax:

layer\_get\_shader(layer\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The handle of the layer to target (or the layer name as a string) |

 

#### Returns:

[Shader Asset](../../../../../The_Asset_Editors/Shaders.md)

 

#### Example:

if (layer\_get\_shader(layer) \=\= \-1\)  

 {  

     layer\_shader(layer, shd\_sepia);  

 }

The above code will check to see if the layer that the instance running the code has a shader assigned to it and if it doesn't one is assigned.
