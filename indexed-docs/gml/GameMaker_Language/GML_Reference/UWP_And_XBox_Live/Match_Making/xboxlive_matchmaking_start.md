# title

This function must be called before you can start any multi\-player session for the user. It takes the User ID pointer, which you can retrieve for a particular game pad by calling the [xboxlive\_user\_for\_pad()](../Users_And_Accounts/xboxlive_user_for_pad.md) function, and will initialise the multi\-player API.

 

#### Syntax:

xboxlive\_matchmaking\_start(user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id |  | The user ID pointer to use |

 

#### Returns:

 

#### Example:

global.UserID \= xboxlive\_user\_for\_pad(global.PadIndex);  
 xboxlive\_matchmaking\_start(global.UserID);
 

The above code gets the user ID for the given pad index and then initialises multiplayer capabilities.
