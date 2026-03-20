# physics\_fixture\_set\_polygon\_shape

This function tells the given fixture to use a polygon shape. The points must be specified after calling this function using [physics\_fixture\_add\_point](physics_fixture_add_point.md).

Note that the polygon is closed when the fixture is bound to an instance. Also note that this function *must* be called before defining any points, and you must also have at least three points defined for your polygon before binding it to an instance or you will get an error.

 

#### Syntax:

physics\_fixture\_set\_polygon\_shape(fixture)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | the index of the fixture |

 

#### Returns:

N/A

 

#### Example:

physics\_fixture\_set\_polygon\_shape(fix\_ship);  

 physics\_fixture\_add\_point(fix\_ship, 0,0\);  

 physics\_fixture\_add\_point(fix\_ship, \-40, 100\);  

 physics\_fixture\_add\_point(fix\_ship, 40, 100\);

The code above will apply a polygon shape to the fixture indexed in the variable fix\_ship and then defines three points to create a triangular shape.
