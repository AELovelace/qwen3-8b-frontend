# title

This function can be used to delete a stat from the stat manager for the given user ID. You supply the user ID as returned by (for example) the function [xboxlive\_get\_user()](../Users_And_Accounts/xboxlive_get_user.md), then the stat string to delete. This clears the stat value and removed it from the stat manager, meaning it will no longer be returned by the functions [xboxlive\_stats\_get\_stat\_names()](xboxlive_stats_get_stat_names.md) or [xboxlive\_stats\_get\_stat()](xboxlive_stats_get_stat.md).

The function will will return \-1 if there was an error or the user ID is invalid, or any other value if the function was successfully called

 

#### Syntax:

xboxlive\_stats\_delete\_stat(user\_id, stat);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id |  | The user ID pointer to delete the stat of |
| stat |  | The statistic to delete (a string) |

 

#### Returns:

 

#### Example:

for(var i \= 0; i \< xboxlive\_get\_user\_count(); i\+\+)  

 {  

     user\_id\[i] \= xboxlive\_get\_user(i);  

     xboxlive\_stats\_delete\_stat(user\_id\[i], "HighScore");  

 }

The above code loops through the connected users and deletes the specified stat from the stat manager for each one.
