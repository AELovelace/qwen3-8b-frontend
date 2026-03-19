# physics\_joint\_enable\_motor

This function sets whether to enable or disable the motor on a physics joint that has a motor.

When you have a joint with a motor ([prismatic](physics_joint_prismatic_create.md) or [revolute](physics_joint_revolute_create.md)), you may want to be able to switch the motor on or off depending on variables and conditions within the game. For this, you need to have stored the index of the joint previously in a variable and then you can switch the motor on or off by using this function and setting the "motor" argument to true or false.

 

#### Syntax:

physics\_joint\_enable\_motor(joint, motor)

| Argument | Type | Description |
| --- | --- | --- |
| joint | [Physics Joint ID](Joints.md) | The joint that you wish to enable or disable the motor on |
| motor | [Boolean](../../../GML_Overview/Data_Types.md) | Whether you wish to turn the motor on (true) or off (false) |

 

#### Returns:

N/A

 

#### Example:

var t\_fix \= physics\_fixture\_create();  

 physics\_fixture\_set\_circle\_shape(t\_fix, sprite\_get\_width(sprite\_index) / 2\);  

  

 var o\_id \= instance\_create\_layer(x\+300, y, "Instances", obj\_Door);  

 physics\_fixture\_bind(t\_fix, id);  

 physics\_fixture\_bind(t\_fix, o\_id);  

  

 perma\_joint \= physics\_joint\_revolute\_create(id, o\_id, x\+25, y, \-90, 90, 1, 10, 2, 0, 0\);  

 physics\_joint\_enable\_motor(perma\_joint, 1\);  

 physics\_fixture\_delete(t\_fix);
 

The above code creates and defines a new fixture and then creates an instance of "obj\_Door", binding the created fixture to the two instances. They are then joined by a revolute joint with no motor and the angles limited to a \+/\- 90 degree swing, and we store the joint index in the variable "perma\_joint". We then switch the motor on using this variable, before finally deleting the fixture from memory as it is no longer needed.
