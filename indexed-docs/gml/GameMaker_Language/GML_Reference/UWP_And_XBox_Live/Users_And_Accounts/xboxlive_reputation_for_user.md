# title

With this function you can retrieve the Xbox Live reputation score for the given user ID pointer.

 

#### Syntax:

xboxlive\_reputation\_for\_user(requesting\_user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| requesting\_user\_id |  | The user ID (a pointer) of the user to check |

 

 

#### Returns:

Real

 

#### Example:

var \_a \= 0;  

 var \_num \= xboxlive\_get\_user\_count();  

 for (var i \= 0; i \< \_num; \+\+i)  

 {  

     var \_uid \= xboxlive\_get\_user(i);  

     if (\_uid !\= pointer\_null)   

     {  

         global.UserName\[\_a] \= xboxlive\_gamedisplayname\_for\_user(\_uid);  

         global.UserScore\[\_a] \= xboxlive\_gamerscore\_for\_user(\_uid);  

         global.UserRep\[\_a] \= xboxlive\_reputation\_for\_user(\_uid);  

         global.UserAvatar\[\_a] \= xboxlive\_sprite\_add\_from\_gamerpicture(\_uid, 256, 0, 0\);  

         \+\+a;  

     }  

 }

The above code loops through the logged in users and stores their gamer data in various global arrays.
