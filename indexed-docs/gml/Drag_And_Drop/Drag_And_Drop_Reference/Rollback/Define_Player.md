# title

This action tells the Rollback system the object that should be used for players. This is optional, and when used, the system will automatically create instances for players that connect, and destroy instances for players that disconnect.

You can specify the layer where the player instances will be created. If a layer is not specified, players will be created on the "Instances" layer, which must exist in the room.

For information on creating a game with or without this function, see [Defining A Player Object](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_System.md#h1).

If used, this function must run before the [join](Join_Game.md)/[start](Start_Game.md) action.

Each instance created with this function gets the [instance variables listed on this page](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Variables/Rollback_Variables.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Object | The object to use for player instances |
| Layer | OPTIONAL The name of the layer where the player instances will be created. "Instances" by default (when no value is specified). |
