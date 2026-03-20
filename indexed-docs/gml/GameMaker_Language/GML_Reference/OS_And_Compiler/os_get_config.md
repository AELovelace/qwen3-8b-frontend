# os\_get\_config

This function returns the name (as a string) of the currently selected configuration for your game. For more information on configurations please see the section [Configurations](../../../Settings/Configurations.md).

 

#### Syntax:

os\_get\_config()

 

#### Returns:

 

#### Example:

if (os\_get\_config() \= "Free\_Version")   

 {  

     global.Ads \= true;  

 }  

 else global.Ads \= false;

The above code will check to see which configuration is being used and if it is the one called "Free\_Version", ads will be enabled in the game.
