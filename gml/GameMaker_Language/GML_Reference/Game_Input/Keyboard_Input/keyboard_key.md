# keyboard\_key

With this variable you can get the keycode of the key that is currently being pressed and it will return 0 if no key is being pressed when the check is done.

 

#### **Syntax:**

keyboard\_key;

 

#### **Returns:**

Virtual Key Constant

 

#### **Example:**

switch (keyboard\_key)  

 {  

     case vk\_numpad1: gun \= weapon\[0]\[0]; break;  

     case vk\_numpad2: gun \= weapon\[1]\[0]; break;  

     case vk\_numpad3: gun \= weapon\[2]\[0]; break;  

 }

The above code uses the value of the keyboard\_key variable to set a variable to the same value as an array.
