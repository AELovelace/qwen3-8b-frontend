# physics\_particle\_get\_max\_count

With this function you can find out what the current cap value is on particles permitted in the physics simulation (you can set this value using [physics\_particle\_set\_max\_count()](physics_particle_set_max_count.md)).

 

#### Syntax:

physics\_particle\_get\_max\_count()

 

#### Returns:

 

#### Example:

if (physics\_particle\_count() \< physics\_particle\_get\_max\_count())  

 {  

     physics\_particle\_create(0, x, y, 0, 0, c\_white, 1, 1\)  

 }

The above code will check to see if there are less than the maximum number of permitted particles in the room, and if so create one more.
