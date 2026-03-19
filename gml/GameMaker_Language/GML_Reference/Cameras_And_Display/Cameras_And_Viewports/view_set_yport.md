# view\_set\_yport

This function sets the y position of the given viewport. You give the viewport index (from 0 to 7\) and the new position to place it at.

 

#### Syntax:

view\_set\_yport(viewport, y)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |
| y | [Real](../../../GML_Overview/Data_Types.md) | The new y position |

 

#### Returns:

N/A

 

#### Example:

if view\_get\_yport(0\) !\= (display\_get\_height() / 2\) \- (view\_hport\[0] / 2\)  

 {  

     view\_set\_yport(0, (display\_get\_height() / 2\) \- (view\_hport\[0] / 2\));  

 }

The above code will check the y position of the viewport\[0] and if it is not where it is required to be it is set to that position.
