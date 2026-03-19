# view\_get\_visible

This function can be used to check the visibility of the given viewport. The function will return true if it is visible, false if not.

 

#### Syntax:

view\_get\_visible(viewport)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!view\_get\_visible(0\))  

 {  

     view\_set\_visible(0, true);  

 }

The above code will check to see if the viewport\[0] is visible and if it is not it is set to visible.
