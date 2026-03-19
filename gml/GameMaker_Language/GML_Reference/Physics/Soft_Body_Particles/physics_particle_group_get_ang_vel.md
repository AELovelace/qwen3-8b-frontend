# physics\_particle\_group\_get\_ang\_vel

With this function you can retrieve the angular velocity of a group of particles. The group value is that which was returned when you created the group of particles using the function [physics\_particle\_group\_end()](physics_particle_group_end.md),
 and the function will return a value which is the combined value of the currently set flags.

 

#### Syntax:

physics\_particle\_group\_get\_ang\_vel(group)

| Argument | Type | Description |
| --- | --- | --- |
| group |  | The particle group to get. |

 

#### Returns:

 

#### Example:

ang\_v \= physics\_particle\_group\_get\_ang\_vel(group1\);

The above code will get the angular velocity of the particle group indexed in the variable "group1" and store it in a variable.
