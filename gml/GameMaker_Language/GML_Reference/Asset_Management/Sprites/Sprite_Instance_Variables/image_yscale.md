# image\_yscale

This value sets the vertical scaling (along the y\-axis) applied to the sprite that has been assigned to the current instance. A scale of 1 indicates no scaling (1:1\), smaller values will scale down (0\.5, for example, will half the height of the sprite), larger values will scale up and negative values will mirror the sprite *and* scale it unless the value used is exactly \-1 (in which case the sprite is just mirrored along the y\-axis with no scaling).  

 

#### Syntax:

image\_yscale

 

#### Returns:

 (single precision floating point value)

 

#### Example:

if (image\_xscale \< 5\)   

 {  

     image\_xscale \+\= 0\.2;  

     image\_yscale \= image\_xscale;  

 }  

 else  

 {  

     instance\_create\_layer(x, y, "Effects", obj\_Explosion);  

     instance\_destroy();  

 }

The above code scales the sprite and then once it is scaled to 5 times its original size, a new instance of another object is created and the instance destroyed.
