# base64\_encode

This function will convert a string into a base64 format encoded string.

Base64 is a commonly used encoding scheme that is often used for any media that needs to be stored or transferred over the internet as text, and renders the output unreadable to the human eye.

 

#### Syntax:

base64\_encode(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The string to encode |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_str, \_file;  

 \_str \= base64\_encode(game\_data);  

 \_file \= file\_text\_open\_write("save.txt");  

 file\_text\_write\_string(\_file, \_str);  

 file\_text\_close(\_file);

The above code will convert the string stored in game\_data into a base64 encoded string which is then stored in an external text file.
