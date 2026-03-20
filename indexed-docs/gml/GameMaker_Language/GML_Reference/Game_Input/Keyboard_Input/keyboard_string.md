# keyboard\_string

This variable holds a string containing the last (at most) 1024 characters typed on the keyboard. This string will only contain printable characters typed, but it *will* correctly respond to pressing the backspace key by erasing the last character. This variable is *not* read only and you can change it, for example to set it to "" (an empty string) if you handled it already, and you can use the [String Functions](../../Strings/Strings.md) to manipulate it.

  When using the on\-screen [Virtual Keyboard](../Virtual_Keys_And_Keyboards/Virtual_Keys_And_Keyboards.md), *only* this variable will be updated with the keyboard input.

  On Xbox GDK, this variable will only function when using the [virtual keyboard](../Virtual_Keys_And_Keyboards/keyboard_virtual_show.md). See [this Wiki article](https://github.com/GameMakerEnterprise/GMS2-Runner-Xbox/wiki/Keyboard-Input-on-Xbox-GDK) for more info.

 

#### **Syntax:**

keyboard\_string

 

#### **Returns:**

[String](../../../GML_Overview/Data_Types.md)

 

#### **Example:**

if string\_length(keyboard\_string) \> 15  

 {  

     keyboard\_string \= string\_copy(keyboard\_string, 1, 15\);  

 }

The above code will limit the length of the keyboard string to 15 characters, removing those that are over that limit by copying the first fifteen characters back into the variable.
