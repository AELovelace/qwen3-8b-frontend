# animcurve\_exists

This function returns if the given [Animation Curve Asset](../../../../The_Asset_Editors/Animation_Curves.md) or [Animation Curve Struct](animcurve_get.md) exists and is a valid Animation Curve.

 

#### Syntax:

animcurve\_exists(curve\_struct\_or\_id)

| Argument | Type | Description |
| --- | --- | --- |
| curve\_struct\_or\_id | [Animation Curve Struct](animcurve_get.md) or [Animation Curve Asset](../../../../The_Asset_Editors/Animation_Curves.md) | The Animation Curve asset or struct that will be checked |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (animcurve\_exists(spring\_curve))  

 {  

     apply\_spring\_animation(sprite\_curve);  

 }

The above code checks if the Animation Curve stored in the custom spring\_curve variable exists. If it does, it runs a custom method to use that Animation Curve.
