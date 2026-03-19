# title

This function can be used to end a matchmaking session for the given user.

 

#### Syntax:

xboxlive\_matchmaking\_stop(user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id |  | The user ID pointer to use |

 

#### Returns:

 

#### Example:

if !xboxlive\_user\_is\_signed\_in(user\_id\[0])  

 {  

     xboxlive\_matchmaking\_stop(user\_id\[0]);  

 }

The above code will end the matchmaking session for the given user.
