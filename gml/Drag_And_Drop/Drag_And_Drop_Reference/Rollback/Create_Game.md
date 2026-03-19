# title

This action hosts a new multiplayer game. It takes the number of players that must be connected for the game to start, and optionally allows you to disable [Sync Test](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_System.md#h).

When called with Sync Test disabled, the system waits for the given amount of players to join before [starting](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Events.md) the game. Make sure to not create or modify any managed instances until the game starts.

TIP You can optionally force the game to start before all players have joined, by running [Start Game](Start_Game.md).

Currently you can only have up to 4 players in one game.

WARNING It is not recommended to set a default region in this action unless you are allowing the player to select it through a menu.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Count of players | The number of players that must be connected for the game to start. If [Define Player](Define_Player.md) is used, this is the number of instances that are automatically created. |
| Sync test | Specifies whether Sync Test should be enabled, and is enabled by default. When disabled, online functionality is enabled. |
| Region | Specifies the region where the virtual room will be created. For info on getting regions, see [rollback\_create\_game()](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Functions/rollback_create_game.md). |
