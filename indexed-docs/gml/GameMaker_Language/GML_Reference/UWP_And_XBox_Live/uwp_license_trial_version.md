# uwp\_license\_trial\_version

This function can be used to check whether the game is under a trial licence or not. If it is the function will return true, or false otherwise.

 

#### Syntax:

uwp\_license\_trial\_version();

 

#### Returns:

[Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (uwp\_license\_trial\_version())   

 {  

     global.LevelCap \= 10;  

 }

The above code checks to see if the app is under a trial licence and, if so, it sets a global variable.
