# webgl\_enabled

This **read\-only** variable holds whether WebGL is enabled (true) or not (false) for your game.

  This variable only contains a correct value for those games running through a browser (i.e.: HTML5\), on all other platforms it will hold true.

 

#### Syntax:

webgl\_enabled

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

if (webgl\_enabled)  

 {  

     global.quality \= 1;  

 }  

 else global.quality \= 0;

The above code checks the WebGL flag and then sets the global variable quality accordingly.
