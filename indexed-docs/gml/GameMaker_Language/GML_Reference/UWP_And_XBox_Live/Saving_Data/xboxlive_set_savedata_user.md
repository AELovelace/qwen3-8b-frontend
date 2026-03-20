# title

This function specifies that future file operations which operate in the save game area (i.e. all file writes, and reads from files that aren't in the bundle area) will be associated with the specified user ID pointer. This can be called as often as necessary to redirect save data to the appropriate user, or you can use the constant pointer\_null to save to the generic machine storage area.

 

#### Syntax:

xboxlive\_set\_savedata\_user(user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id | Xbox User ID or pointer\_null | The user ID (a pointer) to set for saving, or pointer\_null |

 

#### Returns:

N/A

 

#### Example:

if (xboxlive\_get\_savedata\_user() !\= user\_id\[0])  

 {  

     xboxlive\_set\_savedata\_user(user\_id\[0]);  

 }

The above code checks to see if a user is currently assigned as the save target, and if they are not then they are assigned.
