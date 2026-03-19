# ds\_map\_find\_previous

This function returns the previous key stored in the DS map *before* the one specified in the function.

This can be useful if your have to iterate through the DS map looking for something, but should be avoided if possible as it can be slow. If no such key exists then the function will return undefined. You should always check this using the [is\_undefined](../../Variable_Functions/is_undefined.md) function.

 

#### Syntax:

ds\_map\_find\_previous(id, key)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Map](ds_map_create.md) | The handle of the map to use |
| key | [String](../../../GML_Overview/Data_Types.md) | The key to find the previous one to |

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_size \= ds\_map\_size(inventory) \- 1;  

 var \_key \= ds\_map\_find\_last(inventory);  

 for (var i \= \_size; i \> 0; i\-\-)  

 {  

     if (\_key !\= "gold")  

     {  

         \_key \= ds\_map\_find\_previous(inventory, \_key);  

     }  

     else break;  

 }

The above code creates some temporary variables and then gets the DS map size and finds the last key as stored by the computer in the map. It then uses a [for](../../../GML_Overview/Language_Features/for.md) loop to iterate back through the DS map looking for the key value "gold". If it finds it, it breaks out the loop.
