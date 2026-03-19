# ds\_list\_shuffle

With this function you can shuffle a list, which will re\-order all the component values into random positions from those in which they were originally added to the list.

 
 

#### Syntax:

ds\_list\_shuffle(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS List](ds_list_create.md) | The handle of the list to shuffle. |

 

#### Returns:

N/A

 

#### Example:

if (restart)  

 {  

     ds\_list\_shuffle(card\_list);  

 }

The above code will shuffle the list indexed in the variable "card\_list" if the variable "restart" is flagged as true.
