# dbg\_same\_line

This function tells GameMaker to place the next debug control on the same line as the current one (if both are single column controls).

See Also (placeholder)

1. [Topic List](#)

 

#### Syntax:

dbg\_same\_line()

 

#### Returns:

[Debug Control](dbg_button.md)

 

#### Example:

Create Event

dbg\_view("Custom View", true);  

 dbg\_button("Button1", function() {show\_debug\_message("Clicked Button1");});  

dbg\_same\_line();  

 dbg\_button("Button2", function() {show\_debug\_message("Clicked Button2");});
 

The code above first defines a new debug view using [dbg\_view](dbg_view.md) and sets it to be visible. It then adds two buttons directly to the debug view, meaning they will be added to a new debug section "Default". After that, two button controls are added using [dbg\_button](dbg_button.md), which will be placed on the same line because of the dbg\_same\_line between the two function calls. Both functions show a basic debug message.
