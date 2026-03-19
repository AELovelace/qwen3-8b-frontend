# title

With this function you can find out how many pad "slots" are active for the current user (see [xboxlive\_pad\_for\_user()](xboxlive_pad_for_user.md) for further details).

 

#### Syntax:

xboxlive\_pad\_count\_for\_user(user\_id, slot);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id |  | The user ID (a pointer) to check |

 

#### Returns:

 

#### Example:

global.slots\[0] \= xboxlive\_pad\_count\_for\_user(user\_id\[0])

The above code stores the number of pads associated with the given user ID pointer.
