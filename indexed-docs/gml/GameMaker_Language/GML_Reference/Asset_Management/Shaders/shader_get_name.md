# shader\_get\_name

With this function you can retrieve the name of a shader resource. You supply the handle for the shader to get the name of and the function will return the name of the resource as a string.

 

#### Syntax:

shader\_get\_name(shader)

| Argument | Type | Description |
| --- | --- | --- |
| shader | [Shader Asset](../../../../The_Asset_Editors/Shaders.md) | The handle of the shader to get the name of. |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_shader \= shader\_current();  

 var \_name \= shader\_get\_name(\_shader);  

 draw\_text(32, 32, "Debug \- Currently Rendering \= " \+ \_name);

The above code will get the name of the given shader and draw it to the screen.
