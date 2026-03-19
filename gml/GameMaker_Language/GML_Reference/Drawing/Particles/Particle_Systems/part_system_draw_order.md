# part\_system\_draw\_order

With this function you can set the order in which particles in the given particle system are drawn when created on the screen, either old to new or new to old.

The default system uses an old \> new look (the function is set to true), where old particles are drawn at a higher depth than newer ones and so appear "beneath" them new particles, but by setting this function to false you can reverse this order and have the new particles drawn higher and so appear "beneath" the older ones. The images below illustrate this, with the image on the left being the default value of true and the image on the right being false:

 
  When the particles are being drawn with an additive blend mode, the effect of this function may not always be obvious.

 

#### Syntax:

part\_system\_draw\_order(ind, oldtonew)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system to change. |
| oldtonew | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether old particles should be drawn behind newer ones (true) or vice versa (false). |

 

#### Returns:

N/A

 

#### Example:

mysystem \= part\_system\_create();  

part\_system\_draw\_order(mysystem, true);
 

This will create a new particle system with the index mysystem, and then it sets particles to draw newer particles atop older ones.
