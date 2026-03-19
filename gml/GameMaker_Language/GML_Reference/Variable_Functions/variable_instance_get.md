# variable\_instance\_get

With this function you can get the value from a given named variable. You supply the unique instance ID value (which can be found from the [Instance Properties](../../../The_Asset_Editors/Room_Properties/Layer_Properties.md) in the room editor, or is returned when you call the function [instance\_create\_layer()](../Asset_Management/Instances/instance_create_layer.md)) as well as the name of the variable to get the value of *as a string* (see example code below). The function will return the value held by the variable, or undefined if the variable does not exist.

**IMPORTANT!** If the variable you are getting does not exist then the function will return the keyword undefined and you may get errors that will stop the game from functioning, so if in doubt use the function [variable\_instance\_exists](variable_instance_exists.md) first.

 

#### Syntax:

variable\_instance\_get(instance\_id, name)

| Argument | Type | Description |
| --- | --- | --- |
| instance\_id | Instance ID | The unique ID value of the instance to use |
| name | String | The name of the variable to get (as a string) |

 

#### Returns:

Variable (any data type) or undefined (if the named variable does not exist)

 

#### Example:

if (variable\_instance\_exists(id, "shields"))   

 {  

     var ss \= variable\_instance\_get(id, "shields");  

 }  

 else  

 {  

     var ss \= \-1;  

 }

The above code will check to see if a variable exists and if it does then the value it holds is retrieved and stored in a local variable. If it does not exist, the local variable is set to \-1\.
