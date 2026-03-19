# mask\_index

This built\-in instance variable holds the index of the sprite used as the collision mask for the instance.

When you define an object in GameMaker you can assign it a mask to be used for collisions rather than the one that corresponds to the defined sprite. This variable can be used to find the [sprite\_index](sprite_index.md) of that mask (or it will hold an invalid handle (\-1) if no sprite has been assigned) or to set the mask for an instance to the chosen sprite. Setting the mask index means that you can have, for example, a sprite for the instance with an irregular shape, yet give it a circular collision mask from a different sprite.

 

#### Syntax:

mask\_index

 

#### Returns:

[Sprite Asset](../../../../../The_Asset_Editors/Sprites.md)

 

#### Example:

mask\_index \= spr\_round;

The above code sets the mask of the instance to that of the sprite spr\_round.
