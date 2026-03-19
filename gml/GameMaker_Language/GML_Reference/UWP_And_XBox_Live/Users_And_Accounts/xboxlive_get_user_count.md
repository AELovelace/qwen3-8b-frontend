# title

With this function you can find the total number of users currently signed in to the XBox system. The return value will be an integer value, from 0 \- N, where N is the number of signed in users \-1\.

 

#### Syntax:

xboxlive\_get\_user\_count();

 

#### Returns:

 

#### Example:

for(var i \= 0; i \< xboxlive\_get\_user\_count(); \+\+i)  

 {  

     user\_id\[i] \= xboxlive\_get\_user(i);  

 }

The above loops through all the signed in users and stores their unique ID pointer in an array.
