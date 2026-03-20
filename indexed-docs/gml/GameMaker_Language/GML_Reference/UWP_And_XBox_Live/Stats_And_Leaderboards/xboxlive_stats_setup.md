# title

This function needs to be called before you can use any of the other Xbox Live stat functions, and simply initialises the required libraries on the system. The "user\_id" argument is the raw user ID as returned by the function [xboxlive\_get\_user()](../Users_And_Accounts/xboxlive_get_user.md), while the "service\_config" and "title\_id" is the unique ID for your game on the Xbox Live Dev Center.

This function is only for use with Event\-Based (2013\) stats.

 

#### Syntax:

xboxlive\_stats\_setup(user\_id, service\_config\_id, title\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id | Xbox User ID | The ID pointer of the user to check. |
| service\_config\_id | String | This is the config\_id string for the game. |
| title\_id | String | The unique ID for your game on the Xbox Dev Center. |

 

#### Returns:

N/A

 

#### Example:

var user \= xboxlive\_get\_user(0\);  

 xboxlive\_stats\_setup(user, "4d61a1aa\-61ac\-4541\-badd\-31f91244fea6", $1244FEA6\);

The above code initialises the stats system for the given user ID.
