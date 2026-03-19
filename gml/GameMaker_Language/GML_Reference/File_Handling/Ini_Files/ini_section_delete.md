# ini\_section\_delete

With this function you can delete a whole section of an ini file, which will also remove all key\-value pairs that are associated with it.

 

#### Syntax:

ini\_section\_delete(section)

| Argument | Type | Description |
| --- | --- | --- |
| section | [String](../../../GML_Overview/Data_Types.md) | The section to delete. |

 

#### Returns:

N/A

 

#### Example:

ini\_open("savedata.ini");  

 ini\_write\_real("save1", "Score", score );  

 ini\_section\_delete("save1");  

 ini\_close();

This example will open "savedata.ini" and write a value to "save1" \> "Score". It will then delete the "save1" section and close the .ini file.
