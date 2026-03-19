# show\_question

This function creates a pop\-up message box with two buttons for "Yes" and "No". It returns true or false depending on which one of the two buttons the user presses.

 
It is recommended to use [show\_question\_async](../Asynchronous_Functions/Dialog/show_question_async.md) instead as it can be used on more platforms and it is good practice to use asynchronous dialog windows.

 

#### Syntax:

show\_question(str)

| Argument | Type | Description |
| --- | --- | --- |
| str | [String](../../GML_Overview/Data_Types.md) | The string to show in the pop\-up question. |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

if (score \> 500\) \&\& debug\_mode  

 {  

     if show\_question("Continue to next room?")  

     {  

         room\_goto(rm\_Level2\);  

     }  

     else game\_end();  

 }

The above code will check the score and if it is over 500, it will ask the user if they wish to continue or not and if the "yes" button is clicked it will go to another room, but if the "no" button is selected it will end the game.
