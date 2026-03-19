# gpu\_get\_zwriteenable

This function can be used to retrieve whether z\-writing is enabled (the function returns true) or not (the function returns false).

The default value is that z\-writing is *enabled*, so the function will return true.

 

#### Syntax:

gpu\_get\_zwriteenable()

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (gpu\_get\_zwriteenable() \=\= false)  

 {  

     gpu\_set\_zwriteenable(true);  

 }

The above code checks to see if z\-writing is enabled or not and if it is disabled it is then enabled again.
