# collision\_space

This **built\-in read\-only** variable returns the collision space that the instance is in. This will be one of the following enum members:

 
This affects the collision checks done within the instance, as an instance can only collide with instances in the same space. This also affects the default behaviour of the [instance deactivation](../Deactivating_Instances/Deactivating_Instances.md) functions as by default they will only activate/deactivate instances in the same space, however that can be changed in each function call.

 

#### Syntax:

collision\_space

 

#### Returns:

[Collision Space](collision_space.md)

 

#### Example:

instance\_activate\_all(collision\_space);

The above code will activate all deactivated instances that are placed within the same collision space as the calling instance.
