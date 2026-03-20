# title

With this function you can check whether the given user ID is in the list of users currently using the console, and the function will return true if they are, or false otherwise. You can get a User ID pointer with the function [xboxlive\_get\_user()](xboxlive_get_user.md).

 

 

#### Syntax:

xboxlive\_user\_is\_active(user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id |  | The ID pointer of the user to check. |

 

#### Returns:

 

#### Example:

global.PlayerNum \= 0;  

 global.Player\_ID \= array\_create();  

 for(var i \= 0; i \< xboxlive\_get\_user\_count(); \+\+i)  

 {  

     var \_uid \= xboxlive\_get\_user(i);  

     if (xboxlive\_user\_is\_active(\_uid))   

     {  

         global.Player\_ID\[global.PlayerNum\+\+] \= \_uid;  

     }  

 }

The above code loops through the user accounts and then checks to see if any of them are active. If they are, their user ID is added into a global array.
