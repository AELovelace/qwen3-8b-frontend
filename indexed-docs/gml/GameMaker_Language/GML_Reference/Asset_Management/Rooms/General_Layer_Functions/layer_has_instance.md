# layer\_has\_instance

This function can be used to check if a given instance is currently assigned to the given layer. You supply the layer handle (which you get when you create the layer using [layer\_create()](layer_create.md)) or the layer name (as a string \- this will have a performance impact) and the instance ID of the instance to check for. You can also give an object\_index (ie: the name of the object in the Asset Browser) and the function will check if any instances of that object are on the given layer. The function will return true if the instance is on the layer and false if it is not.

 

#### Syntax:

layer\_has\_instance(layer\_id, instance\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The handle of the layer to target (or the layer name as a string) |
| instance\_id | [Object Instance](../../Instances/Instance_Variables/id.md) | The unique instance ID or the object index of the instance to check for |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!layer\_has\_instance(global.Bullet\_Layer, obj\_Bullet\_Parent))  

 {  

     layer\_destroy(global.Bullet\_Layer);  

 }

The above code will check to see if the given layer contains any instances of the object "obj\_Bullet\_Parent" and if not it will destroy the layer.
