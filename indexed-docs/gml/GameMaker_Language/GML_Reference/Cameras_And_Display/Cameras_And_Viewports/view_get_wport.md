# view\_get\_wport

This function returns the width of the given viewport.

 

#### Syntax:

view\_get\_wport(viewport)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (view\_get\_wport(0\) !\= (display\_get\_width () / 2\))  

 {  

     view\_set\_wport(0, display\_get\_width() / 2\);  

 }

The above code will check the width of the viewport\[0] and if it is not half of the display width it is set to that value.
