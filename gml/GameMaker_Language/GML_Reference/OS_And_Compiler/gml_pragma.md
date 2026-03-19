# gml\_pragma

The gml\_pragma function affects how the given target compiles your code and should be called with the different commands to further optimise the final compilation of your project. These commands are effectively *pre\-processed* before the game is compiled and so the function can be placed anywhere in your project and it will still be processed before the game is fully compiled. The available commands are as follows:

- "**forceinline**" \- When a **function or method** contains a "forceinline" pragma, the YYC requests the C\+\+ compiler to compile the project with the function [inlined](https://en.wikipedia.org/wiki/Inline_expansion "Inline expansion"), rather than referenced. This request isn't guaranteed and what happens depends on the C\+\+ compiler.  

 Inlining functions will give a further processing boost, but care must be taken when using it as it will also inflate the final executable file size (especially if the inlined code is large and/or used in multiple different places) as well as greatly increase the compile time. Note that this pragma is **only valid when building using the YYC**.
- "**global**", "**\[gml code]**" \- The "global" pragma permits you to call some GML code formatted as a string, at a **global** scope, at compile time, before the first room of the game executes. For example:
 gml\_pragma("global", "Init()");

 This will call the script function "Init" before the first room of the game is run. Note that the GML supplied as the second argument **must be a compile\-time constant**, and also note that you cannot use this pragma to create instances or perform any operations that require a room (or anything in a room) to function.
- **"optimise"/"optimize", "\", "\"** \- The "optimise" (or "optimize") pragma provides an optimisation hint to the compiler. For example: 
 gml\_pragma("optimise", "js\_array\_check", "push, off");

 This pragma will make the compiler omit type checking code on arrays when it generates JavaScript code.  

  

 See the section on **Compiler Optimisations** below for a full list of optimisations you can use.
- "**PNGCrush**" \- The "PNGCrush" pragma will use the [PNGCrush](https://pmt.sourceforge.io/pngcrush/) program on each texture created. Note that this can add significantly to the time that it takes to compile the game, so you don't want it on all the time, although it can make significant savings on final file size. This option only applies to Texture Groups that use the PNG format (see [Texture Group Format](../../../Settings/Texture_Groups.md#texture_group_format)).
- "**Texgroup.Scale**", "**\[TextureGroupName]**", "**\[Scale Divisor]**" \- The "Texgroup.Scale" will scale the given texture group on compile. You need to give an additional two arguments here: the "\[TexGroupName]", which is the name (a string) of the texture group to scale, and the "\[Scale Divisor]" (also a string), which is the divisor you wish to use for the scaling, i.e.:
 gml\_pragma("Texgroup.Scale", "level1", "2");

 This will halve all the textures in the "level1" texture group.
- "**UnityBuild**", "**\[enable/disable]**" \- If you call the function with this pragma and set the enable/disable argument to true then on compile it will collapse all the .cpp files in the project into a single file which it then uses to build everything, for example:
 gml\_pragma("UnityBuild", "true");

 The benefit of doing a unity build is that builds are faster but the down side is that it does a *full* build each time so even if you change a single part of the code it will build everything again without using any cached files. This has been added specifically for the Xbox One export using the YYC although it can be called for other builds (**YYC only**). For more information on unity builds, please see [here](https://buffered.io/posts/the-magic-of-unity-builds/).
- "**AllowReentrantStatic**" \- This pragma reverts static initialisation to the old re\-entrant initialisation behaviour of GameMaker versions up to 2024\.8\. It is a project\-wide setting and so cannot be put around code sections. The following code enables this old behaviour: 
 gml\_pragma("AllowReentrantStatic", true);

  You should only use this in existing projects that make use of the old behaviour. [GMRT (GameMaker Runtime)](../../../Settings/Runner_Details/GMRT_(GameMaker_Runtime).md) will no longer allow it.
- "**MarkTagAsUsed**" \- When "**Automatically remove unused assets when compiling**" is enabled in the [Game Options](../../../Settings/Game_Options.md), any unused assets are stripped from the compiled game. This can break games that dynamically load assets at runtime. With this pragma you can mark the [Tags](../../../Introduction/The_Asset_Browser.md#h "tags") that should not be stripped and any assets with the assigned tags will always be present in the compiled game package.
 gml\_pragma("MarkTagAsUsed", "used");  

 gml\_pragma("MarkTagAsUsed", "multiple", "tags", "can", "be", "specified");
- **"LegacySetObjectOrder"** \- This pragma ensures that the given object references are listed in the specified relative order on export, without moving other objects in the list. It can be used more than once in your project and the results will depend on which pragmas are processed first, so if you have a paradox in the commands then the output will be ill\-defined and depend on the asset compiler's order of processing. An error is thrown when an object is mentioned more than once in the list or when an object name is not in the project. Note that this pragma has been added for pragmatic reasons and *using it is strongly discouraged*. It is unlikely to be supported in future versions of GameMaker.
 gml\_pragma("LegacySetObjectOrder", Object2, Object3, Object1\);

 Using the code above, Object2 will be listed first, followed by Object3 and Object1.
- **"MarkUILayerAsUsed"** \- This pragma marks the UI layer with the given name as used to the asset compiler. This makes sure a UI layer present in a prefab is added to the main project upon export.  

 Note that the object which calls this pragma should itself not be on any UI layer which you mark as used, as this will result in a situation where dragging the prefab into an Instances layer in your room will then give you two instances of the object when the game is run \- the one you dragged onto the Instances layer and the original one on your marked UI layer.
gml\_pragma("MarkUILayerAsUsed", "UI Layer Name");

  The first argument to the gml\_pragma function **must be a compile\-time string constant** and not a variable.

[Compiler Optimisations](#)

Compiler optimisations can be provided with the "optimise" (or "optimize") pragma. Their basic syntax is: 

gml\_pragma("optimise", "\", "\");

"\" is a string containing the specific optimisation to modify.

"\" is a string that contains a comma\-delimited list of commands that control the optimisation from this point in your code: 

- push \- pushes onto an internal stack (for that optimisation) the current state of that optimisation
- pop \- pops from the internal stack (for that optimisation) into the current state
- on or true \- switches on the optimisation
- off or false \- switches off the optimisation

The following table lists all optimisations that you can use: 

Compiler Optimisations

| Optimisation | Description |
| --- | --- |
| js\_array\_check | If ON then the compiled code will include checks that variables are arrays and do basic error checking on the array, omitted if OFF. These checks are done at each use of the array.   If OFF then you need to make sure that every variable used as an array is definitely of type array before using it. |
| js\_error\_check | If ON then the compiled code will include checks in the generated JavaScript code to bring it in line with how the VM/YYC runner handles errors. These checks will be omitted if OFF.   This can be safely omitted if your code is not erroring when used, generally something that can be disabled once your code is working error free. |
| js\_check\_index | If ON then the generated code will include checks on the index on array access (read and write) to catch out of range errors. If OFF you need to make sure to always use an array index that's within the array's length (i.e. from 0 to [array\_length](../Variable_Functions/array_length.md)\-1\). |
| js\_pre\_post\_no\_long | If ON then increment \+\+ and decrement \-\- expressions are not checked to see if they operate on values of type int64 (or Long in JavaScript). You need to make sure that no variables are of type [int64](../Variable_Functions/is_int64.md) when using the \+\+ and \-\- operators. |
| js\_use\_infix\_ops | If ON then JavaScript's binary operators \+, \-, \*, etc. are used in preference to using GameMaker's type checking functions. In this case you need to make sure that all variables used in the expression are of type [real](../Variable_Functions/is_real.md). |

### Example

As an example, to optimise the following function: 

function multiples\_of\_two()  

 {  

     var a \= \[];  

     for (var i \= 0; i \< 100; i\+\+)  

     {  

         a\[i] \= i \* 2;  

     }  

 }

You would then add gml\_pragma statements as follows: 

function multiples\_of\_two()  

 {  

     gml\_pragma( "optimise", "js\_array\_check", "push, off");  

     gml\_pragma( "optimise", "js\_error\_check", "push, off");  

     gml\_pragma( "optimise", "js\_check\_index", "push, off");  

     gml\_pragma( "optimise", "js\_pre\_post\_no\_long", "push, on");  

     gml\_pragma( "optimise", "js\_use\_infix\_ops", "push, on");  

     var a \= \[];  

     for(var i \= 0; i \< 100; i\+\+)  

     {  

         a\[i] \= i \* 2;  

     }  

     gml\_pragma( "optimise", "js\_use\_infix\_ops", "pop" );  

     gml\_pragma( "optimise", "js\_pre\_post\_no\_long", "pop" );  

     gml\_pragma( "optimise", "js\_check\_index", "pop" );  

     gml\_pragma( "optimise", "js\_error\_check", "pop" );  

     gml\_pragma( "optimise", "js\_array\_check", "pop" );  

 }

### Usage Notes

- Compiler optimisations are treated as *hints* to the compiler, it is free to ignore those hints. Also, certain optimisations may only target specific compilers, for example the JavaScript transpiler (these optimisations begin with "js\_").
- All the parameters to the "optimise" command must be known at compile\-time and therefore **must** be constant strings, an error is generated otherwise.
- If the compiler doesn't understand a "specific\_optimisation" string, it will silently ignore it.

 

 

#### Syntax:

gml\_pragma(command, \[optional...])

| Argument | Type | Description |
| --- | --- | --- |
| command | [String](../../GML_Overview/Data_Types.md) | A string with one of the commands listed above. |
| \[optional] | [String](../../GML_Overview/Data_Types.md) | Some of the available commands require an optional argument or arguments. These are explained above for each command. |

 

#### Returns:

N/A

 

#### Example:

gml\_pragma("forceinline");

The above example code will force the script function where it is used to be inlined on compile.
