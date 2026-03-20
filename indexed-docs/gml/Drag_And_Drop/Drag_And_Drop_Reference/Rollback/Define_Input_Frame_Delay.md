# title

This action defines the fixed frame delay for local player inputs.

By default, your game will use an adaptive input delay, which is based on the latency between players. This will work for almost every game out there, however, some specific types of games (e.g. fighting games) may prefer to use a fixed input delay, instead of an adaptive delay that may change at any time.

It's not recommended to change this unless you know exactly what you're doing.

The delay value specified must be in number of frames. If you specify \-1, the game will revert to using an adaptive delay. The maximum delay you can set is **10 frames**.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Delay | The delay value to use |
