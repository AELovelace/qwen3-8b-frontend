# virtual\_key\_add

This function adds a virtual key that covers a portion of the screen area, mapping "touches" of this area to a keyboard key.

This function enables you to map "touches" of a screen area to keyboard events. This means that once you have assigned an area to a virtual key, all touches on that area will trigger the keyboard event corresponding to the key you have mapped to the area. You can assign each virtual key you define to a variable too, which can then be used in the further virtual key functions to show, hide and delete them. These keys are assigned on a *per room* basis and will be automatically removed by GameMaker when changing rooms.

The actual position of the virtual key is based on the GUI layer rather than room position and so the x/y values use the GUI coordinates. This means that you don't need to worry about the use of views or the relative room coordinates, and can simply define the keys in the **Create Event** of an object (you only need to define a virtual key once per room), then draw your key sprites in the [Draw GUI Event](../../../../The_Asset_Editors/Object_Properties/Draw_Events.md).

 

#### Syntax

virtual\_key\_add(x, y, w, h, keycode)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate (left side) of the virtual key *on the screen* |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate (top side) of the virtual key *on the screen* |
| w | [Real](../../../GML_Overview/Data_Types.md) | The width of the virtual key |
| h | [Real](../../../GML_Overview/Data_Types.md) | The height of the virtual key |
| keycode | [Virtual Key Constant (vk\_\*)](../Keyboard_Input/Keyboard_Input.md) | Which keyboard key event should be triggered by touching this area |

 

#### Returns:

[Virtual Key ID](virtual_key_add.md)

 

#### Example:

global.left \= virtual\_key\_add(32, 32, 64, 64, vk\_left);

The above code creates a virtual key 64x64 pixels square, positioned on the screen at (32, 32\) which will trigger the vk\_left event when touched and assigns the index of this virtual key to a global variable.
