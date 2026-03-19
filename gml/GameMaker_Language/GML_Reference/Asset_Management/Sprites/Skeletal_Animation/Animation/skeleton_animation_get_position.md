# skeleton\_animation\_get\_position

This function will return the position of the animation on the specified animation track as a value ranging from 0 to 1\. This way you can get the track position as a percentage where the value 0 corresponds to 0% and the value 1 to 100%.

It will return \-1 if no animation is assigned to the specific track given or if the instance has no sprite set.

 

#### Syntax:

skeleton\_animation\_get\_position(track)

| Argument | Type | Description |
| --- | --- | --- |
| track | [Real](../../../../../GML_Overview/Data_Types.md) | The animation track to get the position of. |

 

#### Returns:

[Real](../../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_position \= skeleton\_animation\_get\_position(0\);  

 var \_position\_percent \= \_position \* 100;  

 show\_debug\_message("The skeleton animation position on track 0 is at " \+ string(\_position\_percent) \+ "%.");

The above code checks the current position of the skeleton animation assigned to track 0 and stores it in a temporary variable \_position. It then converts that value to a percentage by multiplying it by 100 and stores the result of that in another temporary variable \_position\_percent.  

 Finally it shows a debug message that displays the percent value.
