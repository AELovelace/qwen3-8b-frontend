# texturegroup\_add

This function adds a new [Dynamic Texture Group](../../../../Settings/Texture_Information/Dynamic_Textures.md) to the game from the given image file(s) and/or buffer(s), using the sprite information given as a struct.

## Arguments

The first argument is the name of the Texture Group to be created. If a Texture Group with the given name already exists, this will cause a fatal [error](../../../../Additional_Information/Errors/Runner_Errors.md).

For the second argument, you may pass either a file name, a buffer or an array containing multiple of these (the array can contain a mix of both). The image file(s) can be any bitmap file format. For file access rules see: [Accessing File Areas](../../../../Additional_Information/The_File_System.md#h1)

A buffer can contain any file format supported for texture groups: PNG, JPEG, GIF, QOIF, DDS, ASTC, etc., as well as a RAW texture format that can be used with [Surfaces](../Surfaces/Surfaces.md). Note that any GPU hardware\-compressed texture must be supported on the target for it to work.

[RAW Texture Format](#)

The RAW texture format consists of a 16byte header at the start, followed by the RGBA data:

Byte Offset              Type               Description  

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  

 \+0                       unsigned int       "RAW " text in memory (the value 0x20574152\)  

 \+4                       int                width in pixels of the image  

 \+8                       int                height in pixels of the image  

 \+12                      int                format (this should be 0\)  

 \+16                      ....               the RGBA data stored as byte per pixel R, G, B, A with row first, width\*height pixels

The image data from a surface can be copied to the buffer at an offset using [buffer\_get\_surface](../../Buffers/buffer_get_surface.md).

### Sprite Data Struct

The last argument must be a struct or a JSON string providing information on the sprites contained in the new Texture Group. This struct or JSON object must have the following format:

[Struct Format](#)

- sprites: The struct/JSON must contain a struct named sprites.  

  

 The sprites struct may contain one struct per sprite to be added to the Texture Group. The name of each sprite struct is used as the name of the sprite asset that is created. For example, a sprite from the struct passed into this function would be accessed as struct.sprites.sprite\_name.
	- Each sprite struct **must** contain the following members:
		- width: The width of the sprite in pixels
		- height: The height of the sprite in pixels
		- frames: An array of structs, where each struct defines a frame in the sprite. Each frame struct may contain the following members:
			- x (*REQUIRED*): The x position of the frame within the texture, in pixels
			- y (*REQUIRED*): The y position of the frame within the texture, in pixels
			- w: The width of the frame within the texture, in pixels
			- h: The height of the frame within the texture, in pixels
			- x\_offset: The x offset for this frame within the sprite in pixels (only if frame has been cropped)
			- y\_offset: The y offset for this frame within the sprite in pixels (only if frame has been cropped)
			- crop\_width: The width for this frame within the sprite in pixels (only if frame has been cropped)
			- crop\_height: The height for this frame within the sprite in pixels (only if frame has been cropped)
			- original\_width: The original width for this frame within the sprite in pixels (only if frame has been scaled)
			- original\_height: The original height for this frame within the sprite in pixels (only if frame has been scaled)
			- tp: The index of the image file from the array provided to the function, to point to the correct texture. Used only when multiple files are provided and the frame comes from a texture file after the first.
	- Each sprite struct can also contain the following optional members:
		- xoffset, yoffset: The x and y origin in pixels
		- bbox\_left, bbox\_right, bbox\_top, bbox\_bottom: Bounding box values in pixels
		- bbox\_kind: The type of bounding box as a [Bounding Box Kind (Shape) Constant](../../Asset_Management/Sprites/Sprite_Manipulation/sprite_collision_mask.md)
		- frame\_speed: Animation speed
		- frame\_type: Animation speed type of the sprite as a [Sprite Speed Constant](../../Asset_Management/Sprites/Sprite_Information/sprite_get_speed_type.md)
		- rotated\_bounds: Boolean for whether the sprite supports a rotating rectangular collision mask
		- mask: An array of bits for the mask (single frame)
		- masks: An array of arrays containing bits for the masks (per frame)
		- nineslice: A struct describing the Nine Slice information for the sprite, containing the following members:
			- left, right, top, bottom: The edge positions within the sprite
			- tilemode\_left, tilemode\_right, tilemode\_top, tilemode\_bottom, tilemode\_centre: The [Tile Mode Constant](../../Asset_Management/Sprites/Nine_Slice_Struct.md) for each edge and the centre
		- messages: An array of structs describing the broadcast messages for this sprite. Each struct contains:
			- frame: The frame time
			- message: The broadcast message string
		- frame\_info: An array of structs describing information about the frames in the sprite
			- frame: The frame time
			- duration: The frame duration
			- image\_index: The image index to use for this frame

## Overriding \& Deletion

If any sprite names used in this struct already exist at the time of the call, the original sprites will be overridden.

The Texture Group can later be deleted using [texturegroup\_delete](texturegroup_delete.md). If any sprites were overridden by this Texture Group, they will be restored.

## Notes

  This function is not supported on HTML5\.

  The texture will be **unloaded** after being created and can be loaded with [texturegroup\_load](texturegroup_load.md) or when a sprite from it is first drawn.

  Buffers used by a texture group cannot be deleted while the texture group exists. You need to delete the buffers manually and the texture group *must* be deleted first.

   The "**Preview**" option in the Graphics Game Options for your target will open a folder with a preview of the Texture Pages for your target. This folder will also contain a asset\_layout\_info.json file with JSON info that can be passed into this function as a string. This way you can set up Texture Pages temporarily in the IDE and use the JSON info from this file to load those Texture Pages at runtime using this function, so that e.g. you don't have to figure out the frame coordinates, width, etc., yourself.

 

#### Syntax:

texturegroup\_add(groupname, filename\_or\_buffer\_or\_array, struct\_or\_json)

| Argument | Type | Description |
| --- | --- | --- |
| groupname | [String](../../../GML_Overview/Data_Types.md) | The name of the texture group |
| filename\_or\_buffer\_or\_array | [String](../../../GML_Overview/Data_Types.md) or [Buffer](../../Buffers/buffer_create.md) or [Array](../../../GML_Overview/Arrays.md) | A file name, a buffer or an array containing a combination of these to load |
| struct\_or\_json | [Struct](../../../GML_Overview/Structs.md) or [String](../../../GML_Overview/Data_Types.md) | A struct or JSON string describing the sprite data |

 

#### Returns:

N/A

 

#### Example 1: Basic Use

var \_sprite\_data \= {  

     sprites :   

     {          

         blue\_guy :   

         {  

             width : 116,  

             height : 128,  

             frames :  

             \[   

                 { x : 116\*0, y : 128\*0 },  

                 { x : 116\*1, y : 128\*0 },  

                 { x : 116\*2, y : 128\*0 },  

                 { x : 116\*3, y : 128\*0 },  

                 { x : 116\*4, y : 128\*0 },  

                 { x : 116\*5, y : 128\*0 },  

             ],  

         },  

         red\_guy :  

         {  

             width : 116,  

             height : 128,  

             frame\_speed : 8,  

             frames :  

             \[   

                 { x : 116\*0, y : 128\*1 },  

                 { x : 116\*1, y : 128\*1 },  

                 { x : 116\*2, y : 128\*1 },  

                 { x : 116\*3, y : 128\*1 },  

                 { x : 116\*4, y : 128\*1 },  

                 { x : 116\*5, y : 128\*1 },  

             ],  

         }  

     }  

 };  

  

 texturegroup\_add("MyTextureGroup", "image.png", \_sprite\_data);  

  

 var \_sprites \= texturegroup\_get\_sprites("MyTextureGroup");
 

This first sets up a struct with data for two sprites. Each sprite struct contains its width, height and a frames array with positions for the frames relative to the texture page.

The function is then called with the Texture Group's name, the file name to be loaded (in this case, from the [Included Files](../../../../Settings/Included_Files.md)) and the previously created struct is passed in.

Then [texturegroup\_get\_sprites](texturegroup_get_sprites.md) is called on the new Texture Group which returns an array of the sprites included in that group. The sprites from the array can now be used anywhere.

 

#### Example 2: Multiple Textures, from Different Sources

Create Event

buffer \= buffer\_load("image2\.png");  

  

 var \_sprite\_data \= {  

     sprites :   

     {  

         blue\_guy :   

         {  

             width : 116,  

             height : 128,  

             frames :  

             \[  

                 { x : 116\*0, y : 128\*0 },  

             ],  

         },  

         red\_guy :  

         {  

             width : 116,  

             height : 128,  

             frames :  

             \[  

                 { x : 116\*0, y : 128\*0, tp : 1 },  

             ],  

         }  

     }  

 };  

  

 texturegroup\_add("MyOtherTextureGroup", \["image.png", buffer], \_sprite\_data);
 

Clean Up Event

texturegroup\_delete("MyOtherTextureGroup");  

 buffer\_delete(buffer);

The code above shows how texturegroup\_add can be used with an array of multiple textures.

In the Create event, a PNG image is first loaded from disk into a buffer using [buffer\_load](../../Buffers/buffer_load.md). Next, the sprite data struct is created, which defines two sprites, each having a single frame, one on the first texture page, another one on the second texture page (indicated by the offset value in tp). The texture group is then added using texturegroup\_add. The function receives an array containing two elements: the file name of an image on disk and the previously loaded buffer containing PNG data.

In the Clean Up event, first the texture group is deleted, then the buffer containing the image data.
