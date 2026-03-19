# title

This function will return the User ID pointer associated with the given gamepad index value, or pointer\_null if no user is associated with it. Note that this function should only be used with gamepad indices, and **not** with [xboxlive\_get\_user\_count()](xboxlive_get_user_count.md).

 

#### Syntax:

xboxlive\_user\_for\_pad(pad\_index);

| Argument | Type | Description |
| --- | --- | --- |
| pad\_index |  | The index (an integer) of the gamepad slot to check |

 

#### Returns:

Xbox User ID or pointer\_null

 

#### Example:

for(var i \= 0; i \< 11; \+\+i)  

 {  

     var u\_id \= xboxlive\_user\_for\_pad(i);  

     if (u\_id !\= pointer\_null)   

     {  

         pad\_name\[i] \= xboxlive\_gamedisplayname\_for\_user(u\_id);  

     }  

     else  

     {  

         pad\_name\[i] \= "Press Play";  

     }  

 }

The above code loops through all available pad slots and checks to see if there is a user ID pointer associated with it. If there is, an array is set with the user display name, otherwise the array is set to some default text.
