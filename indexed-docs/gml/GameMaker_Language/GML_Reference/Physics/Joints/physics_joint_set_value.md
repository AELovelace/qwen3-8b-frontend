# physics\_joint\_set\_value

This function sets the value of the joint property corresponding to the given joint constant to the given value.

Certain joint properties can be changed and set even after the creation of the joint. There are a number of constants that can be used in this function and they can be found here: [Physics Joint Constants](Physics_Joint_Constants.md).

 

#### Syntax:

physics\_joint\_set\_value(joint, field, value)

| Argument | Type | Description |
| --- | --- | --- |
| joint | [Physics Joint ID](Joints.md) | The index of the joint that you wish to change |
| field | [Physics Joint Constant](Physics_Joint_Constants.md) | The constant for the joint property that you wish to change |
| value | [Real](../../../GML_Overview/Data_Types.md) | The new value for the joint property |

 

#### Returns:

N/A

 

#### Example:

if (physics\_joint\_get\_value(revJoint, phy\_joint\_max\_motor\_torque) \< 2\)  

 {  

     physics\_joint\_set\_value(revJoint, phy\_joint\_max\_motor\_torque, 2\);  

 }

The above code checks to see if the joints maximum motor torque is set to less than 2 and if it is it then sets it to 2\.
