# view\_get\_xport

This function returns the x position of the given viewport.

 

#### Syntax:

view\_get\_xport(viewport)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if view\_get\_xport(0\) !\= (display\_get\_width() / 2\) \- (view\_wport\[0] / 2\)  

 {  

     view\_set\_xport(0, (display\_get\_width() / 2\) \- (view\_wport\[0] / 2\));  

 }

The above code will check the x position of the viewport\[0] and if it is not where it is required to be it is set to that position.
