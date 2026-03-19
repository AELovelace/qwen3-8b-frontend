# Basic Code Structure

Code is written in *blocks* and a typical code block consists of a set of instructions, called [statement](#)s, that are then interpreted by GameMaker and used to make something happen within your game. That "something" can be as simple as adding 2 and 2 to get 4, or as complex as making an enemy run away when their health gets below a certain value. The actual structure of the program can vary greatly, depending on the functions it uses, but broken down to basics it just looks like this:

\;  

 \;  

 ...

Statements should be separated with a ; symbol to prevent errors with [variable](#) declarations and to keep your code clean and tidy, and they can consist of variable declarations, [expression](#)s and calls to specific **functions**. You can also "group" statements together as a block using the curly brackets { } so that they run together, like in the following [conditional](#) example:

if (\)  

 {  

     \;  

     \;  

     ...  

 }

NOTE The GameMaker Language will also accept begin and end instead of the curly brackets { }, although this is not typically the most common way to do it:

if (\)  

 begin  

     \;  

     \;  

     ...  

 end

Here is a more visual representation of how a code block can look, this time created as a **script** in the GameMaker [Script Editor](../../The_Asset_Editors/Scripts.md):

There are a number of different types of statements, expressions, conditionals and functions, all of which are discussed at length in subsequent sections of the manual.

  If you are new to programming then you may want to check out the [Quick Start Guide](../../Quick_Start_Guide/Quick_Start_Guide.md) before continuing.
