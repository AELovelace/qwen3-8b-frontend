# debug\_input\_playback

This function plays back previously recorded input.

The file can hold various types of input, depending on the types selected when the input was recorded using [debug\_input\_record](debug_input_record.md).

Regular input is blocked while recorded input is played back. This applies per type of input, e.g., if the loaded input contains only keyboard input, all keyboard input will be blocked during playback but mouse and touch input are still processed.

When the playback has finished, the [Async System](../../../The_Asset_Editors/Object_Properties/Async_Events/System.md) event will be triggered with the following properties in the async\_load map:

- "event\_type": "debug\_input\_playback\_stopped"

 
 

#### Syntax:

debug\_input\_playback(filename)

| Argument | Type | Description |
| --- | --- | --- |
| filename | [String](../../GML_Overview/Data_Types.md) | The path to the file storing previously recorded input data |

 

#### Returns:

N/A

 

#### Example:

debug\_input\_playback("input.data");

The above code plays back previously recorded input stored in a file named "input.data".
