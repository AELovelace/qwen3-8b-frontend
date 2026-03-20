# If Sequence Exists

This action can be used to check if the given sequence element exists in the game room. You give the element ID, as returned by the action [Create Sequence](Create_Sequence_Element.md), and if the sequence element exists in the room then the action will return true otherwise it will return false.

If you flag the "**Not**" argument, then the action will check to see if *no* such sequence element exists and if none are found it will return true.

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

These actions will now be run if the "if" evaluates to true, while any actions dropped elsewhere will be performed after the "if" block.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sequence | The element ID of the sequence element to check. |

 

#### Example:

The above action block code checks for to see if the sequence element stored in the variable "my\_seq" exists and if it does, it then destroys it.
