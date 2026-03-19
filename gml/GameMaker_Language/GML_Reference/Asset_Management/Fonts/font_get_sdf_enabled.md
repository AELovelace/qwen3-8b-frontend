# font\_get\_sdf\_enabled

This function returns whether [SDF Rendering](Fonts.md#h) is enabled for the given font or not.

 

#### Syntax:

font\_get\_sdf\_enabled(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Font Asset](The_Asset_Editors/Fonts.md) | The index of the font to check |

 

#### Returns:

[Boolean](GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_sdf\_enabled \= font\_get\_sdf\_enabled(fnt\_title);  

 show\_debug\_message("SDF rendering is {0} enabled for fnt\_title", \_sdf\_enabled ? "" : "not");

The above code checks if SDF rendering is enabled for the font fnt\_title and stores the value in a variable \_sdf\_enabled. It then shows a readable debug message showing the result.
