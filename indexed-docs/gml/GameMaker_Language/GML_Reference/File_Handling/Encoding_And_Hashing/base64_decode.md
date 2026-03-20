# base64\_decode

This function will convert a string encoded previously using base64 format, into standard text.

Base64 is a commonly used encoding scheme that is often used for any media that needs to be stored or transferred over the internet as text, and renders the output unreadable to the human eye.

  To convert a base64 string into a sprite, use [sprite\_add](../../Asset_Management/Sprites/Sprite_Manipulation/sprite_add.md).

 

#### Syntax:

base64\_decode(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The string to decode |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_str, \_file;  

 \_str \= base64\_encode(game\_data);  

 \_file \= file\_text\_open\_read("save.txt");  

 \_str \= file\_text\_read\_string(\_file);  

 level\_data \= base64\_decode(\_str);  

 file\_text\_close(\_file);

The above code will open a text file and read a string from it into the local variable str. This string is then decoded and the result stored in the instance variable level\_data.
