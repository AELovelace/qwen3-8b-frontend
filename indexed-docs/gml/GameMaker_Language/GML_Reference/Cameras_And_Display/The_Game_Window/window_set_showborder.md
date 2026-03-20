# window\_set\_showborder

This function sets whether the game is shown in a borderless window or not.

It corresponds to the **Borderless Window** option in the Windows [Graphics](../../../../Settings/Game_Options/Windows.md#graphics) options; it changes the value of that checkbox *in\-game*.

 
 

#### Syntax:

window\_set\_showborder(show)

| Argument | Type | Description |
| --- | --- | --- |
| show | [Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | Whether to show the window border |

 

#### Returns:

N/A

 

#### Example:

window\_set\_showborder(!window\_get\_showborder());

The above line of code toggles the window border.
