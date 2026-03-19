# audio\_get\_type

This function returns the type of the given sound asset, which can be either *streamed* (1\) or *in memory* (0\).

If you need to know whether a given sound is for streamed audio or not you can use this function, which will throw a fatal error if the index does not point to a valid sound.

 

#### Syntax:

audio\_get\_type(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../The_Asset_Editors/Sounds.md) | The index of the sound to check |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md) (1: streamed, 0: in memory, \-1: any error)

 

#### Example:

type \= audio\_get\_type(snd\_Music\_1\);

The above code checks the type of audio indexed in the variable "snd\_Music\_1" and stores the returned value in the variable "type".
