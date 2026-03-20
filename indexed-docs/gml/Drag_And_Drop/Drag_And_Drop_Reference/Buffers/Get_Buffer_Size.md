# title

This action can be used to retrieve the size of a buffer, in bytes. You supply the unique buffer ID value as returned by the action [Create Buffer](Create_Buffer.md) and then give a target variable to return the size value to. The target
 variable can be flagged as being a temporary local variable, in which case it will be created for you and removed from memory again at the end of the current action script or event.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Buffer | The buffer index (stored in a variable) |
| Target | The target variable to hold the returned value |

 

#### Example:

The above action block code gets the size of the buffer and then uses that value to set the
 read/write position to the end of the currently stored data.
