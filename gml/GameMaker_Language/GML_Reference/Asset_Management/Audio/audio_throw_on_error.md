# audio\_throw\_on\_error

This function enables or disables audio functions throwing fatal errors (as described in [Audio Error Handling](Audio.md#h1)). By default, throwing is enabled and you can pass false to this function to disable that behaviour and instead make such errors print a message to the Output Log.

 
 

#### Syntax:

audio\_throw\_on\_error(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether errors should be thrown (true, default) or logged (false) |

 

#### Returns:

N/A

 

#### Example:

audio\_throw\_on\_error(false);

This disables audio functions throwing errors.
