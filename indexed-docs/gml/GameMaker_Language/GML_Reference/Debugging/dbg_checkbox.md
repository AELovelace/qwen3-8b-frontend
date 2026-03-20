# dbg\_checkbox

This function creates a checkbox control within the current debug section.

The checkbox takes the reference of a [Boolean](../../GML_Overview/Data_Types.md) variable. Clicking it toggles the variable. You can also pass an array of references, in which case a new checkbox will be created for each reference in the array.

 
 

#### Syntax:

dbg\_checkbox(ref\_or\_array, \[label])

| Argument | Type | Description |
| --- | --- | --- |
| ref\_or\_array | [Reference](../Variable_Functions/ref_create.md) or [Array](../../GML_Overview/Arrays.md) | A reference to a [Boolean](../../GML_Overview/Data_Types.md) variable created using [ref\_create](../Variable_Functions/ref_create.md), or an array of references |
| label | [String](../../GML_Overview/Data_Types.md) | A label to display next to the checkbox |

 

#### Returns:

[Debug Control](dbg_button.md)

 

#### Example:

Create Event

toggle \= false;  

  

 var \_ref\_to\_toggle \= ref\_create(self, "toggle");  

dbg\_checkbox(\_ref\_to\_toggle, "The Toggle Switch");
 

The code above sets a boolean variable toggle in the Create event. It creates a reference to the variable using [ref\_create](../Variable_Functions/ref_create.md), stores it in a local variable \_ref\_to\_toggle and passes that to dbg\_checkbox. Since no calls were made to [dbg\_view](dbg_view.md) or [dbg\_section](dbg_section.md), a new view "Default" and a new section "Default" are created that the checkbox control is added to. The checkbox will show a text label "The Toggle Switch" next to it.
