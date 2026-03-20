# event\_perform\_object

This function works the same as [event\_perform()](event_perform.md) except that this time you can specify events from another object. There are many options here which allow complete simulation of all possible events, but note that this literally just performs all the code in the event and the game will not modify anything to make it trigger itself manually, for example if you choose to perform a keyboard press event, the event will be triggered but the relevant key will not be recognised as having been pressed. Or if you perform an alarm event, the alarm counter will not be set to \-1 but rather continue to count down. You can find a complete list of the available constants this function requires from the page for the function [event\_perform()](event_perform.md).

NOTE Actions in the event called with this function are applied to the **current instance**, and not to instances of the given object.

 

#### Syntax:

event\_perform\_object(obj, type, numb)

| Argument | Type | Description |
| --- | --- | --- |
| obj | [Object Asset](../../../../../The_Asset_Editors/Objects.md) | The object that should have its event triggered. |
| type | [Event Type Constant](event_perform.md) | The type of event to perform. |
| numb | [Real](../../../../GML_Overview/Data_Types.md) or [Event Number Constant](event_perform.md) | The specific event, if one is necessary (otherwise, just use 0\). |

 

#### Returns:

N/A

 

#### Example:

event\_perform\_object(obj\_Player, ev\_keypress, ord("W"));

This would perform the event associated with Keyboard Check Pressed \> W key from the object "obj\_Player" in the current instance.
