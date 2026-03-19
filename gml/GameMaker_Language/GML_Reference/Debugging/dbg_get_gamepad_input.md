# dbg\_get\_gamepad\_input

This function gets the status of gamepad input in the Debug Overlay.

The function returns \-1 to indicate gamepad input is disabled, the constant [all](../../GML_Overview/Instance Keywords/all.md) (\-3\) to indicate gamepad input is enabled for all gamepads, or a number \>\= 0 to indicate that a specific gamepad is being used for debug overlay input.

Gamepad input can be configured using optional parameters that you pass to [show\_debug\_overlay](show_debug_overlay.md).

 

#### Syntax:

dbg\_get\_gamepad\_input()

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

var \_input\_status \= dbg\_get\_gamepad\_input();  

 var \_status\_text \= "";  

 if (\_input\_status \>\= 0\)  

 {  

     \_status\_text \= $"Gamepad {\_input\_status}";  

 }  

 if (\_input\_status \=\= all)  

 {  

     \_status\_text \= "All Gamepads";  

 }  

 if (\_input\_status \=\= \-1\)  

 {  

     \_status\_text \= "Disabled";  

 }  

 show\_debug\_message($"Debug Overlay Gamepad Input: {\_text}");

The code above gets the status of gamepad input using dbg\_get\_gamepad\_input and outputs this status in a debug message.
