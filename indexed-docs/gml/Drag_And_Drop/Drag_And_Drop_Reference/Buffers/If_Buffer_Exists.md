# title

This action can be used to check if a given buffer ID is valid and the buffer actually exists in memory. If the buffer ID is valid and exists, the action will return true otherwise it will return false. You can flag "not"
 to make the action check if a buffer does *not* exist.

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Buffer | The buffer index (stored in a variable) |

 

#### Example:

The above action block code checks to see if a buffer exists and if it does it is deleted.
