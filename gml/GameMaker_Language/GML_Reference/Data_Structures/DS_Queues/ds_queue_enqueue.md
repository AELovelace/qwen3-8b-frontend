# ds\_queue\_enqueue

This function will add a value (real or string) onto the tail of the DS queue. The function can take a further 14 optional arguments (making a total of 15 possible additions), permitting you to add multiple values consecutively to the tail of the queue in a single call.

 

#### Syntax:

ds\_queue\_enqueue(id, val \[, val2, ... val15])

| Argument | Type | Description |
| --- | --- | --- |
| id |  | The handle of the queue to add to. |
| val |  | The value to add to the queue. |
| \[val2, ... val15] |  | Optional values to be added to the queue. |

 

#### Returns:

 

#### Example:

move\_queue \= ds\_queue\_create();
   

 ds\_queue\_enqueue(move\_queue, x \+ 200\);
   

 ds\_queue\_enqueue(move\_queue, y);
   

 ds\_queue\_enqueue(move\_queue, x \+ 200\);
   

 ds\_queue\_enqueue(move\_queue, y \+ 200\);
   

 ds\_queue\_enqueue(move\_queue, x);
   

 ds\_queue\_enqueue(move\_queue, y \+ 200\);
   

 ds\_queue\_enqueue(move\_queue, x);
   

 ds\_queue\_enqueue(move\_queue, y);

The above code creates a new DS queue and stores its index in the variable "move\_queue". It then pushes a number of values onto the queue for future use.
