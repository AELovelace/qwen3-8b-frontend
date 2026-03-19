# view\_get\_surface\_id

This function can be used to retrieve the unique ID value for the surface assigned to the given viewport.

It returns an invalid handle (\-1) if no surface has been assigned.

 

#### Syntax:

view\_get\_surface\_id(viewport)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |

 

#### Returns:

[Surface](../../Drawing/Surfaces/surface_create.md)

 

#### Example:

if (view\_get\_surface\_id(0\) \=\= \-1\)  

 {  

     view\_set\_surface\_id(0, global.vSurf);  

 }

The above code will check to see if a surface has been assigned to the viewport\[0] and if it has not then one is assigned.
