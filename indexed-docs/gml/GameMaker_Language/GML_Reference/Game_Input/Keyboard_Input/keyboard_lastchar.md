# keyboard\_lastchar

This variable stores a string of the last key pressed. This variable is *not* read\-only and you can change it, for example to set it to "" (an empty string) if you handled it already.

 
 

#### **Syntax:**

keyboard\_lastchar

 

#### **Returns:**

[String](../../../GML_Overview/Data_Types.md)

 

#### **Example:**

if (keyboard\_lastkey !\= vk\_nokey)  

 {  

     str \+\= keyboard\_lastchar;  

     keyboard\_lastkey \= vk\_nokey;  

 }

The above code checks to see if the [keyboard\_lastkey](keyboard_lastkey.md) variable stores a valid key, and if it is it adds whatever the last key was as a string to the variable str.
