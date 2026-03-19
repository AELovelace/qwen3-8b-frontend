# health

This variable is **global** in scope and is used to hold a numeric value which is usually used for the player health. This variable is only designed to support legacy projects from previous versions of GameMaker and should ***not be used in new projects*** as it is deprecated.

 

#### Syntax:

health

 

#### Returns:

[Real](../../Data_Types.md) (single precision floating point value)

 

#### Example

if (health \<\= 0\)  

 {  

     global.state \= "Game Over";  

     instance\_destroy();  

 }

The above code checks the health variable and if it is less than or equal to 0, a global variable is set and the instance is destroyed.
