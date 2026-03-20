# Call Parent Event

This action block will perform the event of the parent object that the instance is a child of before continuing to run the actions in the actual instance. When you assign a parent object to an instance, all the events from that object are "inherited" by the child. However if you then add an event to the child object, it overrides the parent event. Using this action block, you can force a child object to run both the parent event and the event in the instance itself. See [The Object Editor](../../../The_Asset_Editors/Objects.md) section for more information on parents.

 

#### Action Syntax:

#### Example:

The above action block code calls the parent event of the object that the instance is a child of and then sets an alarm and changes the sprite.
