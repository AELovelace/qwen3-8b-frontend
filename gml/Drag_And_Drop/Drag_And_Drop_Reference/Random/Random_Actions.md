# Random Action Library

The **Random** library has the following actions for dealing with random number generation and chance operations:

|  | [Get Random Number](Get_Random_Number.md) |
| --- | --- |
|  | [Randomise](Randomise.md) |
|  | [Choose](Choose.md) |

It is worth noting that GameMaker will use the same seed when generating random numbers each time you run the game from the IDE. This is to facilitate debugging and means that you will get the same initial results when generating random values, but this will *not* occur when you have compiled the game into an executable (a new seed will be generated each time the game is run). If you do not wish this behaviour when testing, then you should call the [Randomise](Randomise.md) action once at the start of the game, before generating any random values.
