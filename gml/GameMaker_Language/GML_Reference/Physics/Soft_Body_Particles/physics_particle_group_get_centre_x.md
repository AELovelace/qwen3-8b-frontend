# physics\_particle\_group\_get\_centre\_x

With this function you can retrieve the x component of the center of mass of an entire group of particles. The group value is that which was returned when you created the group of particles using the function [physics\_particle\_group\_end()](physics_particle_group_end.md),
 and the function will return a value which is the combined value of the currently set flags.

 

#### Syntax:

physics\_particle\_group\_get\_centre\_x(group)

| Argument | Type | Description |
| --- | --- | --- |
| group |  | The particle group to get. |

 

#### Returns:

 

#### Example:

xx \= physics\_particle\_group\_get\_centre\_x(group1\);  
 yy \= physics\_particle\_group\_get\_centre\_y(group1\);

The above code will get the x and y position for the center of mass of the particle group indexed in the variable "group1" and store them in variables.
