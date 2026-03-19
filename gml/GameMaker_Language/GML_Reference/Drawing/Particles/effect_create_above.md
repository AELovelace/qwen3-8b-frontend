# effect\_create\_above

This function creates a simple effect above all instances of your room (it is actually created at a depth of \-15000\).

 
The effect types ef\_rain and ef\_snow don't use the x/y position (although you must provide them). The size can be a value of 0, 1, or 2, where 0 is small, 1 is medium and 2 is large.

 

The available constants for the different particle kinds are: 

| [Effect Type Constant](GameMaker_Language/GML_Reference/Drawing/Particles/effect_create_above.md) | | |
| --- | --- | --- |
| Constant | Example | Description |
| ef\_cloud |  | An effect that creates random cloud particles of varying sizes |
| ef\_ellipse |  | An effect that creates expanding ellipses |
| ef\_explosion |  | An effect that creates expanding fading explosions |
| ef\_firework |  | An effect that creates multiple small particles to generate a firework explosion |
| ef\_flare |  | An effect that generates a brilliant point that flares up and fades out |
| ef\_rain |  | An effect that generates rain particles coming down from the top of the screen |
| ef\_ring |  | An effect that generates expanding and fading circles |
| ef\_smoke |  | An effect that generates little puffs of smoke |
| ef\_smokeup |  | An effect that creates a smoke plume that rises up the screen |
| ef\_snow |  | An effect that generates multiple snow particles falling down the screen |
| ef\_spark |  | An effect that generates a small spark |
| ef\_star |  | An effect that generates star particles |

 

#### Syntax:

effect\_create\_above(kind, x, y, size, colour)

| Argument | Type | Description |
| --- | --- | --- |
| kind | [Effect Type Constant](GameMaker_Language/GML_Reference/Drawing/Particles/effect_create_above.md) | The kind of effect (use one of the constants listed above). |
| x | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x positioning of the effect if relevant. |
| y | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y positioning of the effect if relevant. |
| size | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The size of the effect. |
| colour | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the effect. |

 

#### Returns:

N/A

 

#### Example:

if (health \<\= 0\)   

 {  

     effect\_create\_above(ef\_explosion, x, y, 1, c\_yellow);  

     instance\_destroy();  

 }

The above code will create a medium, yellow, explosion above the instance and destroy it if its health variable is less than or equal to 0\.
