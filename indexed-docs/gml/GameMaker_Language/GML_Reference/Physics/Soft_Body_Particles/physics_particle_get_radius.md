# physics\_particle\_get\_radius

With this function you can find out what the current radius (in pixels) is for particles in the physics simulation (you can set this value using [physics\_particle\_set\_radius()](physics_particle_set_radius.md)).

 

#### Syntax:

physics\_particle\_get\_radius()

 

#### Returns:

 

#### Example:

if (physics\_particle\_get\_radius() \< 32\)  

 {  

     physics\_particle\_set\_radius(physics\_particle\_get\_radius() \+ 1\);  

 }

The above code will check the current radius of the particles in the simulation and if it is less than 32, then it will increase their size by 1\.
