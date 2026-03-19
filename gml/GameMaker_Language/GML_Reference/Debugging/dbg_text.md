# dbg\_text

This function creates a read\-only text label within the current debug section. You can use this to explain surrounding controls.

Both a [String](../../GML_Overview/Data_Types.md) and a [Reference](../Variable_Functions/ref_create.md) to a variable containing a string can be passed to the function. The text can be multiline.

You can also pass an array containing items of either type. The function will create a label for each item in the array.

  See [dbg\_text\_input](dbg_text_input.md) for a control that allows modifiable text.

 
 

#### Syntax:

dbg\_text(ref\_or\_string\_or\_array)

| Argument | Type | Description |
| --- | --- | --- |
| ref\_or\_string\_or\_array | [Reference](../Variable_Functions/ref_create.md) or [String](../../GML_Overview/Data_Types.md) or [Array](../../GML_Overview/Arrays.md) | A string or a reference to a variable that can be converted to string, returned by [ref\_create](../Variable_Functions/ref_create.md), or an array containing strings or references. |

 

#### Returns:

[Debug Control](dbg_button.md)

 

#### Example:

Create Event

text \= "text";  

 ref\_to\_text \= ref\_create(self, "text");  

dbg\_text(ref\_to\_text);  

dbg\_text(text);  

dbg\_text("More text");
 

The above code assigns some text to an [instance variable](../../GML_Overview/Variables/Instance_Variables.md) text. It then creates a reference to that variable using [ref\_create](../Variable_Functions/ref_create.md) and stores it in ref\_to\_text. Next, it adds three text controls to a new debug view "Default" that will be created, under a new section "Default". The three calls to dbg\_text add a text entry in three different ways: the first provides the reference to the text variable, the second passes the variable text itself (which assigns the *value* the variable currently has) and the last passes a string directly.
