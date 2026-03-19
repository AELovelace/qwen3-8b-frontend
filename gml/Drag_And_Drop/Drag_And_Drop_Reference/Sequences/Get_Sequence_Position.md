# Get Sequence Position

With this action you can retrieve the current position for the given sequence element in the room. You supply the sequence element ID (as returned by the action [Create Sequence](Create_Sequence_Element.md)), and this action will return its X and Y position in target variables. Note that the target variables can be flagged as temporary (local) variables, which will be created for the action and can be used in all subsequent actions for the event the action is in.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Variable | The ID of the sequence element to get the position of. |
| Target X | The target variable to hold the x position. |
| Target Y | The target variable to hold the y position. |

 

#### Example:

The above action block code retrieves the current position of the sequence element ID stored in the variable "my\_seq". These values are then used to set the position of the sequence, moving it 10 pixels to the right.
