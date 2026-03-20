# title

This function sets a (previously created) session to be available for other users to join through the system UI. A user only has one joinable session at once, and when they leave the session (or the session ends) this will be cleared, however you can clear it manually by passing \-1 in for the session argument.

 

#### Syntax:

xboxlive\_matchmaking\_set\_joinable\_session(local\_user, session\_that\_is\_joinable);

| Argument | Type | Description |
| --- | --- | --- |
| local\_user |  | The local user ID pointer. |
| session\_that\_is\_joinable |  | The session ID to make joinable, or \-1\. |

 

#### Returns:

 

#### Example:

if (global.session\_ID !\= \-1\)  

 {  

     xboxlive\_matchmaking\_set\_joinable\_session(xboxlive\_user\_for\_pad(0\), global.session\_ID);  

 }

The above code checks for a valid session ID value, and if one is detected it sets the session to be joinable.
