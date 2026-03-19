# id

This **read\-only** variable holds the unique identifying handle for the instance.

Every instance that you create \- whether through code or by adding it to a room in the Room Editor \- is given a handle that is used internally to identify this instance and the variable id is what you can use to reference it. The id is also returned (and can be stored in a variable) when an instance is created using [instance\_create\_layer](../instance_create_layer.md) or [instance\_create\_depth](../instance_create_depth.md) as well as other instance functions.

  The value of this variable is different from the [instance\_id](../instance_id.md) array which contains all the IDs of all the currently active instances.

  Instances that you add to a room in the Room Editor can be referenced directly in your code through the name given there (e.g. inst\_3FFB2F7A).

 

#### Syntax:

id

 

#### Returns:

[Object Instance](id.md)

 

#### Example:

for (var i \= 0; i \< instance\_count; i\+\+)  

 {  

     if (instance\_id\[i] !\= id)  

     {  

         instance\_id\[i].scr \+\= 5;  

     }  

 }

The above code adds 5 to the scr variable for every active instance in the room, except the one running the code. It does this by looping through ALL the active instances (using the [instance\_id](../instance_id.md) array to return each active instance's ID) and comparing them against the built\-in id variable, which is the ID of the original instance running the code.
