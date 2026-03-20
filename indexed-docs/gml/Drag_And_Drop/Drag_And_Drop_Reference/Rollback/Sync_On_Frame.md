# title

This action checks if all players are synchronised on the current frame, meaning their states are not based on predictions but on the actual data received from them. In such a case, it returns true.

If players are not synchronised on the current frame, it returns false, and attempts to synchronise all players.

Attempting to synchronise players with this action may cause a freeze. You must ensure that this action is not continuously called in a Step event.

Instead, use it as a toggle. See the example at the bottom of the page.

The variable [rollback\_confirmed\_frame](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Variables/rollback_confirmed_frame.md) is updated automatically when all players are synchronised.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Target | The variable where the returned value (true or false) is stored |

 

#### Example
