# physics\_particle\_set\_max\_count

This function will set the total permitted number of particles in a physics simulation. If you set this value to 0, then there is no cap the particles created, and setting it to any other value will stop any further particles being created when the
 total number of particles is equal to the value. Note that the *minimum* number of particles you can create in a simulation is 128, so setting this value any lower will have no effect (unless set to 0\).

 

#### Syntax:

physics\_particle\_set\_max\_count(count)

| Argument | Type | Description |
| --- | --- | --- |
| count |  | The maximum number of particles to permit. |

 

#### Returns:

 

#### Example:

physics\_particle\_set\_max\_count(500\);

The above code will set the particle cap of the physics simulation to 500\.
