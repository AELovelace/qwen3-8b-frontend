# dbg\_set\_section

This function sets the current section to a section that was previously created using [dbg\_section](dbg_section.md). Any new debug controls will be created in the section set using this function.

 

#### Syntax:

dbg\_set\_section(section)

| Argument | Type | Description |
| --- | --- | --- |
| section | [Debug Section Pointer](dbg_section.md) | A pointer to a debug section returned by [dbg\_section](dbg_section.md) |

 

#### Returns:

N/A

 

#### Example:

var \_view1 \= dbg\_view("View", true);  

 var \_sec1 \= dbg\_section("Section 1");  

 var \_sec2 \= dbg\_section("Section 2");  

 dbg\_slider(ref\_create(global, "value2"), 0, 20, "Value2");  

 dbg\_set\_section(\_sec1\);  

 dbg\_slider(ref\_create(global, "value"), 0, 20, "Value1");

This creates two sections and adds a slider into Section 2\. Then it uses dbg\_set\_section() to set the current section to Section 1 and adds a slider into it.
