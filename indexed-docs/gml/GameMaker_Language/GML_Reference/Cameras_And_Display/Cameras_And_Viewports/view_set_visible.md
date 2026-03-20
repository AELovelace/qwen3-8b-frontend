# view\_set\_visible

This function sets the visibility of the given viewport. The function takes the viewport index (from 0 to 7\) and a boolean true if it is visible and false if it is not.

 

#### Syntax:

view\_set\_visible(viewport, visible)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |
| visible | [Boolean](../../../GML_Overview/Data_Types.md) | Visibility toggle (true is visible and false is invisible) |

 

#### Returns:

N/A

 

#### Example:

if (!view\_get\_visible(0\))  

 {  

     view\_set\_visible(0, true);  

 }

The above code will check to see if the viewport\[0] is visible and if it is not it is set to visible.
