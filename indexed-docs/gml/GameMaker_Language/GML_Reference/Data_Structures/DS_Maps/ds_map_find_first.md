# ds\_map\_find\_first

This function returns the first key stored in the given DS map. **This is not the first key in the order you added them!** DS maps are not stored in a linear form, for that use [DS list](../DS_Lists/DS_Lists.md), so all this does is find the first key as stored by the computer. This can be useful if your have to iterate through the DS map looking for something, but should be avoided if possible as it can be slow.

Note that this function will return undefined if the given DS map is empty.

 

#### Syntax:

ds\_map\_find\_first(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Map](ds_map_create.md) | The handle of the map to use. |

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:

var size \= ds\_map\_size(inventory) ;  

 var key \= ds\_map\_find\_first(inventory);  

 for (var i \= 0; i \< size; i\+\+)  

 {  

     if (key !\= "gold")  

     {  

         key \= ds\_map\_find\_next(inventory, key);  

     }  

     else break;  

 }

The above code creates some temporary variables and then gets the DS map size and finds the first key as stored by the computer in the map. It then uses a for loop to iterate through the DS map looking for the key value "gold". If it finds it, it breaks out the loop.
