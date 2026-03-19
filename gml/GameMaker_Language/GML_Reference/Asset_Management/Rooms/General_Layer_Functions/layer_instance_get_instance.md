# layer\_instance\_get\_instance

This function can be used to get the unique instance ID of the given instance element. You give the instance *element* ID (see the code example below for how to get this), and the function will return a handle holding the unique [instance id](../../Instances/Instance_Variables/id.md) for the element. If the element is not an instance, the function will return an invalid handle ([noone](../../../../GML_Overview/Instance Keywords/noone.md)).

 

#### Syntax:

layer\_instance\_get\_instance(element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| element\_id | [Instance Element ID](layer_get_all_elements.md) | The unique ID value of the instance element to get the ID of |

 

#### Returns:

[Object Instance](../../Instances/Instance_Variables/id.md)

 

#### Example:

var \_elements \= layer\_get\_all\_elements("Instances");  

 for (var i \= 0; i \< array\_length(\_elements); i\+\+)  

 {  

      if (layer\_get\_element\_type(\_elements\[i]) \=\= layerelementtype\_instance)  

      {  

          var \_element \= \_elements\[i];  

          var \_inst \= layer\_instance\_get\_instance(\_element);  

          \_inst.x \= \_inst.x \+ 10;  

      }  

 }

The above code will check get all the instance elements on a layer, then get their unique handles and use that to move them 10px to the right.
