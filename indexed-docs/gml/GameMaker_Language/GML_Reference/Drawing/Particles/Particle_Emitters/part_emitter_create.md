# part\_emitter\_create

This function creates a new particle emitter in the given particle system.

The function will return the handle for the new emitter which must be stored in a variable and used in all further functions that reference the emitter, and the emitter itself must be destroyed when no longer used to prevent memory leaks (this can be achieved using the specific emitter destroy functions ([part\_emitter\_destroy](part_emitter_destroy.md)/[part\_emitter\_destroy\_all](part_emitter_destroy_all.md)) or by destroying the whole particle system that the emitter belongs to ([part\_system\_destroy](../Particle_Systems/part_system_destroy.md))).

  Emitter IDs returned by this function are reused, e.g. if you first create three particle emitters they will have IDs 0, 1 and 2 assigned. If you then destroy the second emitter (which got an ID of 1\) using [part\_emitter\_destroy](part_emitter_destroy.md) and then create another emitter, then this emitter will reuse the ID of 1\. Since emitter ID 2 is in use, the next emitter will get an ID of 3, and so on.

#### Syntax:

part\_emitter\_create(ps)

| Argument | Type | Description |
| --- | --- | --- |
| ps | [Particle System Instance](../Particle_Systems/part_system_create.md) | The particle system to create the emitter in. |

 

#### Returns:

[Particle Emitter](part_emitter_create.md)

 

#### Example 1: Basic Use

p\_emit \= part\_emitter\_create(Sname);

This will create a new particle emitter in an existing particle system stored in Sname and store its handle in the variable p\_emit.

 

#### Example 2: Adding an Additional Emitter to a Particle System Created From an Asset

ps \= part\_system\_create(ps\_effects);  

 pe \= part\_emitter\_create(ps);  

 part\_emitter\_region(ps, pe, 0, 100, 0, 100, ps\_shape\_ellipse, ps\_distr\_gaussian);  

 part\_emitter\_stream(ps, pe, pt\_smoke, 2\);

The code above first creates a particle system instance and initialises it with emitters as set up in an existing particle system asset ps\_effects. It then adds an additional emitter to the particle system instance, sets the region in which the emitter will emit particles and finally sets the emitter to stream two particles of type pt\_smoke every step.
