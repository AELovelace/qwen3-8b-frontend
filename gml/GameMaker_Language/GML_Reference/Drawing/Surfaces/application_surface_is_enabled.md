# application\_surface\_is\_enabled

This function returns true if the application surface is being used for drawing, or false if the screen buffer is being used.

 

#### Syntax:

application\_surface\_is\_enabled()

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (keyboard\_check\_pressed(vk\_space))  

 {  

     if (application\_surface\_is\_enabled())  

     {  

         application\_surface\_enable(false);  

     }  

     else  

     {  

         application\_surface\_enable(true);  

     }  

 }

The above code checks for a key press and the toggles the application surface on or off depending on its state (like in an options menu).
