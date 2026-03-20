# If Instance Exists

This action can be used to check if an instance of a specific object exists in the game room, or if a specific instance itself exists. You give the object from [The Asset Browser](../../../Introduction/The_Asset_Browser.md), and if any instance exists in the room then the action will return true otherwise it will return false. Note that you can use a variable here with the unique ID for specific instance (for example as returned by the action [Create Instance](Create_Object_Instance.md)) or even the instance ID value as returned by [The Room Editor](../../../The_Asset_Editors/Rooms.md) when you added the instance.

If you flag the "Not" argument, then the action will check to see if *no* instance exists and if none are found it will return true and if even one exists it will return false.

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

These actions will now be run if the "if" evaluates to true, while any actions dropped elsewhere will be performed after the "if" block.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Object | The name of the object to check for an instance of (or an instance ID). |

 

#### Example:

The above action block code checks for a collision and returns the unique ID value of the instance that is being collided with. This value is stored in a temporary variable and then checked to see if the value corresponds to an instance that is currently within the room (if no collision is found then the variable will hold the keyword [noone](../../../GameMaker_Language/GML_Overview/Instance Keywords/noone.md)), and if it does, then a variable is set in the instance being collided with.
