# keyboard\_virtual\_height

This function returns the current height in pixels of the virtual keyboard, based on the size of the *display*.

The function returns 0:

- if the keyboard is not visible.
- on platforms that don't have a virtual keyboard.

**NOTE** This function is only valid for the **Xbox (GDK)**, **Android** (including **AndroidTV**), and **iOS** (including **tvOS**) target platforms.

 

#### Syntax

keyboard\_virtual\_height()

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (keyboard\_virtual\_status() \=\= true)  

 {  

     key\_h \= keyboard\_virtual\_height();  

 }

The above code will check the status of the OS virtual keyboard, and if it's visible set a variable to the height of the keyboard.
