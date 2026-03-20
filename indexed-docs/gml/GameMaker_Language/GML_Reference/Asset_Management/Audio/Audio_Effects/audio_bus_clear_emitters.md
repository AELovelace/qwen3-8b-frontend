# audio\_bus\_clear\_emitters

This function clears the list of all audio emitters on the given bus and relinks them to the main bus.

  A bus that has no emitters linked to it is not processed.

 

#### Syntax:

audio\_bus\_clear\_emitters(bus)

| Argument | Type | Description |
| --- | --- | --- |
| bus | [AudioBus Struct](AudioBus.md) | The bus of which to clear the emitters |

 

#### Returns:

N/A

 

#### Example:

audio\_bus\_clear\_emitters(bus1\);

The above code clears all emitters linked to an existing audio bus bus1, reassigning them to the main audio bus [audio\_bus\_main](audio_bus_main.md).
