# handle\_parse

This function parses a string to create a [handle reference](../../GML_Overview/Data_Types.md).

A handle is represented in a string with this format:  . Whether a handle is represented as an ID or as a name depends on the internal representation of the type.

 

  You can use [string](../Strings/string.md) to get the string representation of a handle and [real](real.md) to get the index number that it holds.

 

#### Syntax:

handle\_parse(value\_string)

| Argument | Type | Description |
| --- | --- | --- |
| value\_string | [String](../../GML_Overview/Data_Types.md) | The string representation of the handle, formatted as |

 

#### Returns:

[Handle](../../GML_Overview/Data_Types.md) (or [undefined](../../GML_Overview/Data_Types.md) in case of an invalid handle type or an incorrectly formatted string)

 

#### Example:

sprite \= spr\_player;  

 handle\_as\_string \= string(sprite);  

 handle\_from\_string \= handle\_parse(handle\_as\_string);  

  

 show\_debug\_message($"{sprite} ({typeof(sprite)})");  

 show\_debug\_message($"{handle\_as\_string} ({typeof(handle\_as\_string)})");  

 show\_debug\_message($"{handle\_from\_string} ({typeof(handle\_from\_string)})");
 

The code above converts the handle of a sprite named spr\_player to its string representation (handle\_as\_string), and then back into a handle (handle\_from\_string). It then outputs each of the created instance variables in a debug message, along with its type. This prints the following:

ref sprite spr\_player (ref)  

 ref sprite spr\_player (string)  

 ref sprite spr\_player (ref)

You can see that the original reference is converted into a string, which is then parsed back as a reference, which can again be used in functions just like the original reference.

The values of the handle variables are implicitly converted to their string representation to display them.
