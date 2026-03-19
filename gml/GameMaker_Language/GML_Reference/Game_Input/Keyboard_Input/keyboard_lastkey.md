# keyboard\_lastkey

This variable refers to the value that [keyboard\_key](keyboard_key.md#h) was in the previous frame, returning the keycode of that key (all standard keycode constants are returned).

This variable is *not* read\-only and you can change it, for example to set it to [vk\_nokey](Keyboard_Input.md#vk_nokey) if you handled it already.

 

#### **Syntax:**

keyboard\_lastkey

 

#### **Returns:**

[Virtual Key Constant (vk\_\*)](Keyboard_Input.md#table)

 

#### **Example:**

if (keyboard\_lastkey !\= vk\_nokey)  

 {  

     str \+\= keyboard\_lastchar;  

     keyboard\_lastkey \= vk\_nokey;  

 }

The above code checks to see if the keyboard\_lastkey variable is not equal to [vk\_nokey](Keyboard_Input.md#vk_nokey), and if it is it adds whatever the last key was as a string to the variable str, then it resets the keyboard\_lastkey variable to accept further input.
