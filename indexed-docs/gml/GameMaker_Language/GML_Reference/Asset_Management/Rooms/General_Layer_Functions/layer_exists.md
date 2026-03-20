# layer\_exists

This function can be used to check if the given **layer** exists.

You supply the layer handle (which you get when you create the layer using [layer\_create()](layer_create.md)) or the layer name (as a string \- this will have a performance impact) and the function will return a *boolean* value of true if it exists or false if it does not.

  This function works within the scope of the current target room \- by default the room in which the function is called \- which can be set using the function [layer\_set\_target\_room()](layer_set_target_room.md).

 

#### Syntax:

layer\_exists(layer\_name)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_name | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The name of the layer (a string or handle) |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!layer\_exists(global.tileLayer))  

 {  

     global.tileLayer \= layer\_create(1000\);  

 }

The above code will check to see if the layer stored in the global variable actually exists, and if it does not then it is created.
