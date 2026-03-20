# Destroy Sequence

You can call this action whenever you wish to "destroy" a previously created sequence element. You give the element ID, as returned by the action [Create Sequence Element](Create_Sequence_Element.md), and this action will destroy it, removing it from the room.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Variable | The ID of the sequence element to destroy. |

 

#### Example:

The above action block code checks for to see if the sequence element stored in the variable "my\_seq" exists and if it does, it then destroys it.
