# title

This function converts the User ID pointer into a string.

 

#### Syntax:

xboxlive\_user\_id\_for\_user(user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id |  | The ID pointer of the user to check. |

 

#### Returns:

 

#### Example:

var \_uid \= xboxlive\_user\_for\_pad(0\);  
 uid\_string \= xboxlive\_user\_id\_for\_user(\_uid);

The above code gets the user ID pointer for the user assigned to the gamepad \[0] slot, and then saves that user ID as a string to an instance variable.
