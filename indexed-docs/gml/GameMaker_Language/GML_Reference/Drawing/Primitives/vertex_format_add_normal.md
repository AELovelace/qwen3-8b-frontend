# vertex\_format\_add\_normal

This function adds normal data (nx, ny and nz) as part of the new vertex format being created.

 

#### Syntax:

vertex\_format\_add\_normal()

 

#### Returns:

N/A

 

#### Example:

vertex\_format\_begin();  

 vertex\_format\_add\_texcoord();  

 vertex\_format\_add\_normal();  

 my\_format \= vertex\_format\_end();

The above code creates a new vertex format with just texture and surface normal values and then stores the format in the variable my\_format.
