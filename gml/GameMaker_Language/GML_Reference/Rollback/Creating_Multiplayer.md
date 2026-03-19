# Create a Multiplayer Game

This page will take you through the detailed steps for creating your first multiplayer game.  

  

 For information on the Rollback system, read [Rollback System](Rollback_System.md).  

  

 For details on all Rollback functions, read [Rollback Functions](Rollback_Functions/Rollback_Functions.md).
 

## Project Set\-Up

Start a new project, and create a sprite for your player object. You can import an image or just create a filled square.

Create two objects:

- **obj\_game**: This will manage your multiplayer game.
- **obj\_player**: This will be your actual player object. Each connected player will have their own instance of this object that they can control.  

  

 Assign your player sprite to the player object.

Go ahead and place **obj\_game** into a room. **Don't** place **obj\_player**, as it will be created automatically.

## Starting the Game

Add the Create event to **obj\_game**, and write the following code in it:

NOTE If you're using GML Visual, use the corresponding [Rollback Actions](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Rollback_Actions.md).

rollback\_define\_player(obj\_player);  

  

 var \_joined \= rollback\_join\_game();  

  

 if (!\_joined)  

 {  

     rollback\_create\_game(2\);  

 }
 

It first defines the player object to use, and attempts to join a game using [rollback\_join\_game()](Rollback_Functions/rollback_join_game.md). This function returns true if the system found a game to join (meaning you are on the correct URL).

If the game could not be joined, it returns false. When the returned value is false, we call [rollback\_create\_game()](Rollback_Functions/rollback_create_game.md) to host our own game. There we specify that the game should allow a maximum of 2 players.

NOTE At the moment, you can only create games for up to 4 players.

The code above will create two instances of **obj\_player** at the top\-left corner of the room, but they will not yet be controllable.

## Moving Players

Input is managed by the Rollback system and automatically synchronised between players.

In your player object, call [rollback\_get\_input()](Rollback_Functions/rollback_get_input.md) to get a struct containing all of the default inputs, which are as follows:

**left**, **right**, **up**, **down**, **Z**, **X**, **C**, **space**  

  

*These indicate whether the key is held.* \***\_pressed** *and* \***\_released** *variants are also provided.*

To define your own inputs, see [Defining Inputs](Defining_Inputs.md).

Now set up the player with the following code in its Create and Step events:

// Create Event  

 move\_speed \= 5;  

  

 // Step Event  

 var \_input \= rollback\_get\_input();  

  

 if (\_input.left) x \-\= move\_speed;  

 if (\_input.right) x \+\= move\_speed;  

 if (\_input.up) y \-\= move\_speed;  

 if (\_input.down) y \+\= move\_speed;
 

This sets up a variable with the speed of the player, and in the Step event, gets the input struct.

Based on each arrow key held, it moves the instance on the corresponding axis, e.g. pressing left reduces the X, pressing up reduces the Y, and so on.

## Player Locations

Before we test, let's ensure the players are created at specific locations, instead of spawning at the top\-left corner of the room.

In the Create event of your player object, write this:

if (player\_id \=\= 0\)  

 {  

     x \= 300;  

 }  

 else if (player\_id \=\= 1\)  

 {  

     x \= room\_width \- 300;  

 }  

  

 y \= room\_height / 2;
 

[player\_id](Rollback_Variables/player_id.md) is a built\-in instance variable that stores the ID of the player instance.

Since our game has two players, our first player will have the ID **0**, and the second player will have the ID **1**.

Based on that, we are changing the initial X position of the player. The Y position is the same for both.

Now run the game, and you will see both players, where you can control the first one:

The second player is moving erratically on its own, which is a feature of the Rollback system. It automatically provides random values every frame for all defined inputs, as a basic form of test for your game.

You can disable automatic random movement by calling [rollback\_use\_random\_input(false)](Rollback_Functions/rollback_use_random_input.md), or [set up your own "mock" input](Defining_Inputs.md#h1) for the other player.

## Online Connection

Your basic multiplayer example is complete, and it's ready to be taken to the internet.

By default, the system starts in **Sync Test** mode, which is how you test your game offline. To enable online functionality, the second argument of [rollback\_create\_game()](Rollback_Functions/rollback_create_game.md) needs to be set to false (which disables Sync Test).

// obj\_game: Create event  

 rollback\_define\_player(obj\_player);  

  

 var \_joined \= rollback\_join\_game();  

  

 if (!\_joined)  

 {  

     rollback\_create\_game(2, false);  

 }
 

Sign into [GX.games](https://gx.games) and set a region in your [profile settings](https://gx.games/profile/account-details/).

Run the game through the **GX.games** target. When the Rollback system begins, it creates a new "room": not a GameMaker room asset, but a **virtual room** in which the players will play together.

## Inviting Players

When your game starts, you will not see the player instances immediately. Instead, the system will wait for all players to join before starting the game.

TIP You can start the game before players have joined by calling [rollback\_start\_game()](Rollback_Functions/rollback_start_game.md). If you call [rollback\_use\_manual\_start()](Rollback_Functions/rollback_use_manual_start.md) then the game will wait for you to start it manually even after all players have joined.

While waiting, you will see a "**Copy Share Url**" button below your game. Scroll down if you don't see the button.

This will copy a link to your game, which you can paste into another browser window to join as the second player.

You need to have both browser windows visible at the same time, otherwise the player whose window is hidden will time out and your game will end.

Once both game instances have connected and synchronised, you will be able to control each player through its browser window:

You can open both windows side\-by\-side by dragging and resizing them.

During your test you will see debug messages in the top\-left corner of your game, giving you info on the state of your game. You can disable this by calling [rollback\_display\_events(false)](Rollback_Functions/rollback_display_events.md).

## Leaving a Room

Call [rollback\_leave\_game()](Rollback_Functions/rollback_leave_game.md) to make a player leave the room. Read the [function page](Rollback_Functions/rollback_leave_game.md) for detailed information on its use.

## Game Logic

The Rollback system will automatically create player instances when all players have joined, as long as you're using [rollback\_define\_player()](Rollback_Functions/rollback_define_player.md).

However it still allows you to run any other code before the game starts, meaning you must take care to only start your core game logic once all players have joined.

For example, if you're spawning enemy instances using an alarm, only start that alarm once the [Rollback Start](Rollback_Events.md#h) event triggers.

## Major Events

Major events in your game, such as a player winning and ending the level, should be done when all players are synchronised. Otherwise, a wrong prediction might wrongly make a player win, which would appear odd when it eventually rolls back.

See the example on [rollback\_sync\_on\_frame()](Rollback_Functions/rollback_sync_on_frame.md) for doing this properly.

## Further Reading

Your first multiplayer game is now complete!

Read the following pages to learn all about the Rollback system:

- [Rollback System](Rollback_System.md)
- [Defining Inputs](Defining_Inputs.md)
- [Rollback Constraints](Rollback_Constraints.md)
- [Rollback Events](Rollback_Events.md)
- [Player Preferences](Rollback_Preferences.md)

You can add chat to your game using [rollback\_chat()](Rollback_Functions/rollback_chat.md).
