# title

This action can be used to delete a buffer from memory, releasing the resources used to create it and removing any data that it may currently contain. You supply the unique buffer ID value as returned by the action [Create Buffer](Create_Buffer.md). Note that you can select multiple buffers for removal by clicking the plus icon  beside the action, and adding another buffer ID.

  It's important to always remove any dynamically created resources from memory when you no longer need them to prevent memory leaks.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Buffer | The buffer index (stored in a variable) |

 

#### Example:

The above action block code checks to see if a buffer exists and if it does it is deleted.
