# layer\_depth

This function can be used to change the **depth** of the given layer, changing the order in which its contents will be rendered to the screen.

You supply the layer handle (which you get when you create the layer using [layer\_create](layer_create.md)) or the layer name (as a string \- this will have a performance impact) and then give the new depth to set it to (an integer value from \-16000 to 16000). The layer depth is defined as being higher when "further away" from the camera and lower when "closer" to the camera, so if you have three layers with depths \-100, 0, 100, the layers will draw in the order 100, 0, \-100, so that the "top" layer (i.e., the closest to the camera view and so drawn over everything else) will be the layer with the \-100 depth.

The following image shows a schematic of how depth works for layers:

Note that you can check the depth of a layer at any time using the function [layer\_get\_depth](layer_get_depth.md). Also note that the minimum and maximum layer depths are \-16000 to 16000, and anything outside of those depths **will not be rendered**. If you require a depth outside of that range then you will need to use the function [layer\_force\_draw\_depth](layer_force_draw_depth.md).

 
Keep in mind that modifying the depth of a layer may change which [Filters and Effects](../../../../../The_Asset_Editors/Room_Properties/Filters_and_Effects.md) are applied to it, as changing the depth to be lower than an FX layer's depth will no longer apply its effect on the layer.

 

#### Syntax:

layer\_depth(layer\_id, depth)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The handle of the layer to set the depth of (or the layer name as a string) |
| depth | [Real](../../../../GML_Overview/Data_Types.md) | The new depth for the layer |

 

#### Returns:

N/A

 

#### Example:

if (layer\_get\_depth(layer) !\= \-100\)  

 {  

     layer\_depth(layer, \-100\);  

 }

The above code gets the depth of the layer that the instance running the code is on, and if it is not \-100 then the depth is set to \-100\.
