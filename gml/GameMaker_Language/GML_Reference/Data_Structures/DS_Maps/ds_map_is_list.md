# ds\_map\_is\_list

With this function you can check to see if a [DS list](../DS_Lists/DS_Lists.md) is stored in the given map key. If the given key contains a DS list ID, then the function will return true otherwise it will return false.

  This will only detect lists that were added using the [ds\_map\_add\_list](ds_map_add_list.md) function.

 

#### Syntax:

ds\_map\_is\_list(id, key)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Map](ds_map_create.md) | The handle of the map to use. |
| key | [String](../../../GML_Overview/Data_Types.md) | The key to check. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var size \= ds\_map\_size(inventory);  

 var key \= ds\_map\_find\_first(inventory);  

 for (var i \= 0; i \< size; i\+\+)  

 {  

     if (ds\_map\_is\_list(inventory, key))  

     {  

         ds\_list\_destroy(inventory\[? key]);  

     }  

      

     key \= ds\_map\_find\_next(inventory);  

 }  

  

 ds\_map\_destroy(inventory);
 

The above code loops through a DS map and checks to see if any of the keys in it are for a DS list. If they are, then the DS list is destroyed, and the at the end of the loop the DS map is destroyed too.
