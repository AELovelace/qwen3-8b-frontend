# device\_mouse\_y

This function returns the y position of a touch on the device. If you are running this on a the HTML5 or PC and Mac modules then this value is updated constantly, as long as the device (usually a mouse) is plugged in, however for mobile devices, this will only be updated while the screen is being touched and note that the maximum number of touches that can be detected will depend very much on the device being used and the OS it runs.

 

#### Syntax:

device\_mouse\_y(device)

| Argument | Type | Description |
| --- | --- | --- |
| device |  | The device (from 0 \- *n*) that is being checked. |

 

#### Returns:

 

#### Example:

if (device\_mouse\_check\_button(0, mb\_left))   

 {  

     if (device\_mouse\_y(0\) \> y\-32 \&\& device\_mouse\_y(0\) \< y\+32\)   

     {  

         pressed \= true;  

     }  

     else  

     {  

         pressed \= false;  

     }  

 }

The above code checks to see if the device is being pressed and if so it then polls the device y position to see if it is within the parameters. If it is it sets the variable "pressed" to true, other wise it sets it to false.
