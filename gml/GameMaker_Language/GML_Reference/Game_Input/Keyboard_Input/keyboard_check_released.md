# keyboard\_check\_released

With this function you can check to see if a key has been released or not.

Unlike the [keyboard\_check](keyboard_check.md) function, this function will only return true once in the step the key is lifted, i.e. when it switches from held down in the previous step to no longer held down in the current step. So for it to return true again, the key must be first pressed and then released again. In all other steps, the function returns false.

The function will take a keycode value as returned by the function [ord](../../Strings/ord.md) (only *capital* letters from A\-Z or numbers from 0\-9\), or any of the vk\_\* constants listed on the main [Keyboard Input](Keyboard_Input.md) page.

 

#### **Syntax:**

keyboard\_check\_released(key);

| Argument | Type | Description |
| --- | --- | --- |
| key | [Virtual Key Constant (vk\_\*)](../../../../../GameMaker_Language/GML_Reference/Game_Input/Keyboard_Input/Keyboard_Input.md) | The key to check the released state of. |

 

#### **Returns:**

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### **Example:**

if keyboard\_check\_released(ord("P"))  

 {  

     instance\_create\_layer(0, 0, "Controllers", obj\_Pause);  

 }

The above code will check to see if the "P" key has been released and if so, create an instance of obj\_Pause.
