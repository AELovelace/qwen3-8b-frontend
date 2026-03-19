# timeline\_moment\_clear

With this function you can clear a specific moment of any previously defined time line of all codes and actions.

 

#### Syntax:

timeline\_moment\_clear(ind, step)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Timeline Asset](../../../../../The_Asset_Editors/Timelines.md) | The index of the timeline to clear. |
| step | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The moment to clear. |

 

#### Returns:

N/A

 

#### Example:

timeline\_moment\_clear(global.tl, game\_get\_speed(gamespeed\_fps) \* 30\);

The above code will clear the specified moment of the time line indexed by the variable global.tl.
