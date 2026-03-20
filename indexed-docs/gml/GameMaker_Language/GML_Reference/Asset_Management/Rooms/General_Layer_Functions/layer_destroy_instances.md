# layer\_destroy\_instances

This function can be used to destroy all the instances assigned to the given layer.

You supply the layer handle (which you get when you create the layer using [layer\_create()](layer_create.md)) or the layer name (as a string \- this will have a performance impact), and then all instances that are on the layer will be removed from the game, triggering their **Destroy** and **Clean Up** events.

 

#### Syntax:

layer\_destroy\_instances(layer\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The handle of the layer (or the layer name as a string) |

 

#### Returns:

N/A

 

#### Example:

if (global.game\_over)  

 {  

     layer\_destroy\_instances(layer);  

 }

The above code will check a global variable and if it's true then all instances that are on the layer of the calling instance will be destroyed (including the calling instance).
