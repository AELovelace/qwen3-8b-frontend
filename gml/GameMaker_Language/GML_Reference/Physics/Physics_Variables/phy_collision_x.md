# phy\_collision\_x

This **read\-only** array returns the x coordinate of every point detected in a collision between two physics\-enabled instances.

 
 
 

#### Syntax:

phy\_collision\_x\[index]

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md) (single\-precision floating\-point value, or undefined if the instance doesn't have physics enabled)

 

#### Example:

Collision Event

for(var i \= 0; i \< phy\_collision\_points; i \+\= 1\)  

 {  

     part\_particles\_create(global.Sname, phy\_collision\_x\[i], phy\_collision\_y\[i], global.Spark, 5\);  

 }

The above code creates particles at all the defined points of a collision between two physics enabled instances.
