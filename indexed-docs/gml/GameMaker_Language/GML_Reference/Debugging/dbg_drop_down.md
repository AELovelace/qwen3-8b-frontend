# dbg\_drop\_down

This function creates a drop down control for an integer value within the current [debug section](dbg_section.md).

The values and names for the drop down are specified as a comma\-delimited string, where integer values can optionally be specified after a colon symbol. For example "Zero,One:10,Two:20" creates a 3 entry drop down that will set the variable to the value 0, 10 or 20, depending on the selected option.

You can also pass an array as the first argument, and the function will create a drop down for each reference in the array.

Note that you can use the mouse wheel to scroll through a longer list of values.

 
 

#### Syntax:

dbg\_drop\_down(ref\_or\_array, specifier\[, label])

| Argument | Type | Description |
| --- | --- | --- |
| ref\_or\_array | [Reference](../Variable_Functions/ref_create.md) or [Array](../../GML_Overview/Arrays.md) | A reference to the variable, created using [ref\_create](../Variable_Functions/ref_create.md), or an array containing references |
| specifier | [String](../../GML_Overview/Data_Types.md) or [Array](../../GML_Overview/Arrays.md) | A comma\-delimited string listing the options and, optionally, the integer value to use (e.g. "Zero,One:10,Two:20") |
| label | [String](../../GML_Overview/Data_Types.md) | A label to show next to the dropdown |

 

#### Returns:

[Debug Control](dbg_button.md)

 

#### Example:

Create Event

difficulty \= 1;  

 var \_ref \= ref\_create(self, "difficulty");  

dbg\_drop\_down(\_ref, "Easy:0,Normal:1,Hard:2,Impossible:3");
 

The code above first set an instance variable difficulty that stores the game's difficulty level. It creates a reference to the variable using [ref\_create](../Variable_Functions/ref_create.md) and creates a dropdown control using dbg\_drop\_down to change the variable through that reference. The specifier lists the four difficulty levels as "Easy:0,Normal:1,Hard:2,Impossible:3".
