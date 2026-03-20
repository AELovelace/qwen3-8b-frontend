# dbg\_watch

This function creates a watch for a variable within the current debug section.

You can also pass an array as the first argument, and the function will create a watch for each reference in the array.

This is simply used to monitor a variable's value, and cannot be used to change it. Look at the Debug View [Function Reference](The_Debug_Overlay.md#func_ref) for controls that allow variable modification.

Each value is converted to a [String](../../GML_Overview/Data_Types.md) and displayed.

 
 

#### Syntax:

dbg\_watch(ref\_or\_array, \[label])

| Argument | Type | Description |
| --- | --- | --- |
| ref\_or\_array | [Reference](../Variable_Functions/ref_create.md) or [Array](../../GML_Overview/Arrays.md) | A reference to a variable, created using [ref\_create](../Variable_Functions/ref_create.md), or an array containing references |
| label | [String](../../GML_Overview/Data_Types.md) | The label to show |

 

#### Returns:

[Debug Control](dbg_button.md)

 

#### Example:

Create Event

counter \= 0;  

  

dbg\_watch(ref\_create(self, "counter"), "Counter");
 

Step Event

counter \+\= 1;

The above code first initialises a variable counter in the Create event. It then adds a watch for this variable using dbg\_watch.

In the Step event, the counter is incremented, a change that will be shown by the watch.
