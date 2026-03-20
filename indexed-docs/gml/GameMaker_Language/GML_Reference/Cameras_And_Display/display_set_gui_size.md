# display\_set\_gui\_size

This function sets the size of the GUI layer, where the contents of the [Draw GUI Event](../../../The_Asset_Editors/Object_Properties/Draw_Events.md) and any [UI layers](../../../The_Asset_Editors/Room_Properties/UI_Layers.md) are drawn. The GUI layer is stretched to fit the size of the game window no matter the resolution.

You can reset the GUI size at any time to the default configuration by calling this function using \-1 as both the width and height \- which will reset them to be 1:1 with the game window.

This function will override the GUI scale and offset set by [display\_set\_gui\_maximise](display_set_gui_maximise.md).

 

#### Syntax:

display\_set\_gui\_size(width, height)

| Argument | Type | Description |
| --- | --- | --- |
| width | [Real](../../GML_Overview/Data_Types.md) | The width of the GUI |
| height | [Real](../../GML_Overview/Data_Types.md) | The height of the GUI |

 

#### Returns:

N/A

 

#### Example:

display\_set\_gui\_size(768, 1024\);

The above code will lock the GUI layer to the given width and height, scaling all components to fit the game window using that proportion.
