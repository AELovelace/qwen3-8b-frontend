# date\_leap\_year

This function will return true if the year component of the given datetime value is a leap year or false otherwise. This can be a handy function for things like Easter Eggs in your games, or for unlocking special content.

 

#### Syntax:

date\_leap\_year(date)

| Argument | Type | Description |
| --- | --- | --- |
| date |  | The datetime to use. |

 

#### Returns:

 

#### Example:

if (date\_leap\_year(date\_current\_datetime()))   

 {  

     if (!global.ExtraContent)   

     {  

         global.ExtraContent \= true;  

     }  

 }

The above code will check the current datetime to see if the year is a leap year or not. If it is it sets a global variable.
