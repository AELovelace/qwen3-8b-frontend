# Hide Virtual Keyboard

This action can be used to hide the virtual keyboard on the device running the game. Calling this action will generate a [System Asynchronous Event](../../../The_Asset_Editors/Object_Properties/Async_Events/System.md), in which the [async\_load](../../../GameMaker_Language/GML_Overview/Variables/Builtin_Global_Variables/async_load.md)  [DS map](../../../GameMaker_Language/GML_Reference/Data_Structures/DS_Maps/DS_Maps.md) will be populated with the following key/value pairs:

- "**event\_type**" \- this will be "**virtual keyboard status**" when triggered by virtual keyboard actions.
- "**screen\_height**" \- the height of the virtual keyboard (in pixels). This will be 0 if the keyboard is invisible.
- "**keyboard\_status**" \- the current status of the keyboard, returned as one of the following strings:
	- "hiding"
	- "hidden"
	- "showing"
	- "visible"

 

#### Action Syntax:

#### Example:

The above action block code checks for a mouse down action, and if one is
 detected, then a check is performed to see if the OS virtual keyboard is showing. If it isn't then it is set to show \- using a numeric keypad type \- and if is already showing then it is hidden.
