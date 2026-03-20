# phy\_mass

This **read\-only** variable returns the mass of the instance in *kilograms*. This value is calculated automatically based on the surface area of the assigned fixtures and their density values, but it can be changed using the function [physics\_mass\_properties()](../physics_mass_properties.md).

 

#### Syntax:

phy\_mass

 

#### Returns:

 (single precision floating point value, or undefined if the instance is not physics enabled)

 

#### Example:

if (phy\_mass \< other.phy\_mass)  

 {  

     instance\_destroy();  

 }

The above code is from the collision event of the instance with another and it compares the mass of each instance and destroys that which has less mass.
