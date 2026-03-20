# layer\_enable\_fx

This function enables/disables the filter/effect assigned to a Room Layer. You specify either the ID or the name of the layer you want to modify, and then a boolean value telling whether the FX should be enabled (true) or disabled (false).

Passing in false will not remove the FX from the layer, but simply make it invisible. Use [layer\_clear\_fx()](layer_clear_fx.md) to remove an FX from a layer.

Similarly, passing in true will not do anything if there is no FX applied to the layer. Use [layer\_set\_fx()](layer_set_fx.md) to apply an FX to a layer.

 

#### Syntax:

layer\_enable\_fx(layer\_name\_or\_id, enable)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_name\_or\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The name or ID of the layer to modify |
| enable | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether to enable or disable the FX |

 

#### Returns:

N/A

 

#### Example:

if (hp \<\= 3\)  

 {  

     layer\_enable\_fx("DesaturateLayer", true);  

 }  

 else  

 {  

     layer\_enable\_fx("DesaturateLayer", false);  

 }

The above code enables a Desaturate FX layer if the instance's HP value is less than or equal to 3, otherwise it disables it. This indicates to the player that their HP is low, by desaturating the screen.
