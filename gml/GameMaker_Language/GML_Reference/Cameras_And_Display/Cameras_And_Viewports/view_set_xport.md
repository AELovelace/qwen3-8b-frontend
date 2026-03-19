# view\_set\_xport

This function sets the x position of the given viewport. You give the viewport index (from 0 to 7\) and the new position to place it at.

 

#### Syntax:

view\_set\_xport(viewport, x)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |
| x | [Real](../../../GML_Overview/Data_Types.md) | The new x position |

 

#### Returns:

N/A

 

#### Example:

if view\_get\_xport(0\) !\= (display\_get\_width() / 2\) \- (view\_wport\[0] / 2\)  

 {  

     view\_set\_xport(0, (display\_get\_width() / 2\) \- (view\_wport\[0] / 2\));  

 }

The above code will check the x position of the viewport\[0] and if it is not where it is required to be it is set to that position.
