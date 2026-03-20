# colour\_get\_value

This function will return the value (luminosity) of the given colour. This is the amount of the "light" that is mixed into the final colour and is part of the hue, saturation and value method for defining a colour. The following image illustrates
 how this value corresponds to the HSV scale of colour:

 

#### Syntax:

colour\_get\_value(col)

| Argument | Type | Description |
| --- | --- | --- |
| col |  | The colour to check |

 

#### Returns:

 

#### Example:

col \= make\_colour\_hsv(random(255\), 255, colour\_get\_value(c\_teal));

The above code gets the value used to make the colour constant "c\_teal" and then uses that value to set a random colour to have the same luminosity, storing the resulting colour in the variable "col".
