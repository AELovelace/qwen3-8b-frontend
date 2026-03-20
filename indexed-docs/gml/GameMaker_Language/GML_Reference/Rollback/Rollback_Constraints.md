# Rollback Constraints

The Rollback system has some constraints that you should be aware of. Breaking any of these constraints will result in [Sync Test](Rollback_System.md#h) throwing an error to let you know what's wrong.

## Browser Support

Rollback Multiplayer makes use of the WebTransport API, which [may not be supported on all browsers](https://caniuse.com/?search=webtransport). At the moment, Safari, Firefox and Internet Explorer are unsupported on desktop. Chrome, Firefox, and Safari on mobile are also unsupported.

## Rooms

You can change rooms while a multiplayer game is active, as long as all the players are connected.

Changing the room will cause the game to run its synchronisation process again.

Data for managed objects will **not** automatically be carried over when a room is changed. You can carry it over manually by using global variables, a persistent object, or by saving the local player's information to a file.

Using these options you can save the player's information before a room ends, and apply it back when the player instance is created in a new room.

## Event Order

When a multiplayer game starts, the following events will run in the given order:

- [Room Start](../../../The_Asset_Editors/Object_Properties/Other_Events.md#p)
- **Create** events for [defined players](Rollback_Functions/rollback_define_player.md)
- [Rollback Start](Rollback_Events.md#h)
	- rollback\_event\_param.first\_start will be true

When you change the room in the middle of a multiplayer game, the following events will run in the given order:

- [Room End](../../../The_Asset_Editors/Object_Properties/Other_Events.md#p1)
- **Clean Up** events for [defined players](Rollback_Functions/rollback_define_player.md)
- [Room Start](../../../The_Asset_Editors/Object_Properties/Other_Events.md#p)
- **Create** events for [defined players](Rollback_Functions/rollback_define_player.md)
- [Rollback Start](Rollback_Events.md#h)
	- rollback\_event\_param.first\_start will be false

## Destroy event

The **Destroy** event of an instance normally runs as soon as it's destroyed, for example, after [instance\_destroy()](../Asset_Management/Instances/instance_destroy.md) is called. However, the event may not run immediately in a multiplayer game.

An instance\_destroy() call can easily be run by a wrong prediction, which means that the destruction of the instance will soon be rolled back when the correct data from the responsible player is received.

Due to this, the Destroy event of an instance is only called when it's confirmed that it was supposed to be destroyed. This means there may be a slight lag in the instance being destroyed on a player's screen, and its Destroy event being called.

If you want something to happen on a client's screen on the same frame as an instance being destroyed, it's recommended to create a custom function and calling it along with instance\_destroy().

This also applies to the **Clean Up** event running on an instance being destroyed.

## State Management

Rollback Multiplayer manages the "state" of your game between clients, which includes managed instances and their variables. Such managed parts of your game are able to be rolled back in case of a wrong prediction by the Rollback system.

When you create or destroy a managed instance, or modify any properties/variables in a managed instance, you are updating the state of your game. This state is **not** sent to other players, as only [input](Rollback_Functions/rollback_define_input.md) is shared for all clients.

There are some restrictions with managing your game's state that you should follow to ensure proper synchronisation between players.

### State Before Rollback Start

You must ensure that each player starts at the same game state. This means that everything about your game and its managed instances must be the same for all players when the [Rollback Start](Rollback_Events.md) event triggers, which is when the game actually starts.

You can run any creation or set\-up code for your managed instances before that point, as long as it's done in exactly the same manner for all clients. To know if the game has started, use [rollback\_game\_running](Rollback_Variables/rollback_game_running.md).

You can use the time between your start/join call and the [Rollback Start](Rollback_Events.md) event to display a loading screen for the players waiting.

The player is returned to the same state on [leaving a game](Rollback_Functions/rollback_leave_game.md), meaning the use of [rollback\_game\_running](Rollback_Variables/rollback_game_running.md) is necessary to ensure that any game logic only runs while the game is connected.

### Global State

You cannot have global variables affecting your game state, as they are not synchronised between players. All required variables should be within managed objects.

### Draw Event State

You cannot change the state in a Draw event, and its purpose must remain to only draw graphics based on the state set in previous events. All managed objects become read\-only during a Draw event, so you cannot change any variables in them, and you cannot create or destroy instances of managed objects.

### Time Variables

Do not use variables/functions like [current\_time](../Maths_And_Numbers/Date_And_Time/current_time.md) or [get\_timer()](../Maths_And_Numbers/Date_And_Time/get_timer.md) to affect game logic. A managed variable called [rollback\_current\_frame](Rollback_Variables/rollback_current_frame.md) has been provided which can be used instead. It returns the number of frames that have passed since the multiplayer game began.

[Alarm events](../Asset_Management/Instances/Instance_Variables/alarm.md) are safe to use in managed objects.

Also make sure that you don't use [delta\_time](../Maths_And_Numbers/Date_And_Time/delta_time.md), as it is highly dependent on the system running the game and cannot be synchronised between players.

### Instance References

An instance ID stored in a managed instance must point to a managed instance.

If a managed instance has a reference to a non\-managed instance, it will result in inconsistencies between client states, as changes to that non\-managed instance can't be managed and rolled back.

For example, if your managed obj\_workstation instance has a reference to an obj\_anvil instance, obj\_anvil must be a managed object.

### Lost Instance References

A variable inside a managed instance, containing a reference to another managed instance, will be set to undefined if the referenced instance is destroyed.

This means that if a variable in a **persistent** managed instance contains a reference to a **non\-persistent** managed instance, that variable will be set to undefined when the room changes, as the non\-persistent instance would stop existing.

## Random Numbers

Random number generation (RNG) state is managed between players, so it's completely safe to use random functions (e.g. random(), choose(), etc.) for game logic. The Rollback system will ensure that each player gets the same random number at the same point in the game.

Draw events use a separate RNG state. This means that random functions called in a Draw event will not affect the regular RNG state for other events, and may not be the same between different players.

### Seeds

You can't use [randomise()](../Maths_And_Numbers/Number_Functions/randomise.md) or [random\_set\_seed()](../Maths_And_Numbers/Number_Functions/random_set_seed.md) to change the RNG seed, as it's managed by the Rollback system.

The managed RNG state only starts when [Rollback Start](Rollback_Events.md#h) is called, which is when the multiplayer game starts. You can change the seed before that point, which will not have any affect past the starting point.

## Further Reading

Read the following pages for more information on the Rollback system:

- [Rollback Events](Rollback_Events.md)
- [Create a Multiplayer Game](Creating_Multiplayer.md)
- [Rollback System](Rollback_System.md)
- [Defining Inputs](Defining_Inputs.md)
