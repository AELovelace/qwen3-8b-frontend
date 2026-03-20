# sprite\_get\_info

This function is used to retrieve information for the given sprite. You supply a sprite index (which can be an asset added through [The Asset Browser](../../../../../Introduction/The_Asset_Browser.md) or a sprite [added](../Sprite_Manipulation/sprite_add.md) at runtime)

The function returns a [struct](../../../../GML_Overview/Structs.md) with the following variables:

| [Sprite Info Struct](sprite_get_info.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| **width** | [Real](../../../../GML_Overview/Data_Types.md) | The sprite's width (in pixels) |
| **height** | [Real](../../../../GML_Overview/Data_Types.md) | The sprite's height (in pixels) |
| **xoffset** | [Real](../../../../GML_Overview/Data_Types.md) | The sprite's X offset/origin (in pixels) |
| **yoffset** | [Real](../../../../GML_Overview/Data_Types.md) | The sprite's Y offset/origin (in pixels) |
| **transparent** | [Boolean](../../../../GML_Overview/Data_Types.md) | true if the sprite is marked as transparent, otherwise false (This can only be specified through [sprite\_add()](../Sprite_Manipulation/sprite_add.md) or similar functions, and will be false for sprites created in the IDE) |
| **smooth** | [Boolean](../../../../GML_Overview/Data_Types.md) | true if the sprite is marked as smooth, otherwise false  (This can only be specified through [sprite\_add()](../Sprite_Manipulation/sprite_add.md) or similar functions, and will be false for sprites created in the IDE) |
| **type** | [Real](../../../../GML_Overview/Data_Types.md) | The type of the sprite: 0 \- Bitmap (Regular sprites) 1 \- SWF 2 \- Spine 3 \- SVG |
| **bbox\_left** | [Real](../../../../GML_Overview/Data_Types.md) | Position of the left edge of the bounding box (in pixels) |
| **bbox\_top** | [Real](../../../../GML_Overview/Data_Types.md) | Position of the top edge of the bounding box (in pixels) |
| **bbox\_right** | [Real](../../../../GML_Overview/Data_Types.md) | Position of the right edge of the bounding box (in pixels) |
| **bbox\_bottom** | [Real](../../../../GML_Overview/Data_Types.md) | Position of the bottom edge of the bounding box (in pixels) |
| **name** | [String](../../../../GML_Overview/Data_Types.md) | The name of the sprite |
| **num\_subimages** | [Real](../../../../GML_Overview/Data_Types.md) | The number of sub\-images (or frames) in the sprite |
| **use\_mask** | boolean | true if this sprite uses a collision mask (either generated from a shape or the image itself), otherwise false (meaning it uses a bounding box) |
| **num\_masks** | [Real](../../../../GML_Overview/Data_Types.md) | The number of masks in this sprite (will be greater than 1 if the sprite uses per\-frame masks) |
| **rotated\_bounds** | boolean | Whether the mask is "Rectangle with rotation" or not |
| **nineslice** | [Struct](../../../../GML_Overview/Structs.md) | The [Nine Slice struct](../Nine_Slice_Struct.md) for this sprite, or undefined if it has no nine slice data |
| **messages** | [Array](../../../../GML_Overview/Arrays.md) | Array of broadcast messages for this sprite, where each broadcast message is a struct containing information on the message (more information under "General Sprite Data") |
| **frame\_info** | [Array](../../../../GML_Overview/Arrays.md) | Array of frames for this sprite, where each frame is a struct containing information on its timing (more information under "General Sprite Data"). For sprites that do not contain any stretched frames, this will be undefined. |
| **frame\_speed** | [Real](../../../../GML_Overview/Data_Types.md) | The frame speed set for the sprite (see: [The Sprite Editor](../../../../../The_Asset_Editors/Sprites.md#h)) |
| **frame\_type** | [Sprite Speed Constant](sprite_get_speed_type.md) | The type of speed set for the sprite, either spritespeed\_framespersecond or spritespeed\_framespergameframe |

**This additional variable is available only for Bitmap (regular) sprites:**

| [Sprite Info Struct](sprite_get_info.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| **frames** | [Array](../../../../GML_Overview/Arrays.md) | Array of frames for this sprite, where each frame is a struct containing information on its texture (more information under "Bitmap Sprite Data") |

**These additional variables are available only for Spine sprites:**

| [Sprite Info Struct](sprite_get_info.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| **num\_atlas** | [Real](../../../../GML_Overview/Data_Types.md) | The number of atlas textures used |
| **atlas\_textures** | [Array](../../../../GML_Overview/Arrays.md) | Array of texture IDs used for the atlas |
| **premultiplied** | [Boolean](../../../../GML_Overview/Data_Types.md) | true if this sprite is marked as premultiplied, otherwise false |
| **animation\_names** | [Array](../../../../GML_Overview/Arrays.md) | Array containing the names of each animation in this sprite |
| **skin\_names** | [Array](../../../../GML_Overview/Arrays.md) | Array containing the names of each skin in this sprite |
| **bones** | [Array](../../../../GML_Overview/Arrays.md) | Array containing structs for each bone in this sprite (more information under "Spine Sprite Data") |
| **slots** | [Array](../../../../GML_Overview/Arrays.md) | Array containing structs for each slot in this sprite (more information under "Spine Sprite Data") |

The function will return undefined if the given sprite doesn't exist. Also note that information returned in this struct should be considered **read\-only** as modifying any of these variables will not affect the sprite.

The sections below contain information on the arrays and structs included in the returned struct based on the sprite type:

[General Sprite Data](#)

This section contains information on variables included in the struct for all kinds of sprites.

The messages variable is an array that contains information on the broadcast messages that exist in the given sprite. Each broadcast message in this array is a struct containing the following variables:

| Variable Name | Data Type | Description |
| --- | --- | --- |
| **frame** | [Real](../../../../GML_Overview/Data_Types.md) | The timing of this broadcast message from the start of the animation (in frames) |
| **message** | [String](../../../../GML_Overview/Data_Types.md) | The broadcast message string |

The frame\_info variable is an array that contains information on the timings of the sprite's frames. Each frame in this array is a struct containing the following variables:

  For sprites that do not contain any stretched frames, frame\_info will be undefined, meaning no array is provided.

| Variable Name | Data Type | Description |
| --- | --- | --- |
| **frame** | [Real](../../../../GML_Overview/Data_Types.md) | The timing for the start of this frame (in frames) |
| **duration** | [Real](../../../../GML_Overview/Data_Types.md) | The duration of this frame (in frames) |
| **image\_index** | [Real](../../../../GML_Overview/Data_Types.md) | The image index of this frame |

 

[Bitmap Sprite Data](#)

This section contains information on variables included in the struct for Bitmap sprites (sprites that are not Spine or vector type sprites).

The frames variable is an array that contains information on the textures of the sprite's frames. Each frame in this array is a struct containing the following variables:

| Variable Name | Data Type | Description |
| --- | --- | --- |
| **x** | [Real](../../../../GML_Overview/Data_Types.md) | The X position of this frame on its texture page (in pixels) |
| **y** | [Real](../../../../GML_Overview/Data_Types.md) | The Y position of this frame on its texture page (in pixels) |
| **w** | [Real](../../../../GML_Overview/Data_Types.md) | The logical width of the frame (in pixels) used internally |
| **h** | [Real](../../../../GML_Overview/Data_Types.md) | The logical height of the frame (in pixels) used internally |
| **texture** | [Real](../../../../GML_Overview/Data_Types.md) | The texture page ID for this frame |
| **original\_width** | [Real](../../../../GML_Overview/Data_Types.md) | The original width of the frame (in pixels) |
| **original\_height** | [Real](../../../../GML_Overview/Data_Types.md) | The original height of the frame (in pixels) |
| **crop\_width** | [Real](../../../../GML_Overview/Data_Types.md) | The actual width of the frame on the texture page after cropping and scaling (since GameMaker automatically trims the empty space around an image, and also scales it down if it doesn't fit) |
| **crop\_height** | [Real](../../../../GML_Overview/Data_Types.md) | The actual height of the frame on the texture page after cropping and scaling |
| **x\_offset** | [Real](../../../../GML_Overview/Data_Types.md) | The X offset from the left edge of the original image to the left edge of the cropped section |
| **y\_offset** | [Real](../../../../GML_Overview/Data_Types.md) | The Y offset from the top edge of the original image to the top edge of the cropped section |

 

[Spine Sprite Data](#)

This section contains information on variables included in the struct for Spine sprites.

The bones variable is an array that contains information on all bones in the given Spine sprite. Each bone in this array is a struct containing the following variables:

| Variable Name | Data Type | Description |
| --- | --- | --- |
| **parent** | [String](../../../../GML_Overview/Data_Types.md) | The name of the parent bone, or undefined if this bone doesn't have a parent |
| **name** | [String](../../../../GML_Overview/Data_Types.md) | The name of this bone |
| **index** | [Real](../../../../GML_Overview/Data_Types.md) | The index of this bone |
| **length** | [Real](../../../../GML_Overview/Data_Types.md) | The length of this bone |
| **x** | [Real](../../../../GML_Overview/Data_Types.md) | The X position of this bone |
| **y** | [Real](../../../../GML_Overview/Data_Types.md) | The Y position of this bone |
| **rotation** | [Real](../../../../GML_Overview/Data_Types.md) | The rotation of this bone |
| **scale\_x** | [Real](../../../../GML_Overview/Data_Types.md) | (Internal to Spine) Scale value on X |
| **scale\_y** | [Real](../../../../GML_Overview/Data_Types.md) | (Internal to Spine) Scale value on Y |
| **shear\_x** | [Real](../../../../GML_Overview/Data_Types.md) | (Internal to Spine) Shear value on X |
| **shear\_y** | [Real](../../../../GML_Overview/Data_Types.md) | (Internal to Spine) Shear value on Y |
| **transform\_mode** | [Real](../../../../GML_Overview/Data_Types.md) | (Internal to Spine) The transform mode |

  Please consult the [Spine documentation](https://en.esotericsoftware.com/spine-documentation "Spine Documentation") for more information regarding Spine's internal variables.

The slots variable is an array that contains information on all slots in the given Spine sprite. Each slot in this array is a struct containing the following variables:

| Variable Name | Data Type | Description |
| --- | --- | --- |
| **name** | [String](../../../../GML_Overview/Data_Types.md) | The name of the slot |
| **index** | [Real](../../../../GML_Overview/Data_Types.md) | The index of the slot |
| **bone** | [String](../../../../GML_Overview/Data_Types.md) | The name of the slot's bone, or "(none)" if there is no bone for this slot |
| **attachment** | [String](../../../../GML_Overview/Data_Types.md) | Attachment name |
| **red** | [Real](../../../../GML_Overview/Data_Types.md) | Red component of the slot's colour (0\-1\) |
| **green** | [Real](../../../../GML_Overview/Data_Types.md) | Green component of the slot's colour (0\-1\) |
| **blue** | [Real](../../../../GML_Overview/Data_Types.md) | Blue component of the slot's colour (0\-1\) |
| **alpha** | [Real](../../../../GML_Overview/Data_Types.md) | Alpha component of the slot's colour (0\-1\) |
| **blend\_mode** | [Real](../../../../GML_Overview/Data_Types.md) | (Internal to Spine) Blend mode for the slot |
| **dark\_red\*** | [Real](../../../../GML_Overview/Data_Types.md) | Red component of the slot's **dark** colour (0\-1\) |
| **dark\_green\*** | [Real](../../../../GML_Overview/Data_Types.md) | Green component of the slot's **dark** colour (0\-1\) |
| **dark\_blue\*** | [Real](../../../../GML_Overview/Data_Types.md) | Blue component of the slot's **dark** colour (0\-1\) |
| **dark\_alpha\*** | [String](../../../../GML_Overview/Data_Types.md) | Alpha component of the slot's **dark** colour (0\-1\) |
| attachments | [Array](../../../../GML_Overview/Arrays.md) of [String](../../../../GML_Overview/Data_Types.md) | An array containing the names of all available attachments for this slot. |

\*   The dark colour variables are only available if the slot has [Tint Black](https://en.esotericsoftware.com/spine-slots#Tint-black "Tint Black") enabled.

 

 

#### Syntax:

sprite\_get\_info(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The index of the sprite to get the information for. |

 

#### Returns

[Sprite Info Struct](sprite_get_info.md) (or [undefined](../../../../GML_Overview/Data_Types.md))

 

#### Example:

var \_info \= sprite\_get\_info(sprite\_index);  

  

 if (\_info !\= undefined \&\& \_info.type \=\= 0\)  

 {  

     var \_messages \= \_info.messages;  

     var \_messageCount \= array\_length(\_messages);  

       

     for (var i \= 0; i \< \_messageCount; i \+\+)  

     {  

         var \_message \= \_messages\[i];  

         show\_debug\_message("Message at frame " \+ string(\_message.frame) \+ ": " \+ \_message.message);  

     }  

 }
 

The above code gets the info struct for the instance's sprite, and then checks if it's not [undefined](../../../../GML_Overview/Data_Types.md) and that its type is 0 (meaning that it's a bitmap sprite). In that case, it gets the broadcast message array for that sprite and then runs a for loop to print each broadcast message (along with its frame) to the output log.
