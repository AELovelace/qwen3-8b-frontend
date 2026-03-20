# Keyboard Input

When dealing with the keyboard in GameMaker you have a variety of functions that can be used to recognise different keyboard states like pressed or released. There are also some that store all the key presses as a string or that can tell you what the last key pressed was, as well as others that allow you to clear the keyboard state completely.

Each input character from a key (or multiple keys) is defined by its [UTF\-8](https://en.wikipedia.org/wiki/UTF-8) code, which is a numerical value. This value can be retrieved for any character using the [ord](../../Strings/ord.md) function but, GameMaker also has a series of constants for the most used keyboard special keys and a special functions. Typically you'd use a combination of [ord](../../Strings/ord.md) with the keyboard\_check\* functions, something like this:

if (keyboard\_check(ord("A")))  

 {  

     hspeed \= \-5;  

 }

So, the above will check the "A" key and if it's being pressed then it'll set the horizontal speed of the object to \-5\. Note, that using [ord](../../Strings/ord.md) with [keyboard\_check](keyboard_check.md)\*() functions will only function correctly if the input string is only one character in length and is a number from 0 to 9 or a *capitalised* Roman character from A to Z. The function [ord](../../Strings/ord.md) will return a full UTF\-8 value, but the keyboard\_check\* functions will *only detect A \- Z and 0 \- 9*.

But what if you want to use the arrow keys? Or if you want to modify an action using the "Shift" key? Well, for that GameMaker has a series of vk\_\* constants (vk\_ stands for *virtual key*) that you can use in place of [ord](../../Strings/ord.md):

Virtual Key Constant (vk\_\*)

| Constant | Description |
| --- | --- |
| vk\_nokey | keycode representing that no key is pressed |
| vk\_anykey | keycode representing that any key is pressed |
| vk\_left | keycode for the left arrow key |
| vk\_right | keycode for the right arrow key |
| vk\_up | keycode for the up arrow key |
| vk\_down | keycode for the down arrow key |
| vk\_enter | enter key |
| vk\_escape | escape key |
| vk\_space | space key |
| vk\_shift | either of the shift keys |
| vk\_control | either of the control keys |
| vk\_alt | alt key |
| vk\_backspace | backspace key |
| vk\_tab | tab key |
| vk\_home | home key |
| vk\_end | end key |
| vk\_delete | delete key |
| vk\_insert | insert key |
| vk\_pageup | pageup key |
| vk\_pagedown | pagedown key |
| vk\_pause | pause/break key |
| vk\_printscreen | printscreen/sysrq key |
| vk\_f1 ... vk\_f12 | keycode for the function keys F1 to F12 |
| vk\_numpad0 ... vk\_numpad9 | number keys on the numeric keypad |
| vk\_multiply | multiply key on the numeric keypad |
| vk\_divide | divide key on the numeric keypad |
| vk\_add | add key on the numeric keypad |
| vk\_subtract | subtract key on the numeric keypad |
| vk\_decimal | decimal dot keys on the numeric keypad |
| vk\_lshift | left shift key |
| vk\_lcontrol | left control key |
| vk\_lalt | left alt key |
| vk\_rshift | right shift key |
| vk\_rcontrol | right control key |
| vk\_ralt | right alt key |

The following is a small example of how to use the vk\_\* constants:

if (keyboard\_check\_pressed(vk\_tab))  

 {  

     instance\_create\_layer(x, y, "Controllers", obj\_Menu);  

 }

The above code will detect if the "Tab" key is *pressed* and create an instance of object obj\_Menu if it is.

If you need to check for a key character that is not 0 \- 9, A \- Z or one of the vk\_\* constants, then you should be checking one of the keyboard\_\* variables, like [keyboard\_lastchar](keyboard_lastchar.md) for example:

if (keyboard\_lastchar \=\= "ç")  

 {  

     show\_debug\_message("ç key pressed");  

     keyboard\_lastchar \= "";  

 }

## Function Reference

### General

  These functions will *not* work when using an on\-screen [Virtual Keyboard](../Virtual_Keys_And_Keyboards/Virtual_Keys_And_Keyboards.md).

- [io\_clear](io_clear.md)
- [keyboard\_check](keyboard_check.md)
- [keyboard\_check\_pressed](keyboard_check_pressed.md)
- [keyboard\_check\_released](keyboard_check_released.md)
- [keyboard\_check\_direct](keyboard_check_direct.md)
- [keyboard\_clear](keyboard_clear.md)
- [keyboard\_set\_map](keyboard_set_map.md)
- [keyboard\_get\_map](keyboard_get_map.md)
- [keyboard\_unset\_map](keyboard_unset_map.md)
- [keyboard\_set\_numlock](keyboard_set_numlock.md)
- [keyboard\_get\_numlock](keyboard_get_numlock.md)

### Simulating Keypresses

- [keyboard\_key\_press](keyboard_key_press.md)
- [keyboard\_key\_release](keyboard_key_release.md)

### Keyboard State \& Input

  When using the [Virtual Keyboard](../Virtual_Keys_And_Keyboards/Virtual_Keys_And_Keyboards.md), *only* the [keyboard\_string](keyboard_string.md) variable will be updated with the keyboard input.

- [keyboard\_key](keyboard_key.md)
- [keyboard\_lastkey](keyboard_lastkey.md)
- [keyboard\_lastchar](keyboard_lastchar.md)
- [keyboard\_string](keyboard_string.md)
