# ini\_key\_delete

With this function you can remove the selected key (and its corresponding value) from an ini file.

 

#### Syntax:

ini\_key\_delete(section, key)

| Argument | Type | Description |
| --- | --- | --- |
| section |  | The section to delete a key from. |
| key |  | The key to delete. |

 

#### Returns:

 

#### Example:

ini\_open("savedata.ini");  
 ini\_write\_real("save1","Score",score);
   
 ini\_key\_delete("save1","Score");
   
 ini\_close();
 

This example will open "savedata.ini" and write a value to "save1" \> "Score". It will then delete the "Score" key and close the .ini file.
