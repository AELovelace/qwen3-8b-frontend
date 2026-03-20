# ceil

This function takes any real number and rounds it up to the nearest integer.

Care should be taken with this function as one common mistake is to use it to round up a random value and expect it always to be greater than 1, i.e.:

int \= ceil(random(5\));

Now, you would expect this code to *always* give an integer between 1 and 5, but this may not always be the case as there is a very small possibility that the random function will return 0, and rounding up 0 still gives you 0\. This is a remote possibility but should be taken into account when using this function.

 

#### Syntax:

ceil(val)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The number to change |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

val \= ceil( 3\.4 );

This will set val to 4\.
