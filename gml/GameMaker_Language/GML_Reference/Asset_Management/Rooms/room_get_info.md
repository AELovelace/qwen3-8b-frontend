# room\_get\_info

This function gets information on a room from storage, or live information on either the [current](room.md "room") room or a persistent room, and returns the info as a [struct](../../../GML_Overview/Structs.md#struct). You can choose to exclude information through the given optional arguments.

The room must have been previously created using [The Asset Browser](../../../../Introduction/The_Asset_Browser.md) or have been added in\-game using [room\_add](room_add.md).

The format of the returned struct is as follows:

room\_info\_struct \=  

 {  

     instances:  

     \[  

         {/\* Instance Info Struct \*/},  

         {/\* Instance Info Struct \*/},  

     ],  

     layers:  

     \[  

         {  

             elements:  

             \[  

                 {/\* Layer Element Info Struct \*/},  

                     {  

                         /\* Example \*/  

                         type: layerelementtype\_tilemap,  

                         tiles: \[/\* Tile Map Data \*/]  

                     }  

                 ]  

             },  

         ],  

     views:  

     \[  

         {/\* View Info Struct \*/},  

     ]  

 }

 

The instances array holds the information from storage (including instances added to a room at runtime using [room\_instance\_add](room_instance_add.md)). The layers array holds the current instances in the room (the "live" state). Note that the instances and layers members hold a value of 0 if the room has no instances or layers respectively.

The tables below list all the possible structs that can be contained in the returned struct:

[Room Info](#)

This is the main struct returned by the function. All variables listed below are present at the root of this returned struct:

Room Info Struct

| Variable Name | Data Type | Description |
| --- | --- | --- |
| width | [Real](../../../GML_Overview/Data_Types.md) | The width of the room |
| height | [Real](../../../GML_Overview/Data_Types.md) | The height of the room |
| creationCode | [Script Function](../../../GML_Overview/Script_Functions.md) | The index of the script function that contains this room's creation code |
| physicsWorld | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the room has a [physics world](../../Physics/The_Physics_World/The_Physics_World.md) |
| physicsGravityX | [Real](../../../GML_Overview/Data_Types.md) | The physics world's gravity component along the x axis |
| physicsGravityY | [Real](../../../GML_Overview/Data_Types.md) | The physics world's gravity component along the y axis |
| physicsPixToMeters | [Real](../../../GML_Overview/Data_Types.md) | The physics world's pixel\-to\-metre scale |
| persistent | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the room is persistent |
| enableViews | [Boolean](../../../GML_Overview/Data_Types.md) | Whether views are enabled for the room |
| clearDisplayBuffer | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to clear the display buffer before drawing the room |
| clearViewportBackground | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to clear viewports' backgrounds before drawing to them |
| colour | [Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The clear colour used when clearDisplayBuffer is set to true |
| instances | [Array](../../../GML_Overview/Arrays.md) of [Room Instance Info Struct](room_get_info.md#room_instance_info_struct) | An array listing all instances placed in the room with basic information on them |
| layers | [Array](../../../GML_Overview/Arrays.md) of [Room Layer Info Struct](room_get_info.md#room_layer_info_struct) | An array listing all room layers, in order of increasing depth |
| views | [Array](../../../GML_Overview/Arrays.md) of [Room View Info Struct](room_get_info.md#room_view_info_struct) | An array listing all views, ordered by view index |

[Instance Info](#)

This type of struct represents one instance in the room.

These structs are found in the instances array, which is part of the main struct returned by the function.

Instance Info Struct

| Variable Name | Data Type | Description |
| --- | --- | --- |
| id | [Object Instance](../Instances/Instance_Variables/id.md) | The instance ID |
| object\_index | [String](../../../GML_Overview/Data_Types.md) | The name of the object this is an instance of (use [asset\_get\_index](../Assets_And_Tags/asset_get_index.md) to get the actual object) |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the instance's position |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the instance's position |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The x scale of the instance |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The y scale of the instance |
| angle | [Real](../../../GML_Overview/Data_Types.md) | The rotation angle of the instance |
| image\_index | [Real](../../../GML_Overview/Data_Types.md) | The image index used by the instance |
| image\_speed | [Real](../../../GML_Overview/Data_Types.md) | The image speed of the instance |
| colour | [Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The blend colour used to draw the instance |
| creation\_code | [Script Function](../../../GML_Overview/Script_Functions.md) | The index of the script function that contains the instance's creation code |
| pre\_creation\_code | [Script Function](../../../GML_Overview/Script_Functions.md) | The index of the script function that holds the pre\-creation code for this specific instance, i.e. the overrides for its [Object Variables](../../../../The_Asset_Editors/Object_Properties/Object_Variables.md) as set in the Room Editor. See: [Pre\-creation Code](../../../../The_Asset_Editors/Object_Properties/Object_Variables.md#h) |

[Layer Info](#)

This type of struct represents one layer in the room.

These structs are found in the layers array, which is part of the main struct returned by the function.

Layer Info Struct

| Variable Name | Data Type | Description |
| --- | --- | --- |
| id | [Real](../../../GML_Overview/Data_Types.md) | The layer handle |
| name | [String](../../../GML_Overview/Data_Types.md) | The name of the layer |
| visible | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the layer is visible |
| depth | [Real](../../../GML_Overview/Data_Types.md) | The depth of the layer |
| xoffset | [Real](../../../GML_Overview/Data_Types.md) | The x offset of the layer |
| yoffset | [Real](../../../GML_Overview/Data_Types.md) | The y offset of the layer |
| hspeed | [Real](../../../GML_Overview/Data_Types.md) | The horizontal speed of the layer |
| vspeed | [Real](../../../GML_Overview/Data_Types.md) | The vertical speed of the layer |
| effectEnabled | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the layer filter/effect is currently enabled |
| effectToBeEnabled | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the layer filter/effect should be enabled/disabled in the next frame (the next value of effectEnabled) |
| effect | [FX Struct](Filter_Effect_Layers/fx_create.md) | A struct containing the effect's parameters (\-1 if no layer effect is set) |
| shaderID | [Shader Asset](../../../../The_Asset_Editors/Shaders.md) | The shader to be applied to the layer ([layer\_shader](General_Layer_Functions/layer_shader.md)) |
| elements | [Array](../../../GML_Overview/Arrays.md) of [Room Layer Element Info Struct](room_get_info.md#room_layer_element_info_struct) | An array listing all elements on the layer. Each element type struct contains information specific to it. |

[View Info](#)

This type of struct represents one view in the room.

These structs are found in the views array, which is part of the main struct returned by the function.

View Info Struct

| Variable Name | Data Type | Description |
| --- | --- | --- |
| visible | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the view is visible |
| cameraID | [Camera ID](../../Cameras_And_Display/Cameras_And_Viewports/camera_create.md) | The camera assigned to this view |
| xview | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the view camera's position |
| yview | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the view camera's position |
| wview | [Real](../../../GML_Overview/Data_Types.md) | The width of the view's camera |
| hview | [Real](../../../GML_Overview/Data_Types.md) | The height of the view's camera |
| hspeed | [Real](../../../GML_Overview/Data_Types.md) | The horizontal movement speed of the view |
| vspeed | [Real](../../../GML_Overview/Data_Types.md) | The vertical movement speed of the view |
| xport | [Real](../../../GML_Overview/Data_Types.md) | The x position on screen where the view is drawn |
| yport | [Real](../../../GML_Overview/Data_Types.md) | The y position on screen where the view is drawn |
| wport | [Real](../../../GML_Overview/Data_Types.md) | The width of the viewport |
| hport | [Real](../../../GML_Overview/Data_Types.md) | The height of the viewport |
| object | [Object Asset](../../../../The_Asset_Editors/Objects.md) | The object of which the first instance in the room should be followed by the camera |
| hborder | [Real](../../../GML_Overview/Data_Types.md) | The horizontal border around the instance of the object to follow |
| vborder | [Real](../../../GML_Overview/Data_Types.md) | The vertical border around the instance of the object to follow |

[Layer Element Info](#)

This type of struct represents one element in a layer.

These structs are found in the elements array, which is part of a layer struct.

Layer Element Info Struct

| Variable Name | Data Type | Description |
| --- | --- | --- |
| All Element Types | | |
| id | [Real](../../../GML_Overview/Data_Types.md) | The unique ID of the element |
| type | [Layer Element Type Constant](General_Layer_Functions/layer_get_element_type.md) | The type of element |
| Background Element Type | | |
| sprite\_index | [Sprite Asset](../../../../The_Asset_Editors/Sprites.md) | The sprite used by the background |
| image\_index | [Real](../../../GML_Overview/Data_Types.md) | The sprite's subimage |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The scale along the x axis |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The scale along the y axis |
| htiled | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to tile the background image horizontally |
| vtiled | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to tile the background image vertically |
| stretch | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to stretch the background so it fills the entire room |
| visible | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the background should be visible |
| blendColour | [Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The blend colour to draw the background with |
| blendAlpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha value between 0 and 1 to use |
| image\_speed | [Real](../../../GML_Overview/Data_Types.md) | The image speed of the background |
| speed\_type | [Sprite Speed Constant](../Sprites/Sprite_Information/sprite_get_speed_type.md) | The units in which image\_speed is expressed, either spritespeed\_framespersecond or spritespeed\_framespergameframe |
| name | [String](../../../GML_Overview/Data_Types.md) | The name of the background |
| Instance Element Type | | |
| inst\_id | [Object Instance](../Instances/Instance_Variables/id.md) | The ID of the instance |
| Sprite Element Type | | |
| sprite\_index | [Sprite Asset](../../../../The_Asset_Editors/Sprites.md) | The sprite index of this sprite element |
| image\_index | [Real](../../../GML_Overview/Data_Types.md) | The subimage of the sprite |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the sprite's position |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the sprite's position |
| image\_xscale | [Real](../../../GML_Overview/Data_Types.md) | The scale of the image along the x axis |
| image\_yscale | [Real](../../../GML_Overview/Data_Types.md) | The scale of the image along the y axis |
| image\_angle | [Real](../../../GML_Overview/Data_Types.md) | The image angle |
| image\_alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha value between 0 and 1 |
| image\_blend | [Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The blend colour |
| image\_speed | [Real](../../../GML_Overview/Data_Types.md) | The animation speed of the image, expressed in speed\_type units |
| speed\_type | [Sprite Speed Constant](../Sprites/Sprite_Information/sprite_get_speed_type.md) | The units in which image\_speed is expressed, either spritespeed\_framespersecond or spritespeed\_framespergameframe |
| name | [String](../../../GML_Overview/Data_Types.md) | The name of the sprite element as given in [The Room Editor](../../../../The_Asset_Editors/Rooms.md) (default is graphic\_\*) |
| Tile Map Element Type | | |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position (or offset) of the tile map in the room |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position (or offset) of the tile map in the room |
| tileset\_index | [Tile Set Asset](../../../../The_Asset_Editors/Tile_Sets.md) | The tile set that this tile map uses |
| data\_mask | [Real](../../../GML_Overview/Data_Types.md) | The bitmask value for the tile map |
| tiles | [Array](../../../GML_Overview/Arrays.md) of [Real](../../../GML_Overview/Data_Types.md) | This variable is only present when the tilemap\_data parameter is set to true. It is a one\-dimensional array that contains all the tile map data, listed row by row. |
| width | [Real](../../../GML_Overview/Data_Types.md) | The width in cells of the tile map |
| height | [Real](../../../GML_Overview/Data_Types.md) | The height in cells of the tile map |
| name | [String](../../../GML_Overview/Data_Types.md) | The tile map's name |
| Particle System Element Type | | |
| ps | [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md) | The particle system asset |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the particle system element's position |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the particle system element's position |
| angle | [Real](../../../GML_Overview/Data_Types.md) | The angle by which the particle system element is rotated |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The scale along the x axis of the particle system element |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The scale along the y axis of the particle system element |
| blend | [Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The blend colour to use to draw the particle system element |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha value between 0 and 1 to use for the particle system element |
| name | [String](../../../GML_Overview/Data_Types.md) | The name of the particle system element as defined in [The Room Editor](../../../../The_Asset_Editors/Rooms.md) (default is particle\_\*) |
| Tile Element Type | | |
| visible | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the tile is visible |
| sprite\_index | [Sprite Asset](../../../../The_Asset_Editors/Sprites.md) | The sprite this tile is on |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the tile position |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the tile position |
| width | [Real](../../../GML_Overview/Data_Types.md) | The width of the tile |
| height | [Real](../../../GML_Overview/Data_Types.md) | The height of the tile |
| image\_xscale | [Real](../../../GML_Overview/Data_Types.md) | The scale factor along the x axis of the tile |
| image\_yscale | [Real](../../../GML_Overview/Data_Types.md) | The scale factor along the y axis of the tile |
| image\_angle | [Real](../../../GML_Overview/Data_Types.md) | The angle of the tile |
| image\_blend | [Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The blend colour to use to draw the tile |
| image\_alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha to use |
| xo | [Real](../../../GML_Overview/Data_Types.md) | The x offset |
| yo | [Real](../../../GML_Overview/Data_Types.md) | The y offset |
| Sequence Element Type | | |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the sequence position |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the sequence position |
| image\_xscale | [Real](../../../GML_Overview/Data_Types.md) | The scale along the x axis of the entire sequence |
| image\_yscale | [Real](../../../GML_Overview/Data_Types.md) | The scale along the y axis of the entire sequence |
| image\_angle | [Real](../../../GML_Overview/Data_Types.md) | The angle by which the sequence is rotated |
| image\_alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha value between 0 and 1 to use |
| image\_blend | [Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The blend colour to use to draw the sequence |
| image\_speed | [Real](../../../GML_Overview/Data_Types.md) | The animation speed of the sequence, expressed in speed\_type units |
| speedType | [Sprite Speed Constant](../Sprites/Sprite_Information/sprite_get_speed_type.md) | The units in which image\_speed is expressed, either spritespeed\_framespersecond or spritespeed\_framespergameframe |
| seq\_id | [Sequence Asset](../../../../The_Asset_Editors/Sequences.md) | The sequence asset |
| name | [String](../../../GML_Overview/Data_Types.md) | The name of the sequence element as defined in [The Room Editor](../../../../The_Asset_Editors/Rooms.md) (default is graphic\_\*) |
| head\_position | [Real](../../../GML_Overview/Data_Types.md) | The playhead position of the sequence |

 

#### Syntax:

room\_get\_info(room, \[views], \[instances], \[layers], \[layer\_elements], \[tilemap\_data], \[live])

| Argument | Type | Description |
| --- | --- | --- |
| room | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to get the info from |
| views | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to include view information in the struct (defaults to true) |
| instances | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to include instance information in the struct (defaults to true) |
| layers | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to include layer information in the struct (defaults to true) |
| layer\_elements | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to include layer element information in the struct (defaults to true, requires layers to be set to true) |
| tilemap\_data | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to include tile map data in the struct (defaults to true, requires layers and layer\_elements to be set to true) |
| live | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to report live data for the current room or a persistent room, otherwise return data from storage (defaults to false) |

 

#### Returns:

[Room Info Struct](room_get_info.md#room_info_struct)

 

#### Example 1: Basic Use

var \_info \= room\_get\_info(Room1\);  

 var \_info\_json \= json\_stringify(\_info, true);  

 show\_debug\_message(\_info\_json);

The above code gets the information of the room Room1, converts the returned struct to a JSON string using [json\_stringify](../../File_Handling/Encoding_And_Hashing/json_stringify.md), then outputs it in a debug message. All view, instance, layer, layer element and tile map information is included in the output.

 

#### Example 2: Live Data

var \_info \= room\_get\_info(room, true, true, true, true, true, true);  

 var \_info\_json \= json\_stringify(\_info, true);  

 show\_debug\_message(\_info\_json);

The above code gets all live information on the current room and, like the previous example, outputs it in a debug message.

 

#### Example 3: Live Data on a Persistent Room

Create Event

instance\_create\_layer(x, y, layer, obj\_not\_persistent);  

  

 persistent \= true;  

 room\_persistent \= true;  

  

 room\_goto(rm\_two);
 

Room Start Event

if (room !\= rm\_two) { exit; }  

  

 var \_info \= room\_get\_info(rm\_one, false, true, true, true, false, true);  

 var \_info\_json \= json\_stringify(\_info, true);  

 show\_debug\_message(\_info\_json);
 

This code shows how to get live data on a persistent room you're not currently in.

In an object's Create event a new instance of an object not marked persistent is first added using [instance\_create\_layer](../Instances/instance_create_layer.md). The instance executing the code is then marked persistent by setting its [persistent](../Instances/Instance_Variables/persistent.md) variable to true and the room is also marked persistent by setting [room\_persistent](room_persistent.md) to true. The room is then changed to a room rm\_two using [room\_goto](room_goto.md).

In the Room Start event a check is first performed to find out if the current room is rm\_two. If it isn't, the event is exited. If code execution continues, the live data on instances, layers and layer\_elements in the original room is requested using a call to room\_get\_info. This info is once again, like in the previous examples, output in a debug message.
