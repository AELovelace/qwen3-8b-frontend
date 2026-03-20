# debug\_input\_record

This function starts recording various types of input.

The types of input that you want to include are specified as a bitmask that can be a combination of the following constants: 

Debug Input Filter Constant

| Constant | Description |
| --- | --- |
| debug\_input\_filter\_keyboard | Include keyboard input |
| debug\_input\_filter\_mouse | Include mouse input |
| debug\_input\_filter\_touch | Include touch input |

If you want to record, for example, keyboard and mouse input the value would be debug\_input\_filter\_keyboard\|debug\_input\_filter\_mouse.

 
 

#### Syntax:

debug\_input\_record(filter)

| Argument | Type | Description |
| --- | --- | --- |
| filter | [Debug Input Filter Constant](debug_input_record.md) | A bitmask combining the different types of input to record |

 

#### Returns:

N/A

 

#### Example:

debug\_input\_record(debug\_input\_filter\_keyboard\|debug\_input\_filter\_mouse);

The above code starts recording both keyboard and mouse input, which can be saved to a file using [debug\_input\_save](debug_input_save.md).
