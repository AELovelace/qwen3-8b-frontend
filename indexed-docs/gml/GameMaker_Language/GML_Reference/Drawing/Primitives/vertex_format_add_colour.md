# vertex\_format\_add\_colour

This function adds an RGBA colour attribute to the new vertex format being created.

  The attribute is stored as four bytes in the vertex buffer and turned into a vec4 (floats).

 

#### Syntax:

vertex\_format\_add\_colour()

 

#### Returns:

N/A

 

#### Example:

vertex\_format\_begin();  

 vertex\_format\_add\_colour();  

 vertex\_format\_add\_position();  

 my\_format \= vertex\_format\_end();

The above code creates a new vertex format with just colour and position values and then stores the format in the variable my\_format.
