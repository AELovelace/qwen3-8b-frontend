# window\_get\_showborder

This function gets whether the game is shown in a borderless window or not.

It corresponds to the **Borderless Window** option in the Windows [Graphics](../../../../Settings/Game_Options/Windows.md#graphics) options; it gets the value of that checkbox *in\-game*.

 
 

#### Syntax:

window\_get\_showborder()

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_border\_shown \= window\_get\_showborder();

The above code gets whether the window border is shown and stores the result in a temporary variable \_border\_shown.
