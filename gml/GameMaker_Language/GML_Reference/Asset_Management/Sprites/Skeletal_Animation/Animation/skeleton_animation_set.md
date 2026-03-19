# skeleton\_animation\_set

This function defines the *animation set* to be used by the skeletal animation sprite assigned to the instance.

Once you have assigned a skeletal animation sprite to your instance, you can then define which *animation set* it should use at any given time with this function. When you created your sprite (in Spine) you will have defined multiple animation sets for different states and named each of them appropriately. These names are what you will use to tell GameMaker which animation set to use at any time in your game. For example, if your sprite is for a platform game, then you may have a "jump" set, a "run" set and an "idle" set all contained within the one sprite and you can switch between them in your game using this function.  

 The animation plays looped, which is the default.

Note that setting a new animation in this way will reset the [image\_index](../../Sprite_Instance_Variables/image_index.md) to 0, starting the new animation set from the beginning of its animation loop. If this is *not* the desired behaviour, then you can set a "mix" value using [skeleton\_animation\_mix](skeleton_animation_mix.md) and when you set a new animation it will be smoothly interpolated with the previous set. You should also make sure to have a keyframe at the beginning of every animation to prevent data from being held\-over from previous animations, unless you plan on using separate animation tracks.

 

#### Syntax:

skeleton\_animation\_set(animname, \[loop])

| Argument | Type | Description |
| --- | --- | --- |
| animname | [String](../../../../../GML_Overview/Data_Types.md) | The name (a string) of the animation set to use. |
| loop | [Boolean](../../../../../GML_Overview/Data_Types.md) | Whether the animation should loop or not (default is true) |

 

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_space))  

 {  

     if (skeleton\_animation\_get() !\= "jump")  

     {  

         skeleton\_animation\_set("jump");  

     }  

 }

The above code will change the animation set being used to the "jump" set when the space key is pressed, but only if the current set being used is not already "jump".
