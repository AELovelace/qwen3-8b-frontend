# sprite\_nineslice\_create

This function is used to create a Nine Slice [struct](../../../../GML_Overview/Structs.md "Structs") which can be modified and then applied to a sprite.

*Nine Slicing is a technique used to scale rectangular images for preserving details, making them retain their original form after scaling. See [Nine Slice](../../../../../The_Asset_Editors/Sprite_Properties/Nine_Slices.md) for more information.*

The contents of the returned struct are detailed on [this page](../Nine_Slice_Struct.md "The Nine Slice Struct").

You can store this struct in a variable, modify its properties, and apply it to any sprites using [sprite\_set\_nineslice()](sprite_set_nineslice.md "sprite_set_nineslice").

#### Syntax:

sprite\_nineslice\_create()

 

#### Returns:

[Nine Slice Struct](../Nine_Slice_Struct.md)

 

#### Example:

var \_nineslice \= **sprite\_nineslice\_create**();  

  

 \_nineslice.enabled \= true;  

 \_nineslice.left \= 10;  

 \_nineslice.right \= 10;  

 \_nineslice.top \= 10;  

 \_nineslice.bottom \= 10;  

  

 sprite\_set\_nineslice(spr\_box\_0, \_nineslice);
 

The code above creates a new Nine Slice struct, enables it and sets the offsets for the guides. The struct is then applied to a sprite, changing its Nine Slice properties.
