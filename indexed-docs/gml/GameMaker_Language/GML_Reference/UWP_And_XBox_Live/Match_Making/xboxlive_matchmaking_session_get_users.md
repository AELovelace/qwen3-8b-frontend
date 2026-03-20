# title

This function will create and populate a DS map with the details of the users in the specified session, or \-1 if there is an error. You can get the session ID pointer from the [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) DS map that is returned in the [Asynchronous Social Event](../../../../The_Asset_Editors/Object_Properties/Async_Events/Social.md) when you created or found a session (see [xboxlive\_matchmaking\_create()](xboxlive_matchmaking_create.md) for more details). The returned DS map will have the following key/value pairs:

- "**num\_results**" \- contains the number of users in the session
- "**userId\**" \- contains the ID of the user (\ is a value from 0 to "num\_results" \- 1\)
- "**userIsOwner\**" \- contains 1 if the user is the host, otherwise 0 (\ is a value from 0 to "num\_results" \- 1\)

 

#### Syntax:

xboxlive\_matchmaking\_session\_get\_users(session\_id);

| Argument | Type | Description |
| --- | --- | --- |
| session\_id |  | The session ID pointer to use |

 

#### Returns:

Async Request ID

 

#### Example:

var session\_map \= xboxlive\_matchmaking\_session\_get\_users(global.SessionID);  

 if (session\_map !\= \-1\)  

 {  

     for (var i \= 0; i \< session\_map\[? "num\_results"]; i\+\+)  

     {  

         if (session\_map\[? "userIsOwner" \+ string(i)] \=\= 1\)  

         {  

             global.OwnerID \= session\_map\[? "userId" \+ string(i)];  

         }  

     }  

 }

The above will retrieve the user data for all users participating in the matchmaking session and set a global variable to the ID of the session owner.
