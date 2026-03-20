# rollback\_use\_random\_input

When you play a game using [Sync Test](../Rollback_System.md#h), all "remote" players receive random values for their [defined inputs](../Defining_Inputs.md), as a basic way of testing. You can disable this behaviour by calling this function with false as its argument, and enable it again by specifying true.

 

#### Syntax:

rollback\_use\_random\_input(enabled)

| Argument | Type | Description |
| --- | --- | --- |
| enabled | [Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | Specifies whether random input should be enabled (true) or disabled (false). By default, it's enabled. |

 

#### Returns:

N/A

 

#### Example:

rollback\_use\_random\_input(false);

The above code disables random input during Sync Test.
