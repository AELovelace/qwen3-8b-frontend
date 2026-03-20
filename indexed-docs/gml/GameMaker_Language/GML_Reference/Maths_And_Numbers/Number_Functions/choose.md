# choose

This function chooses a random value from the arguments you pass it.

Sometimes you want to specify something other than numbers for a random selection, or the numbers you want are not in any real order or within any set range. In these cases you would use choose to generate a random result. For example, say you want to create an object with a random sprite at the start, then you could use this function to set the sprite index to one of a set of given sprites. Note that you can have as many as you require (note that more arguments will mean that the function will be slower to parse).

 
#### Syntax:

choose(val0, val1, val2\... max\_val)

| Argument | Type | Description |
| --- | --- | --- |
| val0\... max\_val | [Any](../../../GML_Overview/Data_Types.md#variable) | Any type of value(s) |

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) (One of the given arguments)

 

#### Example:

sprite\_index \= choose(spr\_cactus, spr\_flower, spr\_tree, spr\_shrub);  

 hp \= choose(5, 8, 15, 32, 40\);  

 name \= choose("John", "Steven", "Graham", "Jack", "Emily", "Tina", "Jill", "Helen");

The above code uses choose to set a number of properties for the instance.
