# title

This function will return true if the given user ID pointer is a guest user and false if they are not. You can get a User ID pointer with the function [xboxlive\_get\_user()](xboxlive_get_user.md).

 

#### Syntax:

xboxlive\_user\_is\_guest(user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id |  | The ID pointer of the user to check. |

 

#### Returns:

 

#### Example:

if xboxlive\_user\_is\_guest(user\_id\[0])  

 {  

     global.user\_name\[0] \= "GUEST";  

 }  

 else  

 {  

     global.user\_name\[0] \= xboxlive\_gamedisplayname\_for\_user(user\_id\[0]);  

 }

The above stores the activating user ID pointer in a global variable.
