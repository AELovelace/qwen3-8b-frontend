# ds\_priority\_add

With this function you can add a value (either a real number or a string) to a priority queue, at the same time assigning it a priority value.

 

#### Syntax:

ds\_priority\_add(id, val, priority)

| Argument | Type | Description |
| --- | --- | --- |
| id | DS Priority ID | The handle of the priority queue to add to. |
| val | Variable | The value to add to the priority queue. |
| priority | Real | The priority of the value to add. |

 

#### Returns:

N/A

 

#### Example:

ds\_priority\_add(ai\_priority, AI\_Search, 5\);

The above code adds a script function to the priority queue indexed in the variable "ai\_priority" and assigns it a priority of 5\.
