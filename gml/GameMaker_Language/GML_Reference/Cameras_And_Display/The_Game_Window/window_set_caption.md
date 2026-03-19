# window\_set\_caption

With this function you can change or set the windows caption for the room that you are currently in.

This caption appears at the top of the window, next to the game icon, when the game is not in full screen mode.

 

#### Syntax:

window\_set\_caption(caption)

| Argument | Type | Description |
| --- | --- | --- |
| caption | [String](../../../GML_Overview/Data_Types.md) | The new caption. |

 

#### Returns:

N/A

 

#### Example:

if (window\_get\_caption() !\= "")  

 {  

     window\_set\_caption("");  

 }

The above code will check the window's caption to see if it has text or not, and if it does, sets it to an empty string so that no caption is displayed.
