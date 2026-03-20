# title

This function will search for a multi\-player session using the Session Template, matchmaking hopper and Secure Device Association template, which you should have created beforehand in the XDP dashboard. The user ID you can retrieve for a particular game pad by calling the [xboxlive\_user\_for\_pad()](../Users_And_Accounts/xboxlive_user_for_pad.md) function. The function will return a unique Request ID value, which can then be used to identify the correct [Social Asynchronous Event](../../../../The_Asset_Editors/Object_Properties/Async_Events/Social.md) for this function. This event will be triggered when the session has been created and will contain a DS Map in the variable [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) with the following key/value pairs:

- "requestid" – contains the request ID as returned by the calling function
- "status" – contains the string "session\_created" to inform you of what type of event has been triggered.
- "num\_results" – contains 1 or more if a session has been found, otherwise contains 0\.
- "sessionid*\*" – contains the session ID, or \-1 in case of failure  (*\<index/gt;* is a value from 0 to "num\_results" \- 1\).
- "sessionOwner*\*" – contains the ID of the session host if a session has been found  (*\* is a value from 0 to "num\_results" \- 1\).
- "error" – contains 0 on success, or \-1 in case of failure

 

#### Syntax:

xboxlive\_matchmaking\_find(user\_id, template, hopper, sdatemplate, \[matchattributes]);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id | Xbox User ID | The user ID pointer to use |
| template | String | The name of the session template |
| hopper | String | The name of the matchmaking hopper |
| sdatemplate | String | The name of the secure device association template |
| matchattributes | Real | OPTIONAL The match attributes |

 

#### Returns:

Async Request ID

 

#### Example:

var userID \= xboxone\_user\_for\_pad(global.PadIndex);  

 result \= xboxone\_matchmaking\_find(userID, "MatchTicketSession", "MatchTicketHopper", "PeerServerTraffic");

The above will retrieve the user ID for the user on the given gamepad and then try to find a matchmaking session for them.
