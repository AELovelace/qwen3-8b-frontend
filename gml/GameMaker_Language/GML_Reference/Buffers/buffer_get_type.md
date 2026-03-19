# buffer\_get\_type

This function returns the type of the given buffer.

The return value will be one of the following constants:

 
 

#### Syntax:

buffer\_get\_type(buffer)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to check. |

 

#### Returns:

[Buffer Type Constant](buffer_create.md)

 

#### Example:

type \= buffer\_get\_type(buff);

The above code gets the type of the buffer stored in the variable buff and stores it in a variable.
