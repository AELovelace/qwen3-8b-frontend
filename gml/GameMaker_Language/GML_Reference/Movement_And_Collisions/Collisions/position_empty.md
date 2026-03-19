# position\_empty

This function will check to see if a given position enters into collision with *any instance* with a valid collision mask at the given position.

 

#### Syntax:

position\_empty(x, y)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position to check |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position to check |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_xx, \_yy;  

 \_xx \= random(room\_width);  

 \_yy \= random(room\_height);  

 if (position\_empty(\_xx, \_yy))  

 {  

     instance\_create\_layer(\_xx, \_yy, "Bullets", obj\_bomb);  

 }

This will check a random position somewhere in the room for a collision and if there is none it will create an instance of obj\_bomb.
