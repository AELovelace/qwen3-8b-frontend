# sprite\_get\_height

With this function you can find the height of the base sprite asset, with no transforms, in pixels.

 

#### Syntax:

sprite\_get\_height(index)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The index of the sprite to find the height of. |

 

#### Returns

 

#### Example:

if (sprite\_height !\= sprite\_get\_height(sprite\_index))   

 {  

     image\_yscale \= 1;  

 }

The above code checks the height of the sprite as it is in the current instance and if there is a difference between that and the original base sprite, it resets the y axis scale.
