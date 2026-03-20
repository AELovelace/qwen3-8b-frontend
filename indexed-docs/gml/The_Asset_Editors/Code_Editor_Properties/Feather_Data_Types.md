# Feather Data Types

[Feather](../../Setting_Up_And_Version_Information/IDE_Preferences/Feather_Settings.md) uses data types to provide smart syntax\-checking when writing code, ensuring you don't use the wrong data type for a variable or function parameter.

It also allows you to specify the data types for the parameters and return values of your own [script functions](../../GameMaker_Language/GML_Overview/Script_Functions.md), using [JSDoc comments](JSDoc_Script_Comments.md).

The @param and @return JSDoc tags allow you specify any one of the following types:

NOTE JSDoc base types are case\-insensitive, so string and String are the same, however specifiers (after the .) are case\-sensitive, meaning Id.DsList is valid (referring to a [DS List](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Lists/ds_list_create.md)) but Id.dslist is not.

| Base Types | Specifier Examples*\** | Description |
| --- | --- | --- |
| **Real** | *N/A* | A real number |
| **Bool** | *N/A* | A boolean |
| **String** | *N/A* | A string |
| **Array** | *Default* \- [Array](../../GameMaker_Language/GML_Overview/Arrays.md)  ... | An array, may include specifiers |
| **Pointer** | *Default* \- [Pointer](../../GameMaker_Language/GML_Overview/Data_Types.md)  ... | A pointer, may include specifiers |
| **Function** | *Default* \- [Function](../../GameMaker_Language/GML_Overview/Script_Functions.md)  ... | A function, may include specifiers |
| **Struct** | *Default* \- [Struct](../../GameMaker_Language/GML_Overview/Structs.md)  ... | A struct, may include specifiers (such as constructors) |
| **Id** | .Instance \- [Object Instance](../../GameMaker_Language/GML_Reference/Asset_Management/Instances/Instance_Variables/id.md)  .DsList \- [DS List](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Lists/ds_list_create.md)  .DsMap \- [DS Map](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Maps/ds_map_create.md)  .DsGrid \- [DS Grid](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Grids/ds_grid_create.md)  .DsStack \- [DS Stack](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Stacks/ds_stack_create.md)  .DsPriority \- [DS Priority](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Priority_Queues/ds_priority_create.md)  .DsQueue \- [DS Queue](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Queues/ds_queue_create.md)*...* | An ID, requires specifiers |
| **Asset** | .GMAnimCurve \- [Animation Curve Asset](../Animation_Curves.md)  .GMObject \- [Object Asset](../Objects.md)  .GMAudioGroup \- [Audio Group ID](../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Groups/Audio_Groups.md)  .GMFont \- [Font Asset](../Fonts.md)  .GMPath \- [Path Asset](../Paths.md)  .GMScript \- [Script Asset](../Scripts.md)  .GMShader \- [Shader Asset](../Shaders.md)  .GMSound \- [Sound Asset](../Sounds.md)  .GMTimeline \- [Timeline Asset](../Timelines.md)  .GMRoom \- [Room Asset](../Rooms.md)   .GMSequence \- [Sequence Asset](../Sequences.md)  .GMSprite \- [Sprite Asset](../Sprites.md)  .GMTileSet \- [Tile Set Asset](../Tile_Sets.md)*...* | An asset, requires specifiers |
| **Constant** | .Colour \- [Colour](../../GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md)  .HAlign \- [Horizontal Alignment Constant](../../GameMaker_Language/GML_Reference/Drawing/Text/draw_set_halign.md)  .VAlign \- [Vertical Alignment Constant](../../GameMaker_Language/GML_Reference/Drawing/Text/draw_set_valign.md)  .Cursor \- [Cursor Constant](../../GameMaker_Language/GML_Reference/Cameras_And_Display/The_Game_Window/window_get_cursor.md)  .EventType \- [Event Type Constant](../../GameMaker_Language/GML_Reference/Asset_Management/Objects/Object_Events/event_perform.md)  .EventNumber \- [Event Number Constant](../../GameMaker_Language/GML_Reference/Asset_Management/Objects/Object_Events/event_perform.md)  .PrimitiveType \- [Primitive Type Constant](../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_begin.md)  ... | A constant, requires specifiers |
| **Any** | *N/A* | Any data type |

NOTE *\** The **Specifier Examples** column lists some example specifiers, but not all of them. For example, there may be more possible types under the Id, Asset, and Constant groups, which are not listed here.

You may see an Any**\*** type in the IDE when using Feather, which indicates that the type of the identifier (which may be a variable, parameter, return value, etc.) can't be discerned by Feather at the moment. When more code is added for that identifier, it may be able to assume a specific type.

### Specifiers

A specifier is added after the base data type using a dot ., to specify the exact type of data in that group.

Types such as Id.DsList, Asset.GMObject, and Constant.Color use specifiers. Constructors are specified through the syntax Struct.{ConstructorName}. For example:

function Person() constructor  

 {  

  

 }  

  

 /// @param {Struct.Person} \_person  

 function do\_business(\_person)  

 {  

  

 }
 

### Collection Types

Types such as Array and Id.DsList, which are data structures that contain multiple values, are able to specify a single data type for all of their contents.

This is done using Collection Types, which are appended to the type using angle brackets \.

For example, an array containing strings would be Array\, and a DS List, containing an Array, containing Reals, would be Id.DsList\\>.

### Multiple Types

Multiple data types can also be listed, separated by a comma ,. For example String,Array\, Id.Instance,Asset.GMObject, etc.

## Type Validation

The table below shows what happens if you pass a value of a certain type (rows) into a parameter requiring a data type (column).

For example, specifying undefined (first row) for a parameter requiring a string (second column) results in an error.

|  | Undefined | String | Real | Bool | Array | Pointer | Function | Struct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Undefined | Allowed | Error | Error | Error | Error | Error | Error | Error |
| String | Error | Allowed | Allowed | Allowed | Error | Error | Warning | Warning |
| Real | Error | Warning | Allowed | Allowed | Error | Error | Error | Error |
| Bool | Warning | Error | Allowed | Allowed | Error | Warning | Warning | Warning |
| Array | Error | Error | Error | Error | Allowed | Error | Error | Error |
| Pointer | Error | Error | Error | Error | Error | Allowed | Error | Error |
| Function | Error | Error | Error | Error | Error | Error | Allowed | Error |
| Struct | Error | Error | Error | Error | Error | Error | Error | Allowed |

 

 

See Also (placeholder)

1. [Topic List](#)
