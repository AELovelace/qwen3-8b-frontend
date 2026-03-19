# path\_end

This function ends the current path that the instance is following, as set when the function [path\_start](path_start.md) was called.

 
 

#### Syntax:

path\_end()

 

#### Returns:

N/A

 

#### Example:

 

if (place\_meeting(x, y, obj\_Blocker))   

 {  

     path\_end();  

 }

The above code will end the current path if the instance detects any collision with any instance of the given object.
