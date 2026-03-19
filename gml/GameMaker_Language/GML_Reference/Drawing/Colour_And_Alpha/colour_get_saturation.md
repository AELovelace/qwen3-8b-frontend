# colour\_get\_saturation

This function will return the saturation of the given colour. This is the amount of the colour tone that is mixed into the final colour and is part of the hue, saturation and value (luminosity) method for defining a colour. The following image illustrates
 how this value corresponds to the HSV scale of colour:

 

#### Syntax:

colour\_get\_saturation(col)

| Argument | Type | Description |
| --- | --- | --- |
| col |  | The colour to check |

 

#### Returns:

 

#### Example:

col \= make\_colour\_hsv(random(255\), colour\_get\_sat(c\_teal), 255\);

The above code gets the saturation used to make the colour constant "c\_teal" and then uses that value to set a random colour to have the same saturation, storing the resulting colour in the variable "col".
