# wallpaper\_set\_config

This function sends the configuration for your wallpaper to the companion app. It takes a "settings" array containing your options/sections, where each option/section is a [struct](../../GML_Overview/Structs.md).

### Settings Array

The array should have the following format: 

array \=   

 \[  

     {section\_or\_option},  

     {section\_or\_option},  

     {section\_or\_option}  

 ];

Each entry in this array is either a *section* or an *option*.

### Section Struct

A section struct requires the following format: 

{  

     type: "section",  

     name: "unique\_identifier",  

     label: "Label for this section in the companion app",  

     children: \[{section}, {option}, ...]  

 }

The children property in a section struct is an [array.](../../GML_Overview/Arrays.md) Each entry in this array is either another section struct or an option struct.

### Option Struct

An option struct requires the following format: 

{  

     type: "type\_of\_return\_value",  

     name: "unique\_identifier",  

     label: "Label for this section in the companion app"  

 }

The following types are allowed for the type property: "range", "boolean", "string", "string\_multiline", "color" (or "colour"), "file" and "folder".

Depending on the type, you must provide extra properties to the option struct: 

### ["range"](#)

{  

     type: "range",  

     value: \,  

     min: \,  

     max: \,  

     step: \  

 }

### ["boolean"](#)

{  

     type: "boolean",  

     value: \  

 }

### ["string"](#)

{  

     type: "string",  

     value: \  

 }

### ["string\_multiline"](#)

{  

     type: "string\_multiline",  

     value: \  

 }

### ["color" (or "colour")](#)

{  

     type: "colour",  

     value: \  

 }

### ["file"](#)

{  

     type: "file",  

     value: \  

 }

### ["folder"](#)

{  

     type: "folder",  

     value: \  

 }

 

 

#### Syntax:

wallpaper\_set\_config(settings\_array)

| Argument | Type | Description |
| --- | --- | --- |
| settings\_array | [Array](../../GML_Overview/Arrays.md) | An array containing section and option structs as detailed above |

 

#### Returns:

N/A

 

#### Example:

var \_config \=   

 \[  

     {  

         type: "section",  

         name: "animation",  

         label: "Animation",  

         children:  

         \[  

             {  

                 type: "range",  

                 name: "speed",  

                 label: "Rotation speed",  

                 value: 50,  

                 min: 0,  

                 max: 200,  

                 step: 25  

             },  

             {  

                 type: "boolean",  

                 name: "clockwiseRotation",  

                 label: "Clockwise rotation",  

                 value: false  

             },  

             {  

                 type: "boolean",  

                 name: "pause",  

                 label: "Pause animation",  

                 value: true  

             }  

         ]  

     },  

     {  

         type: "section",  

         name: "colours",  

         label: "Colours",  

         children:  

         \[  

            {  

                 type: "colour",  

                 name: "blendColor",  

                 label: "Blend colour",  

                 value: \#FA1E4E  

             },  

             {  

                 type: "range",  

                 name: "blendAlpha",  

                 label: "Blend alpha",  

                 value: 100  

             }  

         ]  

     }  

 ];  

  

wallpaper\_set\_config(\_config);
 

The code above shows an example of the wallpaper\_set\_config function with two sections. The first section contains three options (a range and two booleans) and the second section contains two options (a colour and a range).

This example initialises the array first in a local variable, and passes that into the function call. You can skip the variable stuff and initialise the array in the function arguments directly if you wish to do so.
