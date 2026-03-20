# physics\_fixture\_set\_edge\_shape

This function defines an "edge" shape for the give fixture.

An edge shape is simply a line that will generate a collision when other fixtures overlap it, and can be very useful for generating (for example) terrain, or for creating borders around a room. The position of the edge is defined using *local* space, i.e.: the x/y position of the instance is considered (0, 0\), so this should be taken into consideration when creating them (in the code example below, the instance would have been placed at (0, 0\) in the room to avoid complications).

 

#### Syntax:

physics\_fixture\_set\_edge\_shape(fixture, local\_x1, local\_y1, local\_x2, local\_y2\)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | the index of the fixture |
| local\_x1 | [Real](../../../GML_Overview/Data_Types.md) | start x position for the edge |
| local\_y1 | [Real](../../../GML_Overview/Data_Types.md) | start y position for the edge |
| local\_x2 | [Real](../../../GML_Overview/Data_Types.md) | end x position for the edge |
| local\_y2 | [Real](../../../GML_Overview/Data_Types.md) | end y position for the edge |

 

#### Returns:

N/A

 

#### Example:

var \_xx \= 0;  

 var \_y1 \= room\_height \- 100;  

 var \_y2 \= room\_height \- 50 \- irandom(100\);  

 for (var i \= 0; i \< 10; i\+\+)  

 {  

     var \_fix \= physics\_fixture\_create();  

     physics\_fixture\_set\_edge\_shape(\_fix, \_xx, \_y1, \_xx \+ 50, \_y2\);  

     physics\_fixture\_bind(\_fix, id);  

     physics\_fixture\_delete(\_fix);  

     \_xx \+\= 50;  

     \_y1 \= y2;  

     \_y2 \= room\_height \- 50 \- irandom(100\);  

 }

The above code will create a line of "edge" fixtures with a variety of heights over the length of the room.
