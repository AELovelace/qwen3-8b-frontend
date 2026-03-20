# dbg\_view\_delete

This function deletes an existing debug view created using [dbg\_view](dbg_view.md). It returns true if the view was deleted otherwise it returns false.

 

#### Syntax:

dbg\_view\_delete(view)

| Argument | Type | Description |
| --- | --- | --- |
| view | [Debug View Pointer](dbg_view.md) | A pointer to a debug view |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

Create Event

debug\_view \= dbg\_view("View", true);

Key Pressed Event \- Space

dbg\_view\_delete(debug\_view);

The above code first creates a debug view using [dbg\_view](dbg_view.md) named "View" in the Create event and stores the pointer to it in an instance variable debug\_view.

In the Space Key Pressed event, the debug view is deleted using dbg\_view\_delete.
