# audio\_group\_set\_gain

With this function you can fade a group of sounds in or out over a given length of time, or it can be used to set the group gain instantly.

The time is measured in milliseconds, and the function requires that you input a final level of gain for the group to have reached by the end of that time. This gain can be between 0 (silent) and 1 (full volume) and the scale is linear, such that a value of 0\.5 would be half volume. To instantly change the gain, simply leave out the time argument or set it to 0\.

 
#### Syntax:

audio\_group\_set\_gain(groupID, volume, \[time])

| Argument | Type | Description |
| --- | --- | --- |
| groupID | [Audio Group ID](Audio_Groups.md) | The index of the audio group to set the gain for (as defined in the [Audio Groups](../../../../../Settings/Audio_Groups.md) window) |
| volume | [Real](../../../../GML_Overview/Data_Types.md) | The final value for the group volume. |
| time | [Real](../../../../GML_Overview/Data_Types.md) | The length of the change in gain in milliseconds. Defaults to 0 (instantaneous change) if not passed. |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_space))  

 {  

     audio\_group\_set\_gain(audiogroup1, 0, 5000\);  

 }

The above code checks for the "space" key and then fades all the audio for "audiogroup1" down to 0 over 5 seconds.
