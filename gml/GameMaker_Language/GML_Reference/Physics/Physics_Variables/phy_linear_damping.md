# phy\_linear\_damping

This variable can be used to set the linear damping of the instance, or it can be used to get the current linear damping. The damping is the amount of "resistance" to forward movement that the physics enabled instance has, with a lower value permitting the instance to move and accelerate faster and a higher value making it require a more forceful push

 

#### Syntax:

phy\_linear\_damping

 

#### Returns:

 (single precision floating point value, or undefined if the instance is not physics enabled)

 

#### Example:

if (place\_meeting(phy\_position\_x, phy\_position\_y, obj\_Water))   

 {  

     phy\_linear\_damping \= 10;  

 }  

 else  

 {  

     phy\_linear\_damping \= 3;  

 }

The above code will check for a collision between the calling instance and instances of "obj\_Water" and change the linear damping accordingly.
