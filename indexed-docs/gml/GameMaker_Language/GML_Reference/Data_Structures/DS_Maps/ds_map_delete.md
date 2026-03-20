# ds\_map\_delete

With this function you can remove any given key (and its corresponding value) from the given, previously created, DS map .

 

#### Syntax:

ds\_map\_delete(id, key)

| Argument | Type | Description |
| --- | --- | --- |
| id | DS Map ID | The handle of the map to change. |
| key | String | The key to delete (along with its associated value). |

 

#### Returns:

N/A

 

#### Example:

ds\_map\_delete(inventory, "shield");

The above code will delete the key "shield" (and the value it is paired with) from the DS map (inventory).
