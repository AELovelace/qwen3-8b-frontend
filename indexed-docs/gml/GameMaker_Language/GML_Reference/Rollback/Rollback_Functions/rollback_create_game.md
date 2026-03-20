# rollback\_create\_game

This function hosts a new multiplayer game. It takes the number of players that must be connected for the game to start, and optionally allows you to disable [Sync Test](../Rollback_System.md#h).

When called with Sync Test disabled, the system waits for num\_players amount of players to join before [starting](../Rollback_Events.md) the game. Make sure to not create or modify any managed instances until the game starts.

TIP You can optionally force the game to start before all players have joined, by calling [rollback\_start\_game()](rollback_start_game.md).

Currently you can only have up to 4 players in one game.

WARNING It is not recommended to set a default region in this function unless you are allowing the player to select it through a menu.

 

#### Syntax:

rollback\_create\_game(num\_players, \[enable\_sync\_test, region])

| Argument | Type | Description |
| --- | --- | --- |
| num\_players | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The number of players that must be connected for the game to start. If [rollback\_define\_player()](rollback_define_player.md) is used, this is the number of instances that are automatically created. |
| enable\_sync\_test | [Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | OPTIONAL Specifies whether Sync Test should be enabled, and is true by default. When set to false, online functionality is enabled. |
| region | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | OPTIONAL Specifies the default region where the virtual room will be created. See example at the bottom. |

 

#### Returns:

N/A

 

#### Example:

rollback\_define\_player(obj\_player);  

 var \_joined \= rollback\_join\_game();  

  

 if (!\_joined)  

 {  

     rollback\_create\_game(2, false, "Europe");  

 }
 

The above code defines a player object, and then attempts to join a game. If it was not joined, it creates a new game instead, with a maximum of 2 players and Sync Test disabled.

For an extended example, see [Create a Multiplayer Game](../Creating_Multiplayer.md).

### Getting region names

If you want to specify a default region, you will need the region strings. You can get them with an HTTP request to base API URL \+ /regions.

// Create event  

 http\_get(rollback\_api\_server \+ "/gg/regions");  

  

 // Async \- HTTP event  

 if (async\_load\[? "http\_status"] \=\= 200\)  

 {  

     var \_struct \= json\_parse(async\_load\[? "result"]);  

     var \_data \= \_struct.data;  

     var \_num\_regions \= array\_length(\_data);  

       

     global.regions \= \[];  

     for (var i \= 0; i \< \_num\_regions; i\+\+)  

     {  

         global.regions\[i] \= \_data\[i];  

     }  

 }
 

This requests the region list from GX.games, and in the **Async \- HTTP** event, iterates through the list and stores all regions in a global array.
