# dbg\_section\_delete

This function deletes a debug section that was previously added with [dbg\_section](dbg_section.md). It returns true if the section was deleted otherwise it returns false.

 

#### Syntax:

dbg\_section\_delete(section)

| Argument | Type | Description |
| --- | --- | --- |
| section | [Debug Section Pointer](dbg_section.md) | A pointer to a debug section returned by [dbg\_section](dbg_section.md) |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

Create Event

config\_section \= dbg\_section("Config");

Key Pressed Event \- Space

dbg\_section\_delete(config\_section);

The above code first creates a new debug section using [dbg\_section](dbg_section.md) named "Config" in the Create event. Because no call to [dbg\_view](dbg_view.md) was made before, the section is added to a debug view named "Default".

In the Space Key Pressed Event, the debug section is deleted using dbg\_section\_delete.
