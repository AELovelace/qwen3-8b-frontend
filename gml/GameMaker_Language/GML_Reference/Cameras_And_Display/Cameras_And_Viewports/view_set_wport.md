# view\_set\_wport

This function sets the width of the given viewport. You give the viewport index (from 0 to 7\) and the new width to use.

 

#### Syntax:

view\_set\_wport(viewport, w)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |
| w | [Real](../../../GML_Overview/Data_Types.md) | The new width (in pixels) |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (view\_get\_wport(0\) !\= (display\_get\_width () / 2\))  

 {  

     view\_set\_wport(0, display\_get\_width() / 2\);  

 }

The above code will check the width of the viewport\[0] and if it is not half of the display width it is set to that value.
