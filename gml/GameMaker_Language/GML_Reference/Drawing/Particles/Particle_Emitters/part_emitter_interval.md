# part\_emitter\_interval

This function sets the interval between two consecutive bursts for the given emitter in case it is working in stream mode.

Every time the interval timer times out, i.e. after every burst, a new value for the interval is chosen as a random value between interval\_min and interval\_max.

 
 

#### Syntax:

part\_emitter\_interval(ps, ind, interval\_min, interval\_max, interval\_unit)

| Argument | Type | Description |
| --- | --- | --- |
| ps | [Particle System Instance](GameMaker_Language/GML_Reference/Drawing/Particles/Particle_Systems/part_system_create.md) | The index of the particle system the emitter is in |
| ind | [Particle Emitter ID](GameMaker_Language/GML_Reference/Drawing/Particles/Particle_Emitters/part_emitter_create.md) | The index of the particle emitter |
| interval\_min | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The minimum possible value for the interval, expressed in interval\_unit |
| interval\_max | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The maximum possible value for the interval, expressed in interval\_unit |
| interval\_unit | [Time Source Unit Constant](GameMaker_Language/GML_Reference/Time_Sources/Time_Source_Units.md) | The unit in which the interval values are expressed |

 

#### Returns:

N/A

 

#### Example:
