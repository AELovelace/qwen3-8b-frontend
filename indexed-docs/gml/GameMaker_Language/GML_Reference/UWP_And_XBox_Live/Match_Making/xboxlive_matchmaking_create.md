# title

This function will create a multi\-player session using the Session Template, matchmaking hopper and Secure Device Association template, which you should have created beforehand in the XDP dashboard. The user ID you can retrieve for a particular game pad by calling the [xboxlive\_user\_for\_pad()](../Users_And_Accounts/xboxlive_user_for_pad.md) function and visibility will be one of the following constants:

| [Xbox Match Visibility Constant](../../../../../GameMaker_Language/GML_Reference/UWP_And_XBox_Live/Match_Making/xboxlive_matchmaking_create.md) | |
| --- | --- |
| Constant | Description |
| xboxlive\_match\_visibility\_open | specifies that the session can be joined by the others. |
| xboxlive\_match\_visibility\_private | specifies that the session is not visible to users who are not session members. |
| xboxlive\_match\_visibility\_usetemplate | specifies that the value used in the session template should be used (this should normally be used as you can't override a template's value if one has been set in XDP). |

The function returns a unique Request ID value, which can then be used to identify the correct Social Asynchronous Event for this function. This event will be triggered when the session has been created and will contain a DS Map in the variable async\_load with the following key/value pairs:

- "requestid" – contains the request ID as returned by the calling function
- "status" – contains the string "session\_created" to inform you of what type of event has been triggered.
- "sessionid" – contains the session ID, or \-1 in case of failure
- "error" – contains 0 on success, or \-1 in case of failure
- "correlationid" \- the session handle for correlation with the function [xboxlive\_matchmaking\_join\_session()](xboxlive_matchmaking_join_session.md)

 

#### Syntax:

xboxlive\_matchmaking\_create(user\_id, visibility, template, hopper, sdatemplate, \[matchattributes]);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id | [Xbox User ID](../../../../../LINKGOESHERE) | The user ID pointer to use |
| visibility | [Xbox Match Visibility Constant](../../../../../GameMaker_Language/GML_Reference/UWP_And_XBox_Live/Match_Making/xboxlive_matchmaking_create.md) | One of the constants listed above |
| template | [String](../../../../../LINKGOESHERE) | The name of the session template |
| hopper | [String](../../../../../LINKGOESHERE) | The name of the matchmaking hopper |
| sdatemplate | [String](../../../../../LINKGOESHERE) | The name of the secure device association template |
| matchattributes | [Real](../../../../../LINKGOESHERE) | OPTIONAL The match attributes |

 

#### Returns:

[Async Request ID](../../../../../LINKGOESHERE)

 

#### Example:

var userID \= xboxlive\_user\_for\_pad(global.PadIndex);  

 result \= xboxlive\_matchmaking\_create(userID, xboxlive\_match\_visibility\_usetemplate, "MatchTicketSession", "MatchTicketHopper", "PeerServerTraffic");

The above will retrieve the user ID for the user on the given gamepad and then initialise a matchmaking session for them.
