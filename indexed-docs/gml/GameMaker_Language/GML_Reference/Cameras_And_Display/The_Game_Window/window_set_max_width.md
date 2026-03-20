# window\_set\_max\_width

This function can be used to set a maximum window width for your game. If you enable the window resize option in the Game Options for the target platform, then the player can resize the game window to any size they wish, however by using this function you can limit the maximum width to the size you specify. If you wish to go back to the default behaviour (ie: no minimum), then use a value of \-1\.

 
 

#### Syntax:

window\_set\_max\_width(width)

| Argument | Type | Description |
| --- | --- | --- |
| width | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The maximum width in pixels for the game window. |

 

#### Returns:

N/A

 

#### Example:

window\_set\_min\_width(640\);  

 window\_set\_min\_height(480\);  

 window\_set\_max\_width(1280\);  

 window\_set\_max\_height(960\);

The above code will set the minimum and maximum width and height for the game window.
