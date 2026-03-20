# string\_foreach

This function executes a callback function on all characters of the given string.

The function optionally takes in a starting position and a length that define the range of characters over which to iterate, and the direction of iteration (left\-to\-right or right\-to\-left).

The callback function will receive two arguments for each character in the string: the character itself, and its position in the string.

  A message is output to the console when you attempt to access elements that are out of bounds.

 
 

#### Syntax:

string\_foreach(string, function, \[pos], \[length])

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../GML_Overview/Data_Types.md) | The string to iterate over |
| function | [Function](../../GML_Overview/Script_Functions.md) | The function to execute for each of the characters in the range, with arguments character and position |
| pos | [Real](../../GML_Overview/Data_Types.md) | The starting position (default is 1 for strings). Negative values count from the end of the string (e.g. \-1 is the position of the last character, \-2 is the position of the one before last character, etc.). 0 is treated the same as 1\. |
| length | [Real](../../GML_Overview/Data_Types.md) | The number of characters to iterate over and the direction in which to iterate (left\-to\-right (positive value) or right\-to\-left (negative value)). |

 

#### Returns:

N/A

 

#### Example 1:

function debug\_character(character, position)  

 {  

     show\_debug\_message(character);  

 }  

  

string\_foreach("test", debug\_character);
 

The above code first defines a function debug\_character that prints the character to the log using [show\_debug\_message](../Debugging/show_debug_message.md). It then calls the function string\_foreach on a string "test" to execute the debug\_character function on all its characters.

 

#### Example 2:

function debug\_extended(character, position)  

 {  

     show\_debug\_message("{0}: {1}", position, character);  

 }  

  

string\_foreach("1234567890", debug\_extended, \-1, \-infinity);
 

The above code first defines a function debug\_extended that shows a debug message with both the position and the character in it. Then, string\_foreach is called with the debug\_extended function on the string "1234567890". Because the offset is \-1, the first character on which the function will execute is the last one ("0"). The characters are traversed in a descending order because of the negative length ("0", "9", "8", "7", "6", ..., "1").
