# title

With this function you can request that the XBox shows the profile card for the target user ID pointer. The function requires both the user ID pointer for the user that is *requesting* the information as well as the user ID pointer of the user to *target* and get the profile card of.

 

#### Syntax:

xboxlive\_show\_profile\_card\_for\_user(requesting\_user\_id, target\_user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| requesting\_user\_id |  | The user ID (a pointer) of the requesting user |
| target\_user\_id |  | The user ID (a pointer) of the user to get the profile card of |

 

 

#### Returns:

 

#### Example:

if (gamepad(0, gp\_start))  

 {  

     xboxlive\_show\_profile\_card\_for\_user(user\[0], user\[1]);  

 }

The above code checks for a gamepad button press and if one is detected it shows the profile card for the given user.
