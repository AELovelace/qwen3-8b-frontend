# dbg\_text\_separator

This function adds a horizontal text separator between controls.

The text can be multiline and is either taken from a string or from a reference to a variable that holds a value that can be converted to string. You can also pass an array containing items of either type. The function will then create a separator for each item in the array.

The text is left\-aligned by default though an optional parameter allows you to change this.

 
 

#### Syntax:

dbg\_text\_separator(ref\_or\_string\_or\_array, \[align])

| Argument | Type | Description |
| --- | --- | --- |
| ref\_or\_string\_or\_array | [Reference](../Variable_Functions/ref_create.md) or [String](../../GML_Overview/Data_Types.md) or [Array](../../GML_Overview/Arrays.md) | A string or a reference to a variable that can be converted to string, returned by [ref\_create](../Variable_Functions/ref_create.md), or an array containing references or strings |
| align | [Real](../../GML_Overview/Data_Types.md) | The alignment of the text separator (0\=left, 1\=centre, 2\=right). The default is left alignment. |

 

#### Returns:

[Debug Control](dbg_button.md)

 

#### Example:

Create Event

separator\_text \= "Separating Concerns";  

 a\_variable \= "The Last Separator";  

 a\_number \= 1;  

 dbg\_section("A long list of debug controls");  

dbg\_text\_separator("The First Separator\\n(spans multiple lines)");  

 repeat(4\) { dbg\_text(string(a\_number\+\+)); }  

dbg\_text\_separator(separator\_text, 1\);  

 repeat(4\) { dbg\_text(string(a\_number\+\+)); }  

dbg\_text\_separator(ref\_create(self, "a\_variable"), 2\);  

 repeat(4\) { dbg\_text(string(a\_number\+\+)); }
 

The above code first defines two strings and stores them in the variables separator\_text and a\_variable and also defines a counter variable that it stores in a\_number. It then adds a debug section with three text separators underneath it, created using dbg\_text\_separator, each of them followed by four simple debug controls (added using [dbg\_text](dbg_text.md)).
