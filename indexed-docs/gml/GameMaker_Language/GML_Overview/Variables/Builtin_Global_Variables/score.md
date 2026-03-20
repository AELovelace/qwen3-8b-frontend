# score

This variable is **global** in scope and is used to hold a numeric value which is usually used for the player score. This variable is only designed to support legacy projects from previous versions of GameMaker and should ***not be used in new projects*** as it is deprecated.

 

#### Syntax:

score

 

#### Returns:

[Real](../../Data_Types.md) (single precision floating point value)

 

#### Example

switch (object\_index)  

 {  

     case obj\_Enemy\_Fighter:  

         score \+\= 10;  

     break;  

  

     case obj\_Enemy\_Mage:  

         score \+\= 25;  

     break;  

  

     case obj\_Enemy\_Boss:  

         score \+\= 100;  

     break;  

 }  

 instance\_destroy();
 

The above code checks the object index of the instance running the code using a [switch](../../Language_Features/switch.md) statement, and then adds different amounts to the score variable depending on what object it is.
