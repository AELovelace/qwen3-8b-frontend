# ds\_list\_is\_list

With this function you can check to see if another DS list is stored at the given position within a DS list. If the given position contains a DS list ID, then the function will return true otherwise it will return false.

  This will only detect lists that were manually marked using the [ds\_list\_mark\_as\_list](ds_list_mark_as_list.md) function.

 

#### Syntax:

ds\_list\_is\_list(id, pos)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS List](ds_list_create.md) | The handle of the list to check. |
| pos | [Real](../../../GML_Overview/Data_Types.md) | The position within the list to check. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var size \= ds\_list\_size(ships);  

 for (var i \= 0; i \< size; i\+\+)  

 {  

     if (ds\_list\_is\_list(ships, i))  

     {  

         ds\_list\_destroy(ships\[\| i]);  

     }  

 }  

 ds\_list\_destroy(ships);

The above code loops through a DS list and checks to see if any of the entries contain other list IDs. If they do, then these lists are destroyed, and then the main list is destroyed after the loop is finished.
