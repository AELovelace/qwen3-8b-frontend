# sprite\_get\_number

A sprite has to have at least one sub\-image and this function will return just how many it has. Remember, a sprite sub\-image starts being numbered from 0, so if this function returns 3 (the sprite being checked has 3 sub\-images) they will be numbered
 0, 1 and 2\.

 

#### Syntax:

sprite\_get\_number(index)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The index of the sprite. |

 

#### Returns

 

#### Example:

image\_index \= floor(random(sprite\_get\_number(sprite\_index)));

The above code will set the image index to a random frame based on the number of sub\-images that the sprite has.
