# physics\_particle\_get\_damping

With this function you can find out what the current linear damping is for particles in the physics simulation (you can set this value using [physics\_particle\_set\_damping()](physics_particle_set_damping.md)).

 

#### Syntax:

physics\_particle\_get\_damping()

 

#### Returns:

 

#### Example:

if (physics\_particle\_get\_damping() \< 1\)  

 {  

     physics\_particle\_set\_damping(physics\_particle\_get\_damping() \+ 0\.01\);  

 }

The above code will check the current damping value for all particles in the system and if it is less than 1 then it will add 0\.01 to it.
