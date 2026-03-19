# device\_is\_keypad\_open

This does a check of the device for a keypad and if one is available it returns true otherwise it returns false. Please note that this function is mainly for use with Android devices

For those users with a *Sony Xperia Play*, there is a set button/key map setup within GameMaker, so you can use the [keyboard constants](../Keyboard_Input/Keyboard_Input.md) **vk\_up**, **vk\_down**, **vk\_left**, **vk\_right** for the joypad keys and *Triangle* is ord("T"), *Square* is ord("S"), *Circle* is **vk\_alt** \+ **vk\_backspace** while the *back* button is simply vk\_backspace, *Cross* is **vk\_space**, *Select* is **vk\_return** and *Start* is **vk\_rshift**, the *L Trigger* is ord("L") and *R Trigger* is ord("R").

 

#### Syntax:

device\_is\_keypad\_open
 

#### Returns:

 

#### Example:

if (device\_is\_keypad\_open())   

 {  

      global.Setting \= 2;  

 }  

 else  

 {  

      global.Setting \= 1;  

 }

The above code checks for a keypad then changes a global variable depending on the returned value.
