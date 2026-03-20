# GM\_runtime\_type

This built\-in constant holds the type of the runtime: "gms2" for the current runtime or "gmrt" for the new runtime.

  See [GMRT (GameMaker Runtime)](../../../Settings/Runner_Details/GMRT_(GameMaker_Runtime).md) for more information about the new runtime.

 

#### Syntax:

GM\_runtime\_type

 

#### Holds:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

show\_debug\_message($"Using runtime: {string\_upper(GM\_runtime\_type)}");

The above code outputs a debug message that shows the runtime the game is using.
