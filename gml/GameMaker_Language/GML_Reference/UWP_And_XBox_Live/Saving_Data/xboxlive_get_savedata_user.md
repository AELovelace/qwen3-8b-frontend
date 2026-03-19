# title

This function returns the user ID pointer currently associated with file saving (or the constant pointer\_null if no user ID is currently being used). See [xboxlive\_set\_savedata\_user()](xboxlive_set_savedata_user.md) for further details.

 

#### Syntax:

xboxlive\_get\_savedata\_user();

 

#### Returns:

Xbox User ID or pointer\_null

 

#### Example:

if (xboxlive\_get\_savedata\_user() !\= user\_id\[0])  

 {  

     xboxlive\_set\_savedata\_user(user\_id\[0]);  

 }

The above code checks to see if a user is currently assigned as the save target, and if they are not then they are assigned.
