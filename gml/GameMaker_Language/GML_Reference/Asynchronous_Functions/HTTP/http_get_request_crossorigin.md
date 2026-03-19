# http\_get\_request\_crossorigin

This function can be used to get the cross\-origin type set for HTML5 games and will return a string (on all other platforms an empty string "" will be returned).

 

#### Syntax:

http\_get\_request\_crossorigin()

 

#### Returns:

[String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (string\_lower(http\_get\_request\_crossorigin()) !\= "use\-credentials")   

 {  

     http\_set\_request\_crossorigin("use\-credentials");  

 }  

 sprite\_add("sprites/player\_outfit\_1\.png", 0, false, false, 0, 0\);

The above code will first check the currently set cross origin type and if it is not "use\-credentials" then it is set to "use\-credentials" and then a sprite is added from a file.
