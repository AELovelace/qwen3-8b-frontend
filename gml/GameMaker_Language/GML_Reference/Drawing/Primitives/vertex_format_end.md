# vertex\_format\_end

This function ends the vertex format that was started with [vertex\_format\_begin](vertex_format_begin.md) and returns it.

 

#### Syntax:

vertex\_format\_end()

 

#### Returns:

[Vertex Format](vertex_format_end.md)

 

#### Example:

vertex\_format\_begin();  

 vertex\_format\_add\_position();  

 vertex\_format\_add\_colour();  

 my\_format \= vertex\_format\_end();

The above code creates a new vertex format with just position and colour values and then stores the format in the variable my\_format.
