# vertex\_format\_add\_position\_3d

This function adds 3D position data (x, y and z) to the new vertex format being created.

 

#### Syntax:

vertex\_format\_add\_position\_3d()

 

#### Returns:

N/A

 

#### Example:

vertex\_format\_begin();  

 vertex\_format\_add\_colour();  

 vertex\_format\_add\_position\_3d();  

 my\_format \= vertex\_format\_end();

The above code creates a new vertex format with just colour and position values and then stores the format in the variable my\_format.
