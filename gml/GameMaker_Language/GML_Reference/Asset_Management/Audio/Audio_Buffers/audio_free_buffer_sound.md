# audio\_free\_buffer\_sound

With this function you can free up the pointer index value associated with the sound ID. Freed sounds will not be available for playing, and if multiple instances of the sound are being played they will all be stopped. Note that before you can delete
 the buffer itself, you must first free all sound ID's associated with it.

 

#### Syntax:

audio\_free\_buffer\_sound(index)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The index of the buffered sound to free. |

 

#### Returns:

 

#### Example:

audio\_free\_buffer\_sound(soundID);

The above code frees the buffered sound indexed in the variable "soundID".
