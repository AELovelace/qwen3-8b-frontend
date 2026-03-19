# keyboard\_key\_press

With this function you can simulate the press of any key on the keyboard. When used, the key will be flagged as being pressed until the corresponding release function is called (see [keyboard\_key\_release()](keyboard_key_release.md)). The function will take a keycode value as returned by the function [ord()](../../Strings/ord.md) (only *capital* letters from A\-Z or numbers from 0\-9\), or any of the vk\_\* constants listed on the main [Keyboard Input](Keyboard_Input.md) page.

Note that after calling this function, if the key is *physically* pressed on the keyboard, this press event will *not* be registered again until the key has been physically released (triggering the release event and stopping this function), or the corresponding release key function has been called, and the key pressed again.

  On Windows, this will trigger the given key press outside of the game as well (e.g. when another window is in focus) if it is called repeatedly e.g. in a Step or Alarm event.

 

#### **Syntax:**

keyboard\_key\_press(key);

| Argument | Type | Description |
| --- | --- | --- |
| key | [Virtual Key Constant (vk\_\*)](Keyboard_Input.md) | The key to simulate a press of. |

 

#### **Returns:**

N/A

 

#### **Example:**

keyboard\_key\_press(vk\_space);

This will simulate a spacebar press.
