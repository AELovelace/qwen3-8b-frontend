# gpu\_get\_ztestenable

This function can be used to retrieve whether z\-testing is enabled (the function returns true) or not (the function returns false).

The default value is that z\-testing is *disabled*, so the function will return false.

 

#### Syntax:

gpu\_get\_ztestenable()

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (gpu\_get\_ztestenable() \=\= false)  

 {  

     gpu\_set\_ztestenable(true);  

 }

The above code checks to see if z\-testing is enabled or not and if it is disabled it is then enabled again.
