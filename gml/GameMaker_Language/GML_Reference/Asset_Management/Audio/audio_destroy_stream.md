# audio\_destroy\_stream

This function destroys a previously created audio stream from memory. Any further calls to the sound after it has been destroyed will give an error.

  This will free up the stream but on the target platform this may not show up in a memory manager. This is because GameMaker pools memory resources to prevent memory allocation overhead, and so the memory will remain allocated until required for something else or re\-used for a new stream.

 

#### Syntax:

audio\_destroy\_stream(sound)

| Argument | Type | Description |
| --- | --- | --- |
| sound | [Sound Asset](../../../../The_Asset_Editors/Sounds.md) | The sound asset, as returned by [audio\_create\_stream](audio_create_stream.md) |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md) (1 if the stream was successfully destroyed, \-1 if it wasn't)

 

#### Example:

audio\_destroy\_stream(snd);

The above code removes the sound stored in the variable snd from memory.
