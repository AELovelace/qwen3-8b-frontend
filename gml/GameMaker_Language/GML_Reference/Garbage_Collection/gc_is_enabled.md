# gc\_is\_enabled

With this function you can check to see if the garbage collector is enabled or not. The function will return true if it is enabled or false otherwise.

 

#### Syntax:

gc\_is\_enabled()

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

if (!gc\_is\_enabled())  

 {  

     gc\_enable(true);  

 }

The above code checks to see if the garbage collector is enabled and if it isn't it enables it.
