# Rollback System

After following the [Create a Multiplayer Game](Creating_Multiplayer.md) tutorial, you may have some questions about how the Rollback system works. This page aims to expand on it.

## What is Rollback?

It's easy to experience lag when playing online. If you're playing with someone remotely, it may take a fraction of a second for their input to reach you, but even that can be enough to ruin your game experience.

Rollback uses predictions to reduce the effect of lag. Based on previous inputs, it predicts what the other user is going to do next, and shows you the result of that prediction, which is instant.

When the prediction is correct, you don't experience lag, and your game feels much more responsive.

However, sometimes the system realises its prediction was wrong. In that case, it *rolls back* to the last correct state, and continues the game from that point. This is why it's called "**Rollback multiplayer**".

### Determinism

Rollback is deterministic. It only shares inputs with other players, and expects all of them to run the same logic on the given input, giving the same results on all clients.

A different approach to multiplayer is "state replication", which continually synchronises the state of the game between clients, ensuring they are always doing the same thing.

Rollback does not do that \-\- it only ever sends inputs, but also keeps an eye on the state so it can be rolled back in case of a wrong prediction.

***What is a client?***
  

  

 A "client" is a player in your game, and refers to their copy of the game, running on their machine. 

## How does it work?

As previously mentioned, Rollback **only communicates input** between players.

There are two main things that Rollback handles:

- **Input**: Each player's [inputs](Rollback_Functions/rollback_define_input.md) are sent to other players. If Player 0 presses **"fire"** in their own client, Rollback will ensure that other clients also see Player 0 press **"fire"**.
   

  

**Predictions are only run on input.**
- **State**: This includes all managed objects and their variables. These are NOT synchronised between players: changing one variable in one client will not automatically update it in another client.
   

  

**State is only managed for the purpose of being rolled back.**

## So... what's the difference?

**Input** changes **state**, which is the base concept of Rollback multiplayer.

Here is an example:

- **Input**: Player 0 presses **"fire"**.
- **State**: Because Player 0 pressed fire, a projectile is created. That projectile eventually collides with a rock. This results in Player 0 getting a point.
   

  

 This is essentially your whole game, dependent entirely on input.

"**Input**" is what Rollback communicates between all players, not the state.

However, because all game clients run the same logic on the received input (which is a requirement), **they all result in the same state**.

## What is state, then?

If only input is synchronised, then what is **state** for?

Because input affects state, a wrong input prediction can result in a **wrong state**.

When rollback finds that a prediction was wrong, it replaces the current state with the correct state, and runs inputs and predictions from that point again. This includes all your managed objects and their variables.

This does not mean that Rollback is synchronising objects and variables between clients. Just because variable\_a is set to "Gurpreet" in one client, it won't mean other clients will also see the same value.

They would only see the same value for a variable if it was derived from a player's input, or some other managed system, such as alarms and random functions.

## Managed Objects

Objects have a "**Managed**" checkbox, which is enabled for new objects by default:

Objects that are marked as managed have the ability to be rolled back and to have predictions run on them, including all of their variables, creation and destruction.

All objects that are part of your gameplay, like the player, manager/controller objects, item pickups, projectiles, etc. must be marked as managed.

You can disable this for objects that don't need to be synchronised between players, such as static world objects, visuals, effects, etc. that don't affect gameplay in any way.

Note that the managed property of a parent is not applied to its children automatically, so each child object needs to have its managed checkbox set manually.

## Sync Test

[rollback\_create\_game()](Rollback_Functions/rollback_create_game.md) takes an argument for Sync Test, which is enabled by default (when the argument is not specified).

Sync Test is used to test your game offline. If any synchronisation issues pop up, it lets you know by printing the error to the Output Log. You can use Sync Test on Windows, macOS and GX.games.

Sync Test executes all of your game's code twice in a frame, so it can check for any synchronisation issues. This means you may see some events happening twice when testing offline, which will not happen when your game is running online.

### Random and Mock Input

During Sync Test, "remote" player instances are given random input values for their [defined inputs](Defining_Inputs.md), as a simple form of testing. You can disable this using [rollback\_use\_random\_input()](Rollback_Functions/rollback_use_random_input.md).

The second player is getting random input during Sync Test.

You can also assign temporary mock input to remote players when in Sync Test. See [Mock Input](Defining_Inputs.md#h1) for details.

## Developing Multiplayer Effectively

You must ensure that all game clients run the **same logic** when the **same input** is received. If a particular instance was created or moved only for one client, it will not be reflected on the other clients.

This problem usually does not occur if you program your game as shown in [Create a Multiplayer Game](Creating_Multiplayer.md), with all player logic running the same way for all player instances regardless of whether an instance is [local or not](Rollback_Variables/player_local.md). However if you implement a condition to only do something for a particular player, and not for others, that will cause a disruption in the game state.

## Defining A Player Object

### Automatic Creation of Player Instances

As shown in [Create a Multiplayer Game](Creating_Multiplayer.md), you can define a player object with [rollback\_define\_player()](Rollback_Functions/rollback_define_player.md) / [Define Player (Rollback)](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Define_Player.md) and the system will automatically create instances of it for each connected player. It will also destroy instances for players that disconnect.

Player instances created this way have their IDs assigned automatically, in the [player\_id](Rollback_Variables/player_id.md) variable. Within each player instance, you can simply call [rollback\_get\_input()](Rollback_Functions/rollback_get_input.md) without any arguments and it gives you the inputs for that particular player.

This is the standard way of using the Rollback system, however you can also manage player instances and their inputs manually.

### Manual Creation of Player Instances

To manage player instances manually, don't call [rollback\_define\_player()](Rollback_Functions/rollback_define_player.md). This will cause the game to start without any player instances being created.

Then create your own player instances manually, ideally in the [Rollback Start](Rollback_Events.md#h) event, and give them player IDs in a custom variable. To get input for a player, call [rollback\_get\_input()](Rollback_Functions/rollback_get_input.md) and specify the ID of the player as an argument. Call [rollback\_get\_info()](Rollback_Functions/rollback_get_info.md) to get those [variables](Rollback_Variables/Rollback_Variables.md) in a struct that would otherwise be assigned to players automatically.

This way you can manually manage when and how player instances are created, the IDs assigned to them, and retrieving input for a specific player.

### Keep Player Instances Alive

If you're using [rollback\_define\_player()](Rollback_Functions/rollback_define_player.md) / [Define Player (Rollback)](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Define_Player.md), do not destroy the player instances that are created. If you need to show a player as defeated, then change its sprite, or hide it using some other method, but keep the instance alive as it's managed by GameMaker.

## Single Player

The Rollback system can be used when creating a single\-player game. Simply specify **1** as the number of players when calling [rollback\_create\_game()](Rollback_Functions/rollback_create_game.md).

This way the system will never connect to any servers and your game will essentially be offline, with the ability to be expanded into an online multiplayer game whenever you wish.

Take this approach when you are making a new project that may make use of multiplayer in the future, as it will be tougher to implement multiplayer into your game once it's already completed without using the Rollback system.

## Manual vs. Auto Start

By default, a multiplayer game starts as soon as all players have joined. However you can start it before that point by calling [rollback\_start\_game()](Rollback_Functions/rollback_start_game.md).

You can completely disable the auto\-start behaviour by calling [rollback\_use\_manual\_start()](Rollback_Functions/rollback_use_manual_start.md). This means the game will wait for you to manually start the game.

Auto\-start is automatically disabled when player preferences [are enabled](Rollback_Functions/rollback_use_player_prefs.md).

## Further Reading

Read the following pages for more information on the Rollback system:

- [Defining Inputs](Defining_Inputs.md)
- [Rollback Constraints](Rollback_Constraints.md)
- [Rollback Events](Rollback_Events.md)
- [Player Preferences](Rollback_Preferences.md)
