# ds\_list\_copy

With this function you can copy the contents of one list (source) into another (destination). Both lists must have been created previously and if the destination list already has information within it, this list will be cleared first. The end result is two independent lists which contain the same information.

 

#### Syntax:

ds\_list\_copy(destination, source)

| Argument | Type | Description |
| --- | --- | --- |
| destination | [DS List](ds_list_create.md) | The handle of the list being copied *to*. |
| source | [DS List](ds_list_create.md) | The handle of the list to be copied *from*. |

 

#### Returns:

N/A

 

#### Example:

if (!ds\_list\_empty(main\_list))  

 {  

     old\_list \= ds\_list\_create();  

     ds\_list\_copy(old\_list, main\_list);  

     ds\_list\_clear(main\_list);  

 }

The above code will check a DS list to see if it is empty. If it is not empty it is copied into another DS list (which has been created previously) and then the original list is cleared.
