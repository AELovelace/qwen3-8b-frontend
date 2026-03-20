# phy\_collision\_points

This **read\-only** variable returns the number of points of collision detected between the two instances in the collision.

The number returned by this function is the number of items in the built\-in [phy\_collision\_x](phy_collision_x.md), [phy\_collision\_y](phy_collision_y.md), [phy\_col\_normal\_x](phy_col_normal_x.md) and [phy\_col\_normal\_y](phy_col_normal_y.md) arrays in the current collision event.

 
 

#### Syntax:

phy\_collision\_points

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md) (integer value, or undefined if the instance doesn't have physics enabled)

 

#### Example:

Collision Event

for(var i \= 0; i \< phy\_collision\_points; i \+\= 1\)  

 {  

     part\_particles\_create(global.Sname, phy\_collision\_x\[i], phy\_collision\_y\[i], global.Spark, 5\);  

 }

The above code creates particles at all the defined points of a collision between two physics\-enabled instances.
