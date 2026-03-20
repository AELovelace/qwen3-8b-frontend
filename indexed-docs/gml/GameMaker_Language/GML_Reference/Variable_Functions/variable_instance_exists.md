# variable\_instance\_exists

With this function you can check whether an instance scope variable exists or not. You supply the unique instance ID value (which can be found from the [Instance Properties](../../../The_Asset_Editors/Room_Properties/Layer_Properties.md) in the room editor, or is returned when you call the function [instance\_create\_layer()](../Asset_Management/Instances/instance_create_layer.md)) as well as the variable name to check for *as a string* (see example code below). The function will return true if a variable with the given name exists for the instance and false otherwise.

 

#### Syntax:

variable\_instance\_exists(instance\_id, name)

| Argument | Type | Description |
| --- | --- | --- |
| instance\_id | [Instance ID](../../../../GameMaker_Language/GML_Reference/Asset_Management/Instances/Instance_Variables/id.md) | The unique ID value of the instance to check |
| name | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of the variable to check for |

 

#### Returns:

[Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (!variable\_instance\_exists(id, "shields"))   

 {  

     shields \= 0;  

 }

The above code will check to see if the variable called "shields" exists in the instance running the code and if it does not then it is created and initialised to 0\.
