# part\_type\_scale

This function sets the horizontal and vertical scale of the particle before any other size changes are made. It works on the ratio of the sprite size, so a value of 1 (the default value) is a 1:1 ratio, meaning that 0\.5 would be half and 2 double.

 

#### Syntax:

part\_type\_scale(ind, xscale, yscale)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle Type ID](part_type_create.md) | The index of the particle type to change. |
| xscale | [Real](../../../../GML_Overview/Data_Types.md) | The horizontal scaling of the base particle. |
| yscale | [Real](../../../../GML_Overview/Data_Types.md) | The vertical scaling of the base particle. |

 

#### Returns:

N/A

 

#### Example:

part\_type\_shape(particle1, pt\_shape\_flare);  

 part\_type\_size(particle1, 2, 2, 0\.10, 1\);  

 part\_type\_scale(particle1, 8, 0\.50\);  

 part\_type\_colour3(particle1, 8388608, 4227327, 8454143\);  

 part\_type\_alpha3(particle1, 0\.10, 0\.10, 0\);  

 part\_type\_speed(particle1, 0, 1, 0\.18, 20\);  

 part\_type\_direction(particle1, 0, 359, 0, 0\);  

 part\_type\_orientation(particle1, 0, 0, 0, 0, 1\);  

 part\_type\_blend(particle1, 1\);  

 part\_type\_life(particle1, 10, 40\);

The above code will set various particle values including the scale which sets the xscale to eight times the size and the yscale to half the size.
