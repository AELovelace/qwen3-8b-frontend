# keyboard\_set\_map

This function maps a keyboard key to another one using the keycode value so that any input from either key will be interpreted as the same.

Sometimes when making a game you may wish one key to do the same as another. For example, many people use the keys WASD for movement, but then many people *also* use the arrow keys! So, what to do? Well, you *could* code the movement system twice, but that is a bit complicated and thankfully redundant as this function permits you to "map" one key to another and so any input from either key will be interpreted as the same. To do this you choose a key that you want to map (key2 \- this will be the key that you write the code for) and a key that you want it to be mapped *to* (key1). After that, keypresses to either key will be interpreted by GameMaker as coming from key2. You can also use this function to design a system where the user can define their own keys for playing by simply mapping the user input key to the key that you've coded into the game.

The function takes a keycode value as returned by the function [ord](../../Strings/ord.md) (only *capital* letters from A\-Z or numbers from 0\-9\), or any of the vk\_\* constants listed on the main [Keyboard Input](Keyboard_Input.md) page.

  The key you are mapping to (key1) will no longer be usable as its actual key symbol once you use this function. For example, if you map the up arrow key to "W" then you will no longer be able to detect the press of the "W" key as a "W", it will always be considered as the up arrow. To undo this, either map the key to itself \- so both key1 and key2 would be ord("W") \- or use the function [keyboard\_unset\_map](keyboard_unset_map.md).

 

#### **Syntax:**

keyboard\_set\_map(key1, key2\)

| Argument | Type | Description |
| --- | --- | --- |
| key1 | [Virtual Key Constant (vk\_\*)](Keyboard_Input.md) | This is the key that key2 is to be mapped to |
| key2 | [Virtual Key Constant (vk\_\*)](Keyboard_Input.md) | This is the key that is to be mapped |

 

#### **Returns:**

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### **Example:**

keyboard\_set\_map(ord("A"), vk\_left);

The above example code will map the "A" key to the left arrow key. This means that the player can use either the "A" *or* the left arrow key, and that all code written for the left arrow will also respond to the "A" key being used instead.
