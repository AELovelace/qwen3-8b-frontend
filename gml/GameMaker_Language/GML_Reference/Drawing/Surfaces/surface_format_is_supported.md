# surface\_format\_is\_supported

This function returns whether the given surface format is supported on the current platform. All formats are [listed here](surface_create.md#formats).

 

#### Syntax:

surface\_format\_is\_supported(format)

| Argument | Type | Description |
| --- | --- | --- |
| format | [Surface Format Constant](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md#surface_format_constant) | The surface format to check |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (surface\_format\_is\_supported(surface\_rgba32float))  

 {  

     my\_surf \= surface\_create(320, 180, surface\_rgba32float);  

     // ...  

 }  

 else  

 {  

     show\_debug\_message("Effect disabled, 32\-bit surface not supported");  

 }

This checks if the [surface\_rgba32float](surface_create.md) format is supported on the current platform, and in that case it creates a surface with that format. However, if the format is not supported, it instead prints a message to the output log.
