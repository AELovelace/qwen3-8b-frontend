# physics\_fixture\_set\_chain\_shape

This function tells the given fixture to use a "chain" shape, which consists of a number of points that are connected using edge shapes. The points are specified after calling this function using [physics\_fixture\_add\_point](physics_fixture_add_point.md).

The function takes the index (ID) of the fixture and you can tell the fixture to loop or not. Setting this to true will connect the last point to the first point with an edge, while setting it to false will not. Note that this function prepares the fixture to accept the points required to make the chain, and these should be added after calling this function using [physics\_fixture\_add\_point](physics_fixture_add_point.md), much as you would when building a polygon fixture.

When creating a chain fixture, you must give it at least two points but you are not limited in the number of subsequent points that you can add to make up the finished fixture.

 

#### Syntax:

physics\_fixture\_set\_chain\_shape(fixture, loop)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | The index of the fixture |
| loop | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to close the chain (true) or not (false) |

 

#### Returns:

N/A

 

#### Example:

var \_xx \= \-100;  

 var \_yy \= room\_height / 2;  

 var \_fix \= physics\_fixture\_create(); physics\_fixture\_set\_chain\_shape(\_fix, false);  

 for (var i \= 0; i \< 10; i\+\+)  

 {  

     physics\_fixture\_add\_point(\_fix, \_xx, \_yy);  

     \_xx \+\= 50 \+ random(150\);  

     \_yy \= (room\_height / 2\) \- 250 \+ irandom(500\);  

 }  

 physics\_fixture\_bind(\_fix, id);

The above code will create a line of "edge" fixtures with a variety of heights over the length of the room.
