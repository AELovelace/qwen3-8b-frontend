# title

This function will check the given user ID and return true if the player is a remote player, or false otherwise.

 

#### Syntax:

xboxlive\_user\_is\_remote(user\_id);

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

         if (!xboxlive\_user\_is\_remote(\_uid))   

         {  

             global.Remote\_Player\_ID\[global.PlayerNum\+\+] \= \_uid;  

         }  

     }  

 }

The above code loops through the user accounts and then checks to see if any of them are active. If they are, their user ID is added into a global array, only if they are not remote users.
