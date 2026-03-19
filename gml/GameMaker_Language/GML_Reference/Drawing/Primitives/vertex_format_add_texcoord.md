# vertex\_format\_add\_texcoord

This function adds texture position data (u and v) as part of the new vertex format being created.

 

#### Syntax:

vertex\_format\_add\_texcoord()

 

#### Returns:

N/A

 

#### Example:

vertex\_format\_begin();  

 vertex\_format\_add\_texcoord();  

 vertex\_format\_add\_position\_3d();  

 my\_format \= vertex\_format\_end();

The above code creates a new vertex format with just texture and position values and then stores the format in the variable my\_format.
