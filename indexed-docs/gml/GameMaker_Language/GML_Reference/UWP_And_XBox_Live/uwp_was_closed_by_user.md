# uwp\_was\_closed\_by\_user

With this function you can find out if the game was previously shut down by the user while playing (i.e. it, was terminated correctly and not by the system). If it has been then the function will return true, otherwise it will return false.

 

#### Syntax:

uwp\_was\_closed\_by\_user();

 

#### Returns:

[Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (uwp\_was\_closed\_by\_user())   

 {  

     global.GameLoaded \= false;  

 }

The above code checks to see if the app has previously been terminated by the user, and if so, it sets a global variable.
