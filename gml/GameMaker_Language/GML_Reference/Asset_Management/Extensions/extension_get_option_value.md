# extension\_get\_option\_value

This function returns the value of the given [option](../../../../The_Asset_Editors/Extension_Creation/Creating_An_Extension.md#h1) in the extension with the given name.

The function will return undefined if the provided extension name is invalid.

 

#### Syntax:

extension\_get\_option\_value(extension\_name, option\_name)

| Argument | Type | Description |
| --- | --- | --- |
| extension\_name | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of your extension asset as a string |
| option\_name | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of the option to read |

 

#### Returns:

[Any](../../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable)

 

#### Example:

var \_enabled \= extension\_get\_option\_value("MyExtension", "enabled");

This code gets the value of the enabled option in the MyExtension extension.
