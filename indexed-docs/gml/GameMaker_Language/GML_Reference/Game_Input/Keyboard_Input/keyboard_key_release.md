# keyboard\_key\_release

With this function you can simulate the release of any key on the keyboard. The function will take a keycode value as returned by the function [ord()](../../Strings/ord.md) (only *capital* letters from A\-Z or numbers from 0\-9\),
 or any of the vk\_\* constants listed on the main [Keyboard Input](Keyboard_Input.md) page.

 

#### **Syntax:**

keyboard\_key\_release(key);

| Argument | Type | Description |
| --- | --- | --- |
| key |  | The key to simulate a release of. |

 

 

#### **Returns:**

 

#### **Example:**

keyboard\_key\_release(vk\_space);

This will simulate a spacebar release.
