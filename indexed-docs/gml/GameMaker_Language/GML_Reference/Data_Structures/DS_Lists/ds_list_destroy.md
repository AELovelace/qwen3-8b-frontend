# ds\_list\_destroy

This function will remove the given list data structure from memory, freeing up the resources it was using and removing all values that it contained. This function should always be used when you are finished using the DS list to prevent memory leaks that can slow down and crash your game.

  Destroying a list will de\-reference any data structures stored in it giving a memory leak, so you would need to go through the list and destroy all data structure items manually before destroying it to prevent this. The only time this is not required is when you have flagged any items in the list as another [DS list](DS_Lists.md) or as a [DS map](../DS_Maps/DS_Maps.md), in which case these items will be destroyed and their memory cleaned up automatically as well.

 
 

#### Syntax:

ds\_list\_destroy(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS List](ds_list_create.md) | The DS list to destroy |

 

#### Returns:

N/A

 

#### Example:

if (lives \=\= 0\)  

 {  

     ds\_list\_destroy(AI\_list);  

     AI\_list \= \-1;  

     room\_goto(rm\_Menu);  

 }

The above code will check the value of the built\-in global variable [lives](../../../GML_Overview/Variables/Builtin_Global_Variables/lives.md) and if it is 0, it destroys the DS list indexed in the variable AI\_list and then changes rooms.
