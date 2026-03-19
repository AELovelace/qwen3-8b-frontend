# draw\_button

This function will draw a very simple, rectangular "button" using the currently selected draw colour and alpha where the *up* argument defines how the beveled edge effect looks, as shown in the image below:

 
 

#### Syntax:

draw\_button(x1, y1, x2, y2, up)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the left of the button |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the top of the button |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the right of the button |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the bottom of the button |
| up | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the button is up (true) or down (false) |

 

#### Returns:

N/A

 

#### Example:

draw\_button(100, 100, 200, 150, !mouse\_check\_button(mb\_left));

This will draw a button which will appear pressed if the left mouse button is held down.
