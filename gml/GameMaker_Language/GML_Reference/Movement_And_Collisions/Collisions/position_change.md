# position\_change

  Starting with GameMaker 2024\.14, this function is deprecated and can only be used if "**Allow instance\_change**" under [Deprecated Behaviours](../../../../Settings/Game_Options.md) is enabled.

This function will check a position for a collision with *any instances* at the given point, and if there is one, it will change **all** instances in collision to be instances of the chosen object. You can set the "perf" argument to true which will force GameMaker to perform the **Destroy** and **Clean Up** events of the found instance as well as the **Create** event of the new instance, or false to not perform any of these events. Please note, that if you choose not to perform the Destroy, Clean Up and Create events, any instance created that uses a variable normally defined in the create event will crash the game as that variable will no longer exist.

 

#### Syntax:

position\_change(x, y, obj, perf)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of where to change colliding instances. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of where to change colliding instances. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) | The new object the calling object will change into. |
| perf | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to perform that new object's Create event (true) or not (false). |

 

#### Returns:

N/A

 

#### Example:

position\_change(200, 200, obj\_Bird, true);

This will change all instances colliding at point (200,200\) into an instance of "obj\_Bird", performing "obj\_Bird"s Create event for each of them in the process.
