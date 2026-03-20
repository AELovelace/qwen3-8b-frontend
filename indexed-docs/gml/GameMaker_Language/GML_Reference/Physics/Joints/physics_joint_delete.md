# physics\_joint\_delete

This function deletes the given physics joint.

Once two instances with physics representations have been bound by a joint, this can be deleted again at any time. Normally this will happen automatically when one of the two instances is destroyed, or when the room ends, but there are times when you may wish to do this manually using this function.

It should also be noted that whenever an instance that is part of a [gear joint](physics_joint_gear_create.md "physics_joint_gear_create()") is destroyed, the gear joint should be deleted using this function *before* any of the instances involved in forming the gear (but the remaining joints will be deleted automatically), for example in the Destroy event of the instance.

 

#### Syntax:

physics\_joint\_delete(joint)

| Argument | Type | Description |
| --- | --- | --- |
| joint | [Physics Joint ID](Joints.md) | The index of the joint that you wish to delete |

 

#### Returns:

N/A

 

#### Example:

var \_reaction\_force\_x, \_reaction\_force\_y, \_reaction\_force;  

 if (ship\_joint)  

 {  

     \_reaction\_force\_x \= physics\_joint\_get\_value(ship\_joint, phy\_joint\_reaction\_force\_x);  

     \_reaction\_force\_y \= physics\_joint\_get\_value(ship\_joint, phy\_joint\_reaction\_force\_y);  

     \_reaction\_force \= sqrt((\_reaction\_force\_x \+ \_reaction\_force\_x) \+ (\_reaction\_force\_y \+ \_reaction\_force\_y));  

     if (\_reaction\_force \> 2\)  

     {  

         physics\_joint\_delete(ship\_joint);  

         ship\_joint \= \-1;  

     }  

 }

The above code checks to see if the variable ship\_joint holds a valid joint index and if it does, it then calculates the force being applied to that joint using the two constants. Finally, if the total force is greater than 2, the joint is deleted.
