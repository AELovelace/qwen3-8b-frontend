# skeleton\_animation\_clear

This function will clear the specified animation track of all animations, ready to be reassigned.

It can optionally reset the skeleton to its setup pose in a given amount of time.

 

#### Syntax:

skeleton\_animation\_clear(track, \[reset], \[duration])

| Argument | Type | Description |
| --- | --- | --- |
| track | [Real](../../../../../GML_Overview/Data_Types.md) | The animation track to clear. |
| reset | [Boolean](../../../../../GML_Overview/Data_Types.md) | Whether to reset the skeleton to its setup pose. Default is false. |
| duration | [Real](../../../../../GML_Overview/Data_Types.md) | How long animating the skeleton to setup pose should take, in seconds. |

 

#### Returns:

N/A

 

#### Example 1: Basic Use

if (mouse\_check\_button(mb\_right))  

 {  

     skeleton\_animation\_clear(1\);  

 }

The above code will clear the animation track 1 if the right mouse button is pressed.

 

#### Example 2: Resetting to Setup Pose

skeleton\_animation\_clear(1, true, 1\);

The above code clears animation track 1 of the skeletal animation assigned to the current instance and resets it to its setup pose.
