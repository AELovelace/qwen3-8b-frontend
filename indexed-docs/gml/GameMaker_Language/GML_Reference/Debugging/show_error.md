# show\_error

This function will show a custom string as an error message.

IMPORTANT The second argument only exists for backwards compatibility with older projects and will have no effect on the error dialog shown.

**NOTE** This function is for debug use **only**.

 

#### Syntax:

show\_error(str, abort)

| Argument | Type | Description |
| --- | --- | --- |
| str | String | The string to show in the pop\-up message. |
| abort | Boolean | UNUSED Whether the error should abort the game (true) or allow the player to ignore it (false). |

 

#### Returns:

N/A

 

#### Example:

if (room !\= rm\_Dungeon)  

 {  

     show\_error("Error: Went to wrong area. Aborting game.", true);  

 }

The above code will check if the current room is rm\_Dungeon, and if it's not, it will show an error message.
