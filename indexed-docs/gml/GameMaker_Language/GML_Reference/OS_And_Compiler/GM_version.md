# GM\_version

This constant hold the version number as defined in the [Game Options](../../../Settings/Game_Options.md) for each target platform. The value is stored as a string.

 

#### Syntax:

GM\_version

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

draw\_text(32, 32, date\_time\_string(GM\_build\_date));  

 draw\_text(32, 64, "v" \+ GM\_version);

The above code takes the GM date and version constants and draws them to the screen.
