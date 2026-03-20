# part\_type\_colour\_rgb

This function sets the mix of red, green and blue colours for all newly created particles of the given type.

You supply a minimum value and a maximum value for each of the three components and the particles created will have a random colour based on the given range of parameters. All values must be between 0 and 255\.

 
 

#### Syntax:

part\_type\_colour\_rgb(ind, rmin, rmax, gmin, gmax, bmin, bmax)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle Type ID](part_type_create.md) | The index of the particle type to change. |
| rmin | [Real](../../../../GML_Overview/Data_Types.md) | The minimum value the final colour's red component can have. |
| rmax | [Real](../../../../GML_Overview/Data_Types.md) | The maximum value the final colour's red component can have. |
| gmin | [Real](../../../../GML_Overview/Data_Types.md) | The minimum value the final colour's green component can have. |
| gmax | [Real](../../../../GML_Overview/Data_Types.md) | The maximum value the final colour's green component can have. |
| bmin | [Real](../../../../GML_Overview/Data_Types.md) | The minimum value the final colour's blue component can have. |
| bmax | [Real](../../../../GML_Overview/Data_Types.md) | The maximum value the final colour's blue component can have. |

 

#### Returns:

N/A

 

#### Example:

part\_type\_colour\_rgb(global.Blood\_Part, 0, 255, 0, 0, 0, 0\);

The above code sets each particle emitted of the particle type indexed in the global variable Blood\_Part to be only different shades of red.
