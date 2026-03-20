# path\_endaction

This built\-in variable can be used to get or to change the reaction of an instance when it reaches the end of the current path. Normally you would set this when you start the path using [path\_start](../path_start.md) but you may wish to change this behaviour depending on any number of events in your game. The available values are expressed using the following constants:

| [Path End Action Constant](path_endaction.md) | |
| --- | --- |
| Constant | Description |
| path\_action\_stop | Stop the path |
| path\_action\_restart | Continue from start position, jumping to the start if the path is not closed |
| path\_action\_continue | Start the path again from the current position |
| path\_action\_reverse | Reverse the speed of the path (run the path in reverse) |

 

#### Syntax:

path\_endaction

 

#### Returns:

[Path End Action Constant](path_endaction.md)

 

#### Example:

if (path\_endaction \=\= path\_action\_stop)  

 {  

     path\_endaction \= path\_action\_reverse;  

 }

The above code will check the path end action and if it's set to stop, then the end action will be changed to reverse.
