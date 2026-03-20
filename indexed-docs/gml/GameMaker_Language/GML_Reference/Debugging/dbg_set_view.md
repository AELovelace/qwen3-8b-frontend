# dbg\_set\_view

This function sets the current view to a view that was previously created using [dbg\_view](dbg_view.md). Any new debug controls will be created in the view set using this function.

 

#### Syntax:

dbg\_set\_view(view)

| Argument | Type | Description |
| --- | --- | --- |
| view | [Debug View Pointer](dbg_view.md) | A pointer to a debug view |

 

#### Returns:

N/A

 

#### Example:

var \_view1 \= dbg\_view("View 1", true);  

 var \_view2 \= dbg\_view("View 2", true);  

 dbg\_slider(ref\_create(global, "value2"), 0, 20, "Value2");  

 dbg\_set\_view(\_view1\);  

 dbg\_slider(ref\_create(global, "value"), 0, 20, "Value1");

This creates two views and adds a slider into View 2\. Then it uses dbg\_set\_view() to set the current view to View 1 and adds a slider into it.
