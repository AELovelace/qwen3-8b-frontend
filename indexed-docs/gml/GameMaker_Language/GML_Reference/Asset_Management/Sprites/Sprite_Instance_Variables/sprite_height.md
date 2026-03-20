# sprite\_height

This **read only** variable returns the height of the sprite that has been assigned to the instance. This height is returned in pixels and will be dependent on the [image\_yscale](image_yscale.md). If you need the un\-scaled height you should use [sprite\_get\_height()](../Sprite_Information/sprite_get_height.md).

 

#### Syntax:

sprite\_height

 

#### Returns:

Real

 

#### Example:

if (sprite\_height !\= sprite\_get\_height(sprite\_index))   

 {  

     image\_yscale \= 1;  

 }

The above code checks the height of the sprite assigned to the instance running the code against the height of the sprite resource and if it is not the same, it resets the image\_yscale to 1,
