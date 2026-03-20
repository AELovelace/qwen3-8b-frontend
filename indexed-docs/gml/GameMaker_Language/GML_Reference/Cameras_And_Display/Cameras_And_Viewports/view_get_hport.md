# view\_get\_hport

This function can be used to retrieve the height of the given viewport.

 

#### Syntax:

view\_get\_hport(viewport)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (view\_get\_hport(0\) !\= (display\_get\_height () / 2\))  

 {  

     view\_set\_hport(0, display\_get\_height() / 2\);  

 }

The above code will check the height of the viewport\[0] and if it is not half of the display height it is set to that value.
