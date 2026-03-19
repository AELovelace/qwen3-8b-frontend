# gamepad\_button\_count

This function will return the *total* number of buttons available for the gamepad connected to the given device "slot".

 

#### Syntax:

gamepad\_button\_count(device)

| Argument | Type | Description |
| --- | --- | --- |
| device | [Real](../../../GML_Overview/Data_Types.md) | Which gamepad device "slot" to check. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

b\_num \= gamepad\_button\_count(0\);

The above code will return the number of buttons available on the gamepad plugged into device "slot" 0 and store the value in the variable "b\_num".
