# layer\_fx\_is\_enabled

This function returns whether the filter/effect for a layer is enabled.

You specify either the ID or the name of the layer you want to target, and the function returns a boolean value indicating whether the layer's FX is enabled (true) or disabled (false).

 

#### Syntax:

layer\_fx\_is\_enabled(layer\_name\_or\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_name\_or\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The name or ID of the layer to check |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

x \= xstart;  

 y \= ystart;  

 hp \= hp\_max;  

  

 if (layer\_fx\_is\_enabled("DesaturateLayer"))  

 {  

     layer\_enable\_fx("DesaturateLayer", false);  

 }
 

The above code "respawns" the instance, by moving it to its original position and refilling its HP. It then checks if the Desaturate FX layer is enabled, and if it is, disables it.
