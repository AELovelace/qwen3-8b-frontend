# view\_get\_yport

This function returns the y position of the given viewport.

 

#### Syntax:

view\_get\_yport(viewport)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if view\_get\_yport(0\) !\= (display\_get\_height() / 2\) \- (view\_hport\[0] / 2\)  

 {  

     view\_set\_yport(0, (display\_get\_height() / 2\) \- (view\_hport\[0] / 2\));  

 }

The above code will check the y position of the viewport\[0] and if it is not where it is required to be it is set to that position.
