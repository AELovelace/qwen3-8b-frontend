# weak\_ref\_alive

With this function you can check the [weak reference](#) to a struct to see if it is still "alive" or not. You supply the weak reference to check (as returned by the function [weak\_ref\_create](weak_ref_create.md)), and the function will return true if the struct is still being referenced somewhere or false if it's not and has been garbage collected. Note that if you supply a value that is not a weak reference, the function will return undefined.

 

#### Syntax:

weak\_ref\_alive(weak\_ref)

| Argument | Type | Description |
| --- | --- | --- |
| weak\_ref | [Struct Weak Reference](weak_ref_create.md) | The weak reference to the struct you want to check |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md) (or undefined)

 

#### Example:

if (weak\_ref\_alive(inventory\_ref))  

 {  

     inventory \= \-1;  

 }

The above code checks a weak reference to a struct and if it is still alive the variable referencing it is set to \-1, de\-referencing the struct and enabling it to be garbage collected.
