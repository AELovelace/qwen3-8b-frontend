# device\_mouse\_raw\_y

This function returns raw y position of the touch on a device. What this means is that it returns the actual device definition of the y position that is being touched, *not* the GameMaker one, and as such will ignore things like view position and scaling. Note that the maximum number of device touches that can be detected will depend very much on the device being used and the OS it runs

**NOTE**: This function is very much device dependent and you should experiment first with the desired target module and device to see what exactly is returned.

 

#### Syntax:

device\_mouse\_raw\_y(device)

| Argument | Type | Description |
| --- | --- | --- |
| device |  | The device (from 0 \- *n*) that is being checked. |

 

#### Returns:

 

#### Example:

if (device\_mouse\_check\_button(0, mb\_left) \&\& device\_mouse\_check\_button(1, mb\_left))   

 {  

     x\_av \= mean(device\_mouse\_raw\_x(0\), device\_mouse\_raw\_x(1\));  

     y\_av \= mean(device\_mouse\_raw\_y(0\), device\_mouse\_raw\_y(1\));  

 }

The above code checks to see if device1 and device2 are being pressed, and if they are it calculates the average position of the x/y coordinates between each press point.
