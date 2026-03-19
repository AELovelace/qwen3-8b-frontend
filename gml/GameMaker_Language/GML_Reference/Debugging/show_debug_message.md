# show\_debug\_message

This function shows a custom debug message in [The Output Window](../../../Introduction/The_Output_Window.md) and [The Debug Overlay](The_Debug_Overlay.md) at runtime.

The syntax of this function is identical to that of the [string](../Strings/string.md) function; aside from a single argument it can also take a [Format String](../Strings/string.md#h) with placeholders and additional arguments to replace the placeholders with.

 
Debug messages shown with this function will be shown in the [Compiler Output Window](../../../Introduction/The_Output_Window.md) at the bottom of the IDE as well as in the [Graph View](../../../IDE_Tools/The_Debugger.md) of the debugger when running the game in Debug Mode. If you only want to see messages in Debug Mode then you should probably be using [debug\_event](debug_event.md) instead.

  See [Strings](../Strings/Strings.md) for the reference on the various ways in which you can add variables to strings.

 

#### Syntax:

show\_debug\_message(value\_or\_format \[, value1, value2, ... max\_val])

| Argument | Type | Description |
| --- | --- | --- |
| value\_or\_format | [Any](../../GML_Overview/Data_Types.md#variable) (if value) or [String](../../GML_Overview/Data_Types.md) (if format) | The value to be turned into a string. |
| \[, value1, value2, ... max\_val] | [Any](../../GML_Overview/Data_Types.md#variable) | The values to be inserted at the placeholder positions. |

 

#### Returns:

N/A

 

#### Example 1: Basic Use

show\_debug\_message("Starting...");  

show\_debug\_message(\[3, 2, 1]);  

show\_debug\_message("Display Width:" \+ string(display\_get\_width()));  

show\_debug\_message($"Display Height: {display\_get\_height()}");
 

The above code shows a few calls to show\_debug\_message, where each call uses a different way to create the string that is output by the function. The first call to the function takes a string literal as the parameter, the second call takes an array, which can automatically be converted to its string representation, the third call takes a concatenation of a string and a variable converted to string using the [string](../Strings/string.md) function and the last one takes a template string.

 

#### **Example 2: Format String**

show\_debug\_message("Instances:");  

 for(var i \= 0;i \< instance\_count;i\+\+)  

 {  

     var \_id \= instance\_id\[i];  

     var \_obj \= object\_get\_name(\_id.object\_index);  

     var \_x \= \_id.x;  

     var \_y \= \_id.y;  

     show\_debug\_message("{0} ({1}) at ({2}, {3})", \_id, \_obj, \_x, \_y);  

 }

The above code outputs a debug message for every active instance in the room, using a format string that determines how the information is displayed.

In a [for](../../GML_Overview/Language_Features/for.md) loop the [instance\_id](../Asset_Management/Instances/instance_id.md) array is looped through and a few variables are retrieved for every instance in it: its [id](../Asset_Management/Instances/Instance_Variables/id.md), its [object\_index](../Asset_Management/Objects/object_index.md) (replaced with the more readable [object name](../Asset_Management/Objects/object_get_name.md)) and its [x](../Asset_Management/Instances/Instance_Variables/x.md) and [y](../Asset_Management/Instances/Instance_Variables/y.md). show\_debug\_message is then called with a format string as the first parameter and the values to be inserted into it are passed as the next parameters.

The output will look as follows:

Instances:  

 ref instance 100000 (obj\_enemy) at (832, 256\)  

 ref instance 100001 (obj\_player) at (960, 544\)  

 ref instance 100002 (obj\_enemy) at (128, 480\)  

 ref instance 100003 (obj\_enemy) at (640, 576\)
