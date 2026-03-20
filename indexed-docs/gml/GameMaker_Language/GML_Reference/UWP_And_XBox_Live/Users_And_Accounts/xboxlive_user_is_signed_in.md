# title

The function will check to see if a user is signed\-in and return true if there is and false otherwise. If no user is signed in then you can call the function [xboxlive\_show\_account\_picker()](xboxlive_show_account_picker.md) to open the account picker and prompt them to sign\-in.

 

#### Syntax:

xboxlive\_user\_is\_signed\_in();

 

#### Returns:

 

#### Example:

if (!xboxlive\_user\_is\_signed\_in())   

 {  

     if (!xboxlive\_user\_is\_signing\_in())   

     {  

         xboxlive\_show\_account\_picker();  

     }  

 }  

 else  

 {  

     global.GamerTag \= xboxlive\_gamertag\_for\_user();  

 }

The above code checks to see if a user is signed\-in to XBox Live and if they are signed\-in, the code will get the gamertag for the user and store it in a global variable for future use. If they are not signed\-in then the code checks to see if they are in the process of signing\-in, in which case nothing further will happen, and if they are not, then it will open the account picker, prompting them to sign\-in.
