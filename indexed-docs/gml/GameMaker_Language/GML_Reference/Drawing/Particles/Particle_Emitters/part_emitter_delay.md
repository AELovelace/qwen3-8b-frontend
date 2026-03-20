# part\_emitter\_delay

This function sets the delay before the particle emitter creates particles for the first time when it is in stream mode.

The value for the delay is chosen to be a random value between delay\_min and delay\_max.

 
 

#### Syntax:

part\_emitter\_delay(ps, ind, delay\_min, delay\_max, delay\_unit)

| Argument | Type | Description |
| --- | --- | --- |
| ps | [Particle System Instance](GameMaker_Language/GML_Reference/Drawing/Particles/Particle_Systems/part_system_create.md) | The index of the particle system containing the emitter |
| ind | [Particle Emitter ID](GameMaker_Language/GML_Reference/Drawing/Particles/Particle_Emitters/part_emitter_create.md) | The emitter index |
| delay\_min | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The minimum possible value for the delay, expressed in delay\_unit |
| delay\_max | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The maximum possible value for the delay, expressed in delay\_unit |
| delay\_unit | [Time Source Unit Constant](GameMaker_Language/GML_Reference/Time_Sources/Time_Source_Units.md) | The unit in which delay\_min and delay\_max are expressed |

 

#### Returns:

N/A

 

#### Example:
