# ds\_map\_copy

You can use this function to copy the contents of one map (source) into another one (destination) that you have previously created using [ds\_map\_create()](ds_map_create.md). If the destination map is not empty, then this function will clear it first before copying. The source DS map remains unchanged by this process.

 

#### Syntax:

ds\_map\_copy(destination, source)

| Argument | Type | Description |
| --- | --- | --- |
| destination | [DS Map](ds_map_create.md) | The handle of the map you are copying **to** |
| source | [DS Map](ds_map_create.md) | The handle of the map you are copying **from** |

 

#### Returns:

N/A

 

#### Example:

inventory\_2 \= ds\_map\_create();  

 ds\_map\_copy(inventory\_2, inventory\_1\);

The above code will create a new map and assign it to the variable "inventory\_2". It will then copy the contents of the DS map indexed in the variable "inventory\_1" to this new map.
