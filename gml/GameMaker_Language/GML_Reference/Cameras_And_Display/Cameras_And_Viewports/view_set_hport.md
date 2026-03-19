# view\_set\_hport

This function sets the height of the given viewport. You give the viewport index (from 0 to 7\) and the new height to use.

 

#### Syntax:

view\_set\_hport(viewport, h)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |
| h | [Real](../../../GML_Overview/Data_Types.md) | The new height (in pixels) |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (view\_get\_hport(0\) !\= (display\_get\_height () / 2\))  

 {  

     view\_set\_hport(0, display\_get\_height() / 2\);  

 }

The above code will check the height of the viewport\[0] and if it is not half of the display height it is set to that value.
