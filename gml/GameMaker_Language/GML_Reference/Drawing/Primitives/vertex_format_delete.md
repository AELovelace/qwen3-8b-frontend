# vertex\_format\_delete

This function deletes the given vertex format and must be called whenever you are finished using any created vertex formats.

You provide the vertex format (as returned by the function [vertex\_format\_end](vertex_format_end.md)), and this function will free the memory associated with it. Note that if you try to use this format again after calling this function, you will get an error.

 

#### Syntax:

vertex\_format\_delete(format\_id)

| Argument | Type | Description |
| --- | --- | --- |
| format\_id | [Vertex Format](vertex_format_end.md) | The vertex format to delete |

 

#### Returns:

N/A

 

#### Example:

vertex\_format\_delete(my\_format);

The above code will remove the vertex format stored in the variable my\_format from memory.
