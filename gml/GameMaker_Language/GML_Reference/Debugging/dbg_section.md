# dbg\_section

This function creates a section in the current view and shows it in [The Debug Overlay](The_Debug_Overlay.md). A debug section groups together multiple debug controls inside a debug view.

The active section can later be changed using [dbg\_set\_section](dbg_set_section.md).

  If no debug view is active then the section is added to a new debug view named "Default".

### Usage Notes

- Most controls span two columns, others only a single one ([dbg\_text](dbg_text.md) and [dbg\_button](dbg_button.md)).
- Two single\-column controls can be placed on the same row by calling [dbg\_same\_line](dbg_same_line.md).
- A debug section's contents can be copy\-pasted to and from the clipboard as [JSON](#) using the **Copy** and **Paste** buttons.

 

#### Syntax:

dbg\_section(name \[, open])

| Argument | Type | Description |
| --- | --- | --- |
| name | [String](../../GML_Overview/Data_Types.md) | The name of the new debug section |
| open | [Boolean](../../GML_Overview/Data_Types.md) | true if the section should be open when it's created, false if not (default is true) |

 

#### Returns:

[Debug Section Pointer](dbg_section.md)

 

#### Example:

dbg\_view("CustomDebugView");  

dbg\_section("Player Variables");
 

The code above creates a new debug view using [dbg\_view](dbg_view.md) named "CustomDebugView" and adds a new section "Player Variables" to it using dbg\_section.
