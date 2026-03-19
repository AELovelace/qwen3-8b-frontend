# phy\_fixed\_rotation

This variable can be used to set whether or not the instance can be affected by rotational forces (default is false). If this is set to true, no external force (either from coded impulses or forces, or from collisions) will affect
 the rotation value of the instance and this would have to be set manually using the [phy\_rotation](phy_rotation.md) variable

 

#### Syntax:

phy\_fixed\_rotation

 

#### Returns:

 (or undefined if the instance is not physics enabled)

 

#### Example:

phy\_rotation \= 0;  
 phy\_fixed\_rotation \= true;

The above code will switch the instance to have a fixed rotation, then set the rotation angle.
