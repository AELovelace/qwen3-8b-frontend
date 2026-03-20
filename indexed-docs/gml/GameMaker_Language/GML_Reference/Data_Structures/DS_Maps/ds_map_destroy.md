# ds\_map\_destroy

This function destroys the given DS map, freeing the memory it is using.

DS maps take up space in memory, which is allocated to them when they are created. This means that you also need to free this memory when the DS map is not needed to prevent errors, memory leaks and loss of performance when running your game.

  Destroying a map will de\-reference any data structures stored in the map giving a memory leak, so you would need to go through the map and destroy all data structure items manually before destroying it to prevent this. The only time this is not required is when you have flagged any items in the map as a [DS list](../DS_Lists/DS_Lists.md) or as another [DS map](DS_Maps.md), in which case these items will be destroyed and their memory cleaned up automatically as well.

 
 

#### Syntax:

ds\_map\_destroy(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Map](ds_map_create.md) | The DS map to destroy |

 

#### Returns:

N/A

 

#### Example:

ds\_map\_destroy(inventory);  

 inventory \= \-1;

The above code will destroy the DS map referenced in the variable inventory.
