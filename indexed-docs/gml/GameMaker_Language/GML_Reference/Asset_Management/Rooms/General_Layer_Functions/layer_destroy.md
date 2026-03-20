# layer\_destroy

This function will destroy the given layer.

You supply the layer handle (which you get when you create the layer using [layer\_create()](layer_create.md)) or the layer name (as a string \- this will have a performance impact) and this will remove it from the current room. If the layer is one that has been designed in the room editor, then the next time you leave the room and then return, the layer will be recreated again with the original contents, however if the room is persistent, the layer will be removed unless room persistence is switched off again. When you destroy a layer in this way, all its contents will be removed too, so any reference IDs for backgrounds or tile maps, etc., will no longer be valid and any instances assigned to the layer will be destroyed (performing their **Destroy Event** at the same time, if they have one, as well as the **Clean Up Event**).

 

#### Syntax:

layer\_destroy(layer\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The handle of the layer to destroy (or the layer name as a string) |

 

#### Returns:

N/A

 

#### Example:

if (!instance\_exists(obj\_Bullet\_Parent))  

 {  

     layer\_destroy(global.Bullet\_Layer);  

 }

The above code will check to see if any instances of the object "obj\_Bullet\_Parent" exists, and if they don't it will destroy the layer with the ID stored in the global variable.
