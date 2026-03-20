# title

This action returns a struct containing the input values for a player. It takes an optional argument specifying the ID of the player for which inputs will be returned.

It's recommended to use [If Key Down (Rollback)](If_Key_Down_(Rollback).md), [If Key Pressed (Rollback)](If_Key_Pressed_(Rollback).md) and [If Key Up (Rollback)](If_Key_Up_(Rollback).md) for checking inputs in multiplayer.

When used in a player instance that was created by [Define Player (Rollback)](Define_Player.md), you do not need to specify a player ID, so you can just specify player\_id.

When used in any other instances, or player instances that were created manually, you must specify a player ID.

For information on what inputs are returned and how they can be changed, see [Defining Inputs](../../../GameMaker_Language/GML_Reference/Rollback/Defining_Inputs.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Player ID | The ID of the player to get input for |
| Target | The variable where the returned struct should be stored |
