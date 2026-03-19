# title

With this action you can add a key/value pair into the map data structure. You supply the variable that holds the map index (as returned by the action [Create Map](Create_Map.md)) and then give a "key" (which is the identifier
 within the map for a value), and then the "value" to be associated with that key. Both keys can be either integer values (like 0, 200, 36712, etc...) or strings (like "Name", "Shield" etc...), but the value can be any
 valid data type.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Map | The index (stored in a variable) of the map to set |
| Key | The key to set (integer or string) |
| Value | The value to be stored with the given key |

 

#### Example:

The above action block code creates a new map data structure and then sets three key/value
 entries in it.
