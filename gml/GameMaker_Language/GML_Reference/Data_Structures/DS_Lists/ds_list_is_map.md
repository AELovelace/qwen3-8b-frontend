# ds\_list\_is\_map

With this function you can check to see if a [DS map](../DS_Maps/DS_Maps.md) is stored at the given position within a DS list. If the given position contains a DS map ID, then the function will return true otherwise it will return false.

  This will only detect maps that were manually marked using the [ds\_list\_mark\_as\_map](ds_list_mark_as_map.md) function.

 

#### Syntax:

ds\_list\_is\_map(id, pos)

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

     if (ds\_list\_is\_map(ships, i))  

     {  

         ds\_map\_destroy(ships\[\| i]);  

     }  

 }  

 ds\_list\_destroy(ships);

The above code loops through a DS list and checks to see if any of the entries contain map IDs. If they do, then these maps are destroyed, and then the main list is destroyed after the loop is finished.
