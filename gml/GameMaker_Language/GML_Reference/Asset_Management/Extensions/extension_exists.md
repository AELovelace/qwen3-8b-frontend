# extension\_exists

This function tells whether an extension with the given name exists (true) or not (false).

 

#### Syntax:

extension\_exists(extension\_name)

| Argument | Type | Description |
| --- | --- | --- |
| extension\_name | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of your extension asset as a string |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (extension\_exists("MyExtension"))  

 {  

     var \_options \= extension\_get\_options("MyExtension");  

     var \_enabled \= \_options.enabled;  

 }

This code checks if the MyExtension extension exists, and if it does, gets its options as a struct, and reads a value from it.
