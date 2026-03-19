# title

This function will return one of four constants (shown below) to indicate the age\-range assigned to the specified user ID pointer.

 

#### Syntax:

xboxlive\_agegroup\_for\_user(user\_id);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id | [Xbox User ID](../../../../../LINKGOESHERE) | The user ID (a pointer) to check |

 

 

#### Returns:

[Xbox Age Group Constant](../../../../../GameMaker_Language/GML_Reference/UWP_And_XBox_Live/Users_And_Accounts/xboxlive_agegroup_for_user.md)

| [Xbox Age Group Constant](../../../../../GameMaker_Language/GML_Reference/UWP_And_XBox_Live/Users_And_Accounts/xboxlive_agegroup_for_user.md) | |
| --- | --- |
| Constant | Description |
| xboxlive\_agegroup\_unknown | The age group for the user is unknown |
| xboxlive\_agegroup\_child | The user age group is between 8 and 12 (inclusive) |
| xboxlive\_agegroup\_teen | The user age group is between 13 and 17 (inclusive, and between 13 and 19 in South Korea) |
| xboxlive\_agegroup\_adult | The user age group is 18 or over (or 20 and over in South Korea |

 

 

#### Example:

var \_age \= xboxlive\_agegroup\_for\_user(xboxlive\_get\_activating\_user());  

 if (\_age !\= xboxlive\_agegroup\_adult)   

 {  

     global.ContentControl \= true;  

 }  

 else global.ContentControl \= false;

The above code checks the age group of the activating user and sets a global variable to true or false depending on the returned constant.
