# environment\_get\_variable

This function returns the value (a string) of the environment variable with the given name (also a string). When the specified environment variable is not found, the function returns an empty string "".

You can get the available environment variables on macOS and Ubuntu (Linux) by typing "env" into the terminal app, and for information on Windows environment variables, if you are using the command prompt then type "set", and using PowerShell it's "ls env:". Note that on both macOS and Ubuntu (Linux) the "HOME" environment variable will return the "\~/" path which maps to "/Users/\" on macOS and "/home/\" on Ubuntu (Linux).

  This function is for Windows, macOS and Ubuntu (Linux) only.

 

#### Syntax:

environment\_get\_variable(name)

| Argument | Type | Description |
| --- | --- | --- |
| name | [String](../../GML_Overview/Data_Types.md) | The name of the environment variable to check |

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

e\_str \= environment\_get\_variable("APPDATA");

The above code will return the full path for the environment variable "%appdata%", which is normally "C:\\Users\\{username}\\AppData\\Roaming".
