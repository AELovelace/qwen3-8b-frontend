# GM\_runtime\_version

This constant hold the runtime version number as defined in the [Runtime Feeds Preferences](../../../Setting_Up_And_Version_Information/IDE_Preferences/Runtime_Feed_Preferences.md) as the runtime being used to build the project.

 

#### Syntax:

GM\_runtime\_version

 

#### Holds:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

draw\_text(32, 32, date\_time\_string(GM\_build\_date));  

 draw\_text(32, 64, "v" \+ GM\_version);  

 draw\_text(32, 96, "Runtime " \+ GM\_runtime\_version);

The above code takes the GM date, version and runtime constants and draws them to the screen.
