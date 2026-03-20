# keyboard\_set\_numlock

You can use this function to switch the keypad number\-lock on or off (set to **true** for on, and **false** for off).

**NOTE** This functionality is only available in the Windows target builds and will not function on any other device.

 

#### **Syntax:**

keyboard\_set\_numlock(value);

| Argument | Type | Description |
| --- | --- | --- |
| value | [Boolean](../../../GML_Overview/Data_Types.md) | Set this to true for "on" and false for "off" |

 

#### **Returns:**

N/A

 

#### **Example:**

if (keyboard\_get\_numlock())  

 {  

     keyboard\_set\_numlock(false);  

 }  

 else  

 {  

     keyboard\_set\_numlock(true);  

 }

The above example code will get the state of the numberlock key and if it is on (true) it will set it to off (false) and vice versa.
