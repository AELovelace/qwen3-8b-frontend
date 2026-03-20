# application\_surface\_is\_draw\_enabled

This function returns true if default drawing of the application surface is [enabled](application_surface_draw_enable.md), otherwise it returns false.

 

#### Syntax:

application\_surface\_is\_draw\_enabled()

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (keyboard\_check\_pressed(vk\_space))  

 {  

     if (application\_surface\_is\_draw\_enabled())  

     {  

         application\_surface\_draw\_enable(false);  

     }  

     else  

     {  

         application\_surface\_draw\_enable(true);  

     }  

 }

The above code checks for a key press and the toggles the application surface's automatic drawing on or off depending on its state (like in an options menu).
