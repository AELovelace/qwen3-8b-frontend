# skeleton\_bone\_list

With this function you can populate a (pre\-created) [DS List](../../../../Data_Structures/DS_Lists/ds_list_create.md) with all the names of the bones used as part of the skeletal animation sprite. The names will be strings and can then be used in the other skeleton animation bone functions for these types of sprite.

 

#### Syntax:

skeleton\_bone\_list(sprite, list)

| Argument | Type | Description |
| --- | --- | --- |
| sprite | [Sprite Asset](../../../../../../The_Asset_Editors/Sprites.md) | The sprite index of the Spine skeletal animation to get the list from. |
| list | [DS List](../../../../Data_Structures/DS_Lists/ds_list_create.md) | The ID of the DS list to populate with the bone names. |

 

#### Returns:

N/A

 

#### Example:

bone\_list \= ds\_list\_create();  

 skeleton\_bone\_list(sprite\_index, bone\_list);

The above code creates a DS list then populates it with the bone names for later use.
