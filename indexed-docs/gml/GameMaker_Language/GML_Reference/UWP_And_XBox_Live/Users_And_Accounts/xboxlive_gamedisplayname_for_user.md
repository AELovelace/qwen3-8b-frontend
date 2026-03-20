# title

With this function you can retrieve the display name \- as a string \- from the user ID pointer given. Note that if the user is local then the returned value is simply a string of the their display name, but if it is a remote user then the string will be their gamertag which can then be used, for example, for muting/unmuting in voice chat.

 

#### Syntax:

xboxlive\_gamedisplayname\_for\_user(user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id |  | The ID pointer of the user to check. |

 

#### Returns:

 

#### Example:

for(var i \= 0; i \< xboxlive\_get\_user\_count(); \+\+i)  

 {  

     user\_id\[i] \= xboxlive\_get\_user(i);  

     user\_name\[i] \= xboxlive\_gamedisplayname\_for\_user(user\_id\[i]);  

 }

The above code gets the user ID pointer for each available user account and then stores the pointer along with the display name in two arrays.
