# physics\_fixture\_set\_circle\_shape

This function defines a circle shape for your fixture with a radius defined by the argument "rad".

 

#### Syntax:

physics\_fixture\_set\_circle\_shape(fixture, rad)

| Argument | Type | Description |
| --- | --- | --- |
| fixture |  | the index of the fixture |
| rad |  | radius of the circle |

 

#### Returns:

 

#### Example:

physics\_fixture\_set\_circle\_shape(fix\_Ball, sprite\_get\_width(spr\_Ball) / 2\);

The code above will apply a circle shape to the fixture indexed in the variable "fix\_Ball" with a radius the same as that of the width of the sprite "spr\_Ball" divided by 2\.
