# room\_set\_view\_enabled

This function enables (true) or disables (false) views in any of the rooms within your game *except the current one*.

 

#### Syntax:

room\_set\_view\_enabled(index, val)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to set. |
| val | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to enable (true) or disable (false) views in the given room. |

 

#### Returns:

N/A

 

#### Example:

global.myroom \= room\_add();  

 room\_set\_view\_enabled(global.myroom, true);

This will enable views in the room indexed in global.myroom.
