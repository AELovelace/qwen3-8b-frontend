# dbg\_control\_delete

This function deletes a debug control, e.g. a button, slider, text box, etc. It returns true if the control was deleted otherwise it returns false.

 

#### Syntax:

dbg\_control\_delete(control)

| Argument | Type | Description |
| --- | --- | --- |
| control | [Debug Control](dbg_button.md) | A debug control value returned by any debug control function, e.g. [dbg\_button](dbg_button.md), [dbg\_slider](dbg_slider.md), [dbg\_text\_separator](dbg_text_separator.md), etc. |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

var \_view1 \= dbg\_view("View", true);  

 var \_sec1 \= dbg\_section("Section 1");  

 var \_slider \= dbg\_slider(ref\_create(global, "value"), 0, 20, "Value1");  

 show\_debug\_message($"Slider exists? { dbg\_control\_exists(\_slider) }");  

 dbg\_control\_delete(\_slider);  

 show\_debug\_message($"Slider exists? { dbg\_control\_exists(\_slider) }");

This code creates a debug view, section and slider. It prints a message to the Output Log to check if the slider exists, then deletes the slider and prints the same message again.

This code outputs the following:

Slider exists? 1  

 Slider exists? 0
