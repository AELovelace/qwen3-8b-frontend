# layer\_get\_visible

With this function you can check whether a layer is visible or not. You supply the layer handle (which you get when you create the layer using [layer\_create()](layer_create.md)) or the layer name (as a string \- this will have a performance impact) and the function will return true if it is visible, and false otherwise.

 

#### Syntax:

layer\_get\_visible(layer\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The handle of the layer to target (or the layer name as a string) |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var lay\_id \= layer\_get\_id("Instances");  

 if (layer\_get\_visible(lay\_id))  

 {  

     layer\_set\_visible(lay\_id, false);  

 }  

 else  

 {  

     layer\_set\_visible(lay\_id, true);  

 }

The above code gets the handle for the layer named "Instances" in the room editor, then uses the ID to check if the layer is visible or not, toggling the layer visibility depending on the returned value.
