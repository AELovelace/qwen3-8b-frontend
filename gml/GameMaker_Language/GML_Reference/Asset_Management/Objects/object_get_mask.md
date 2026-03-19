# object\_get\_mask

This function will tell you whether the object you are checking has a mask index or not, and if it does then it will return the index of that mask (which is a sprite asset), or an invalid sprite handle (\-1\) if it does not. Please note that this is not an instance function! You can have an object with no mask while an instance of that same object can have one and vice versa, or they can even have different masks. You can set an individual instance's mask index using the [mask\_index](../Sprites/Sprite_Instance_Variables/mask_index.md) instance variable.

 

#### Syntax:

object\_get\_mask(obj)

| Argument | Type | Description |
| --- | --- | --- |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) | The object asset to check |

 

#### Returns:

[Sprite Asset](../../../../The_Asset_Editors/Sprites.md)

 

#### Example:

if (mask\_index !\= object\_get\_mask(object\_index))  

 {  

     mask\_index \= object\_get\_mask(object\_index);  

 }

The above example will check the mask index of the instance against the mask of the [object\_index](object_index.md) of the instance. If they are not the same, then it will assign the same mask as the one the object index has to the instance.
