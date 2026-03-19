# animcurve\_channel\_new

This function creates a new animation curve channel [struct](../../../GML_Overview/Structs.md).

A channel struct has the following variables:

 
 

Animation Curve Interpolation Type Constant

| Constant | Description |
| --- | --- |
| **animcurvetype\_linear** | Used for linear interpolation between points. |
| **animcurvetype\_catmullrom** | Used for smooth interpolation between points using Catmull\-Rom interpolation. |
| **animcurvetype\_bezier** | Used for Bezier interpolation between points. |

  

 By default, when you create a new channel struct, the name variable will be an empty string, the type will be animcurvetype\_linear and the iterations will be 16\. All these variables can be set to the values that you require (note that the iterations value has no effect on linear curve types). Once created you need to add points to the curve, which is done by adding different point structs to the points [array](../../../GML_Overview/Arrays.md). These point structs can be created using the function [animcurve\_point\_new](animcurve_point_new.md).

 

#### Syntax:

animcurve\_channel\_new()

 

#### Returns:

[Animation Curve Channel Struct](animcurve_get_channel.md)

 

#### Example:

my\_curve \= animcurve\_create();  

 my\_curve.name \= "My\_Curve";  

 var \_channels \= array\_create(1\);  

 \_channels\[0] \= animcurve\_channel\_new();  

 \_channels\[0].name \= "alpha";  

 \_channels\[0].type \= animcurvetype\_catmullrom;  

 \_channels\[0].iterations \= 8;  

 var \_points \= array\_create(3\);  

 \_points\[0] \= animcurve\_point\_new();  

 \_points\[0].posx \= 0;  

 \_points\[0].value \= 0;  

 \_points\[1] \= animcurve\_point\_new();  

 \_points\[1].posx \= 0\.5;  

 \_points\[1].value \= 1;  

 \_points\[2] \= animcurve\_point\_new();  

 \_points\[2].posx \= 1;  

 \_points\[2].value \= 0;  

 \_channels\[0].points \= \_points;  

 my\_curve.channels \= \_channels;

The above code creates a new animation curve struct and stores it in the variable my\_curve. This struct is then populated with a name and a channel array. The channel array contains a single channel with three points.
