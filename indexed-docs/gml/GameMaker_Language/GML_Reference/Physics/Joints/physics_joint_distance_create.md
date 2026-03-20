# physics\_joint\_distance\_create

This function creates a distance joint between two physics instances.

One of the simplest joints is a distance joint which says that the distance between two points on two instances must be constant. When you specify a distance joint the two instances should already be created and have a fixture assigned, then you define the two anchor points in room coordinates. The first anchor point is connected to instance 1, the second anchor point is connected to instance 2 and the distance between these points implies the length of the distance constraint. The image below shows how this works:

As you can see, the anchor points are specified as room coordinates so care must be taken when defining them, especially if the instances are being created at the same time as the joints rather than being placed in the room through the Room Editor. You should also realise that the joints are created independently of the size of the sprite of the instances or the fixtures they have attached. So, if you create a distance joint somewhere other than the origin of the instance, it is still valid and will constrain the two instances relative to the position at which it was created. If you set the col value to true then the two instances can interact and collide with each other but *only* if they have collision events. If it is set to false, however, they will not collide no matter what.

 

#### Syntax:

physics\_joint\_distance\_create(inst1, inst2, w\_anchor1\_x, w\_anchor1\_y, w\_anchor2\_x, w\_anchor2\_y, col)

| Argument | Type | Description |
| --- | --- | --- |
| inst1 | [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) | The first instance to connect with the joint |
| inst2 | [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) | The second instance to connect with the joint |
| w\_anchor1\_x | [Real](../../../GML_Overview/Data_Types.md) | The first x coordinate for the joint, within the game world |
| w\_anchor1\_y | [Real](../../../GML_Overview/Data_Types.md) | The first y coordinate for the joint, within the game world |
| w\_anchor2\_x | [Real](../../../GML_Overview/Data_Types.md) | The second x coordinate for the joint, within the game world |
| w\_anchor2\_y | [Real](../../../GML_Overview/Data_Types.md) | The second y coordinate for the joint, within the game world |
| col | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the two instances can collide (true) or not (false) |

 

#### Returns:

[Physics Joint ID](Joints.md)

 

#### Example:

var mainFixture, o\_id;  

 mainFixture \= physics\_fixture\_create();  

 physics\_fixture\_set\_circle\_shape(mainFixture, sprite\_get\_width(sprite\_index) / 2\);  

 o\_id\=instance\_create\_layer(x\+300, y, "Instances", obj\_Rudder);  

 physics\_fixture\_bind(mainFixture, id);  

 physics\_fixture\_bind(mainFixture, o\_id);  

 physics\_joint\_distance\_create(id, o\_id, x \+ 50, y, o\_id.x \- 50, o\_id.y, 0\);  

 physics\_fixture\_delete(mainFixture);

The above code creates and defines a new fixture and then creates an instance of "obj\_Rudder". The fixture is then assigned to the instance that is running the code as well as the newly created one and a joint is created between them. Finally the fixture is deleted as it is no longer needed.
