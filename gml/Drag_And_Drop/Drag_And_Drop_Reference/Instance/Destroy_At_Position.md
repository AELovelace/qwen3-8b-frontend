# Destroy At Position

This action block will destroy *all* instances found at the point given, calling the [Destroy Event](../../../The_Asset_Editors/Object_Properties/Object_Events.md) and then the [Clean Up Event](../../../The_Asset_Editors/Object_Properties/Object_Events.md) for all instances found.

Note that this action is based on the collision mask of the instances, and if any part of the mask overlaps with the target point it then the function will destroy that instance (if the instances have no sprite or mask applied, then they will not be destroyed).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| x | The x position in the room to use. |
| y | The y position in the room to use. |

 

#### Example:

The above action block code checks for a key\-press (the space key) and if one is detected it will destroy all the instances found at the instances relative position.
