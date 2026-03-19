# keyboard\_unset\_map

With his function you can clear all remapped keys so that they return to their default state, i.e.: all keys map to themselves.

 

#### **Syntax:**

keyboard\_unset\_map();

 

#### **Returns:**

N/A

 

#### **Example:**

if (keyboard\_check\_pressed(vk\_escape))  

 {  

     keyboard\_unset\_map();  

 }

The above example code will reset all mapped keys to their default settings if the user presses the "escape" key.
