# Defining Inputs

Input is managed by the Rollback system, so it can properly be synchronised between players. Inputs for a player can be retrieved using [rollback\_get\_input()](Rollback_Functions/rollback_get_input.md), which returns a struct containing the inputs for the player.

## Default Inputs

By default you will get the following keys in the input struct:

**left**, **right**, **up**, **down**, **Z**, **X**, **C**, **space**

The directional inputs are mapped to the arrow keys.

## Input Variants

Each keyboard input defined is read using [keyboard\_check()](../Game_Input/Keyboard_Input/keyboard_check.md), which gets if the key is held or not. For mouse input it uses [mouse\_check\_button()](../Game_Input/Mouse_Input/mouse_check_button.md).

With each defined input (default or custom), you also get variants that use [keyboard\_check\_pressed()](../Game_Input/Keyboard_Input/keyboard_check_pressed.md) and [keyboard\_check\_released()](../Game_Input/Keyboard_Input/keyboard_check_released.md) (and the equivalent functions for mouse input). These are added with the suffix "**\_pressed**" and "**\_released**" respectively.

For example, for the space input, you will get space\_pressed and space\_released as well.

## Custom Controls

### Defining

To define your own inputs, create a struct containing the input keys and assigned constants to use, and then pass that into [rollback\_define\_input()](Rollback_Functions/rollback_define_player.md). This will override the default controls mentioned at the top of this page.

You define your input names on the left\-hand side (e.g. fire), and assign an input on the right\-hand side (e.g. mb\_left):

// Before starting rollback game  

 rollback\_define\_input({  

     fire: mb\_left,  

     interact: vk\_space,  

     left: ord("A"),  

     right: ord("D")  

 });

Calling [rollback\_get\_input()](Rollback_Functions/rollback_get_input.md) now will only return the inputs defined here (fire, interact, etc.), along with \*\_pressed and \*\_released variants for each of them.

For GML Visual, use [Define Input (Rollback)](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Define_Input.md).

### Constants

You can assign any of the following input values to the inputs in your struct:

| Input Type | Value | Description |
| --- | --- | --- |
| **Keyboard** | vk\_\* constants | Use these constants to define keyboard keys. A list of such constants is [given here](../Game_Input/Keyboard_Input/Keyboard_Input.md). |
| ord("") | Define a letter key by wrapping it in [ord()](../Strings/ord.md). |
| **Gamepad** | gp\_\* constants | Use these constants to define gamepad inputs (buttons and axes). A list of such constants is [given here](../Game_Input/GamePad_Input/Gamepad_Input.md). |
| **Mouse** | mb\_\* constants | Use these constants to define mouse buttons. A list of such constants is [given here](../Game_Input/Mouse_Input/Mouse_Input.md).  NOTE: mb\_any and mb\_none cannot be used. |
| m\_axisx | The X position of the mouse in the room (using [mouse\_x](../Game_Input/Mouse_Input/mouse_x.md)). |
| m\_axisy | The Y position of the mouse in the room (using [mouse\_y](../Game_Input/Device_Input/device_mouse_y.md)). |
| m\_axisx\_gui | The X position of the mouse on the GUI layer (using [device\_mouse\_x\_to\_gui()](../Game_Input/Device_Input/device_mouse_x_to_gui.md)). |
| m\_axisy\_gui | The Y position of the mouse on the GUI layer (using [device\_mouse\_y\_to\_gui()](../Game_Input/Device_Input/device_mouse_y_to_gui.md)). |
| m\_scroll\_up | 1 if the mouse wheel is being scrolled up, 0 otherwise |
| m\_scroll\_down | 1 if the mouse wheel is being scrolled down, 0 otherwise |

### Multiple Controls

You can assign multiple controls to each input, by listing input constants in an array:

rollback\_define\_input({  

     fire:     \[mb\_left, ord("X")],  

     interact: \[vk\_space, ord("C")],  

     left:     \[ord("A"), vk\_left],  

     right:    \[ord("D"), vk\_right]  

 });

In this example, fire will be triggered by both mb\_left and the X key, interact will be triggered by vk\_space and the C key, and so on.

var \_input \= rollback\_get\_input();  

 if (\_input.fire)  

 {  

     // Runs when LMB or X is pressed  

 }

NOTE You can't bind the same input constant to multiple inputs, e.g. a specific input value (say, mb\_left or ord("A")) can only be used **once** throughout your whole input struct.

## Mock Input

When testing locally, you may want to define temporary inputs for remote players so you can test multiplayer gameplay offline.

You can achieve that by defining mock input for a player using [rollback\_define\_mock\_input()](Rollback_Functions/rollback_define_mock_input.md). For example, after calling the code snippet above to define fire, interact, left and right inputs for all players, you can define a separate set of inputs for the second player specifically, which you can use during Sync Test.

rollback\_define\_mock\_input(1, {  

     fire: vk\_control,  

     interact: vk\_shift,  

     left: ord("J"),  

     right: ord("L")  

 });

This defines mock input for player 1 (the second player), keeping the same input names but assigning different inputs. This way two people could play the game locally on the same computer.

## Further Reading

Read the following pages for more information on the Rollback system:

- [Rollback Constraints](Rollback_Constraints.md)
- [Rollback Events](Rollback_Events.md)
- [Creating a Multiplayer Game](Creating_Multiplayer.md)
- [Rollback System](Rollback_System.md)
