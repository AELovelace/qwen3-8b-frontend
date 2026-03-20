# random\_set\_seed

This function sets the seed used by GameMaker to generate random numbers.

To generate a random number GameMaker starts with a random seed number. With this function you can set that seed to a known value and so "force" the outcome of all random events afterwards to be the same every time the program is run. For example, this function can be used in conjunction with [random\_get\_seed](random_get_seed.md) to create procedurally generated content and save the results without having huge savegames (you save the seed only, no need for anything else). Should you need truly random results for everything, you should be using the [randomise](randomise.md) function.

You can specify any value into the optional second argument fix\_range\_bug, which uses an alternate function to set the seed that should ensure a higher range of the random state. This should be more accurate in setting the state as the previous behaviour was erroneous and is only kept for legacy purposes.

  While this seed will give consistent results on each target platform, results may vary between platforms due to the different way each target works.

 

#### Syntax:

random\_set\_seed(val, \[fix\_range\_bug])

| Argument | Type | Description |
| --- | --- | --- |
| val | [Real](../../../GML_Overview/Data_Types.md) | The seed to set |
| fix\_range\_bug | [Boolean](../../../GML_Overview/Data_Types.md) | Specify any value to use alternate function to remove range limits |

 

#### Returns:

N/A

 

#### Example:

if (debug)  

 {  

     random\_set\_seed(1, true);  

 }

The above code sets the random seed to 1 only if the variable debug is true, using the newer method to set the seed (by supplying a second argument).
