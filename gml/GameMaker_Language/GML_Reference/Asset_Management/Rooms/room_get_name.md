# room\_get\_name

This function returns the name of the given room as a string.

Please note that this is *only* a string and cannot be used to reference the room directly \- for that you would need the *room index*. You can, however, use this string to get the *room index* using the returned string along with the function [asset\_get\_index()](../Assets_And_Tags/asset_get_index.md).

 

#### Syntax:

room\_get\_name(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to check the name of. |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_roomname \= room\_get\_name(room);  

  

 draw\_text(32, 32, \_roomname);
 

The above code gets the name of the current room and draws it on the screen.
