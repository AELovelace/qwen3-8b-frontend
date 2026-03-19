# gamepad\_hat\_count

This function will return the *total* number of hats available for the gamepad connected to the given device "slot". Hats are usually (though not always) direction pads with up/down/left/right buttons.

  On the Windows target, hats are only available on DirectInput controllers (so, from slot 4 upwards).

 

#### Syntax:

gamepad\_hat\_count(device)

| Argument | Type | Description |
| --- | --- | --- |
| device | [Real](../../../GML_Overview/Data_Types.md) | Which gamepad device "slot" to check. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

h\_num \= gamepad\_hat\_count(4\);

The above code will return the number of hats available on the gamepad plugged into device "slot" 4 and store the value in the variable h\_num.
