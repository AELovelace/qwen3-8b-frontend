# ds\_map\_find\_next

This function returns the next key stored in the DS map *after* the one specified in the function.

This can be useful if your have to iterate through the DS map looking for something, but should be avoided if possible as it can be slow. If no such key exists then the function will return undefined. You should always check this using the [is\_undefined](../../Variable_Functions/is_undefined.md) function.

 

#### Syntax:

ds\_map\_find\_next(id, key)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Map](ds_map_create.md) | The handle of the map to use |
| key | [String](../../../GML_Overview/Data_Types.md) | The key to find the next one to |

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_size \= ds\_map\_size(inventory);  

 var \_key \= ds\_map\_find\_first(inventory);  

 for (var i \= 0; i \< \_size; i\+\+)  

 {  

     if (\_key \=\= "gold")  

     {  

         break;  

     }  

       

     \_key \= ds\_map\_find\_next(inventory, \_key);  

 }

The above code creates some temporary variables and then gets the DS map size and finds the first key as stored by the computer in the map. It then uses a [for](../../../GML_Overview/Language_Features/for.md) loop to iterate through the DS map looking for the key value "gold". If it finds it, it breaks out of the loop.
