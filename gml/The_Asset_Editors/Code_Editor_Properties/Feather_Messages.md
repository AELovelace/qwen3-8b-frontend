# Feather Messages

This page contains descriptions of all Feather rules that are shown under [Message Severity](../../Setting_Up_And_Version_Information/IDE_Preferences/Feather_Settings.md#s3) in the [Feather Preferences](../../Setting_Up_And_Version_Information/IDE_Preferences/Feather_Settings.md).

Hit CTRL/CMD \+ F on this page to find the rule you want to read about.

## Rules

### GM1000 \- No enclosing loop from which to break.

The keyword [break](../../GameMaker_Language/GML_Overview/Language_Features/break.md) must be used inside the body of a loop statement such as [while](../../GameMaker_Language/GML_Overview/Language_Features/while.md), [for](../../GameMaker_Language/GML_Overview/Language_Features/for.md), [repeat](../../GameMaker_Language/GML_Overview/Language_Features/repeat.md), or [with](../../GameMaker_Language/GML_Overview/Language_Features/with.md).

Usage outside of a loop statement is not possible and results in a Compile Error.

#### Example

var \_items \= get\_items();  

 var i \= 0;  

 repeat (array\_length(\_items))  

 {  

     var \_item \= \_items\[i\+\+];  

     if (\_item \=\= undefined)  

         break; // Good!  

     // ... Some logic here ...  

 }  

 break; // GM1000 \- No loop to break from.

Correcting this error requires identifying where the break statement was intended to go and moving it to the correct location. In the above example there was no loop to break from and thus the fix is to simply remove the last break statement.

### GM1001 \- No enclosing loop from which to continue.

The keyword [continue](../../GameMaker_Language/GML_Overview/Language_Features/continue.md) must be used inside the body of a loop statement such as [while](../../GameMaker_Language/GML_Overview/Language_Features/while.md), [for](../../GameMaker_Language/GML_Overview/Language_Features/for.md), [repeat](../../GameMaker_Language/GML_Overview/Language_Features/repeat.md), or [with](../../GameMaker_Language/GML_Overview/Language_Features/with.md).

Usage outside of a loop statement is not possible and results in a Compile Error.

var \_items \= get\_items();  

 var i \= 0;  

 repeat (array\_length(\_items))  

 {  

     var \_item \= \_items\[i\+\+];  

     if (\_item \=\= undefined)  

         continue; // Good!  

     // ... Some logic here ...  

 }  

 continue; // GM1001 \- No loop to continue from.

Correcting this error requires identifying where the continue statement was intended to go and moving it to the correct location. In the above example there was no loop to continue from and thus the fix is to simply remove the last continue statement.

### GM1002 \- globalvar does not support inline initializers.

When using globalvar's you must split the declaration and initialization of its value. This is in contrast to local variables which can be declared and initialized in the same statement (e.g. var \_width \= 100;).

Attempting to initialize a globalvar inline in this manner is invalid syntax and results in a Compile Error.

#### Example

globalvar gameManager \= new GameManager(); // GM1002 \- globalvar does not support inline initializers.

Correcting this error requires splitting the declaration and initialization statements. The above example can be fixed by rewriting it as so:

globalvar gameManager;  

 gameManager \= new GameManager();

### GM1003 \- Enum assignment must be integer assignment.

When declaring the members of an [enum](../../GameMaker_Language/GML_Overview/Variables/Constants.md#enumhead) you can assign specific integer values to the members. You cannot assign any other type of value to these members however. Attempting to do so will result in a Compile Error.

#### Example

enum FRUIT  

 {  

     UNKNOWN \= \-1, // Good!  

     BANANA,  

     ORANGE,  

     APPLE \= "apple" // GM1003 \- Enum assignment must be integer assignment.  

 }

Correcting this error requires changing the assigned value to an integer in some way. If your code requires a value type other than [Real](../../GameMaker_Language/GML_Overview/Data_Types.md) for some reason then you may want to investigate using macros instead.

// Approach 1  

 enum FRUIT  

 {  

     UNKNOWN \= \-1, // Good!  

     BANANA,  

     ORANGE,  

     APPLE \= 10 // Good!  

 }  

  

 // Approach 2  

 \#macro FRUIT\_UNKNOWN     \-1  

 \#macro FRUIT\_BANANA     0  

 \#macro FRUIT\_ORANGE     1  

 \#macro FRUIT\_APPLE     "apple"
 

### GM1004 \- The enum value 'ENUM MEMBER NAME' has already been previously defined in the enum 'ENUM NAME'.

[Enum](../../GameMaker_Language/GML_Overview/Variables/Constants.md#enumhead) members must be uniquely named, duplicate names will result in a Compile Error.

#### Example

enum FRUIT  

 {  

     APPLE, // Good!  

     APPLE, // GM1004 The enum value 'APPLE' has already been previously defined in the enum 'FRUIT'  

 }

Typically, this error is the result of a typo of oversight. Removing the duplicate declaration will fix the issue.

enum FRUIT  

 {  

     APPLE, // Good!  

 }

### GM1005 \- Argument must be provided.

A function's parameter is required, yet an argument was not passed. While some parameters are optional (denoted with \[square brackets]), most are required. When no argument is passed to these parameters, a compile error occurs.

#### Example

draw\_set\_color(); // GM1005 \- Argument must be provided.

Typically, this error is the result of an oversight. Providing the missing argument will fix the issue.

draw\_set\_color(c\_black); // Good!

### GM1006 \- The enum 'ENUM NAME' has already been previously declared.

[Enums](../../GameMaker_Language/GML_Overview/Variables/Constants.md#enumhead) must be uniquely named, duplicate names will result in a compile error.

#### Example

enum FRUIT {  

     APPLE,  

     ORANGE,  

     BLUEBERRY  

 }  

 enum FRUIT // GM1006 \- The enum 'FRUIT' has already been previously declared.  

 {  

     APPLE,  

     ORANGE,  

     CHERRY  

 }

Typically, this error is the result of an oversight. Removing the duplicate declaration, merging members of applicable will fix the issue. If the enums are intended to be different but names conflict, consider a different name for the new enum.

enum FRUIT  

 {  

     APPLE,  

     ORANGE,  

     BLUEBERRY,  

     CHERRY  

 }

### GM1007 \- Left\-hand side of an assignment must be a variable.

The assignment operator \= requires that the left\-hand side of the statement be a variable. Constants, and other non\-variables cannot be logically assigned to. E.g. 1 \= 2 is not a mathematically valid statement.

A variable assignment stores the value on the right\-hand side of the \= sign somewhere in the computer's memory and makes it accessible in code through the name that you write on the left. If the variable already exists, the assignment will replace its contents with the new value on the right\-hand side. Instances, structs, functions, constants and asset IDs are all non\-variables and cannot be assigned to. You can, however, assign a value to one of the variables of an instance, struct or function.

For more info on variable assignment see [Variables And Variable Scope](../../GameMaker_Language/GML_Overview/Variables_And_Variable_Scope.md).

#### Example

var \_foo \= 1234;  

 \_foo \= 4321; // Good!  

  

 function get\_random\_item()  

 {  

     return  

     {  

         name: "Sword"  

     };  

 }  

  

 get\_random\_item() \= "Shield"; // GM1007 \- Left\-hand side of an assignment must be a variable
 

Typically, this error is the result of a typo or oversight. Sometimes it's the result of a misunderstanding of how data flows through a program. If this is the case, take a step back and think about what you're trying to communicate to the CPU.

var \_foo \= 1234;  

 \_foo \= 4321; // Good!  

  

 function get\_random\_item()  

 {  

     return  

     {  

         name: "Sword"  

     };  

 }  

  

 get\_random\_item() \= { name: "Shield" }; // Bad! Return values are not variables  

 get\_random\_item().name \= "Shield"; // Good!  

 vk\_space \= vk\_tab; // Bad! Constants are not variables and cannot change
 

### GM1008 \- The variable 'BUILT\-IN VARIABLE' is readonly and cannot be assigned to.

Attempting to assign a value to a read\-only built\-in variable is not allowed. These variables can be read and assigned to other variables or used in expressions, but cannot have their value directly modified.

#### Example

working\_directory \= @"PlayerData"; // Bad! working\_directory is readonly  

 var \_file \= file\_find\_first(working\_directory \+ @"\\Screenshots\\\*.png", fa\_archive);  

 // ...

Since read\-only variables cannot be directly assigned to the fix will depend on what your intention with setting the variable is. In the above example, we intend to find all the files in a directory "PlayerData\\Screenshots\\" relative to our working\_directory. For this we can just use a local variable instead.

var \_playerdata\_directory \= working\_directory \+ @"PlayerData";  

 var \_file \= file\_find\_first(\_playerdata\_directory \+ @"\\Screenshots\\\*.png", fa\_archive);  

 // ...

### GM1009 \- Operation OPERATOR between types 'TYPE' and 'TYPE' may result in unexpected behavior or an error during runtime.

This indicates that the specified operation, while valid, may not have the result or behaviour that is expected. You may see this when adding reals to constant or asset types; which is an abuse of these types. Constant values are intended to be used in very specific ways, and asset IDs are not safely modifiable.

 
#### Example

// Find all \*.doc files that are readonly archives  

 var \_attribs \= fa\_readonly \+ fa\_archive; // Warn!  

 var \_filename \= file\_find\_first("/User Content/\*.doc", \_attribs);  

  

 // Go to the next room  

 room\_goto(room \+ 1\); // Warn!
 

In the above example we have 2 problems: Adding constants that are meant to be flags, and adding 1 to the current room ID to find the next room. The tricky bit is that this code might just work! But it's brittle and unrelated changes to the Runner or even your Game Project might break this code! Why?

**Bitfield Constants**

When it comes to constants used as bit field flags you should use the Bitwise OR operation \| instead of the Arithmetic Add operation \+. If we were to consider fa\_readonly as 0b0001 and fa\_archive as 0b0010 and we added (0b0001 \+ 0b0010 \= 0b0011) these two together we would get the same result as if we or'd the values (0b0001 \| 0b0010 \= 0b0011). However, if for some reason the value of fa\_readonly changed to be 0b0011 with two set bits instead of one (perhaps it's a mask field, or represents two other values together) then we will suddenly end up with an incorrect value and our code will stop working. (0b0011 \+ 0b0001 \= 0b0100, and 0b0011 \| 0b0001 \= 0b0011).

**Mutating Asset IDs**

Assets such as Rooms, Sprites and Objects are assigned an ordinal index number when your game is compiled. Which means that each asset is given a unique number that increments by 1 from 0\. This may lead you to believe that if you wanted to get the next or previous room, for example, you can simply add or subtract 1 from the current room. However, the order that the rooms are in is different from the asset ID, perhaps you created the rooms out of order and then rearranged them, perhaps the method by which the compiler determines the asset IDs changes. In either of these instances your code would break. Instead you should use functions provided by the Runner for these specific tasks.

// Find all \*.doc files that are readonly archives  

 var \_attribs \= fa\_readonly \| fa\_archive; // Good!  

 var \_filename \= file\_find\_first("/User Content/\*.doc", \_attribs);  

  

 // Go to the next room  

 room\_goto\_next(); // Good!
 

### GM1010 \- Cannot perform OPERATOR operation between types 'TYPE' and 'TYPE'.

This indicates that the specified operation is invalid in such a way that no result can be produced and instead result in either a runtime or compile time error. You may see this error between some type and undefined or unset. If Feather is unable to determine the type of a variable (or the variable is genuinely unset) then this error will appear.

 
#### Example

var \_item1 \= { price: 10 };  

 var \_item2 \= { price: 20 };  

 var \_diff \= \_item2 \- \_item1; // Error!  

 var \_a, \_b \= 1234;  

 var \_c \= \_a \+ \_b; // Error!

This will require rewriting your code such that the intention is conveyed in valid operations. In the above example we intended to get the difference in price between 2 items. We can instead subtract the price variables, which are of type [Real](../../GameMaker_Language/GML_Overview/Data_Types.md), instead of the structs themselves.

var \_item1 \= { price: 10 };  

 var \_item2 \= { price: 20 };  

 var \_diff \= \_item2\.price \- \_item1\.price; // Good!  

 var \_a \= 4321, \_b \= 1234;  

 var \_c \= \_a \+ \_b; // Good!

### GM1011 \- Implicit cast of type 'TYPE' to 'Bool' may result in unexpected behavior or an error during runtime.

A common shorthand for if statement conditionals is to exclude the \=\= false or \=\= true from a boolean logic comparison. In GML doing so implicitly casts the conditional to a Boolean and compares it to true. Some types cannot be converted to Boolean and will result in a runtime error. The type Unset is special and indicates that you've declared a variable but never assigned a value to it, no operation is valid on Unset.

 
See: [if / else and Conditional Operators](../../GameMaker_Language/GML_Overview/Language_Features/If_Else_and_Conditional_Operators.md)

#### Example

var \_a \= true;  

 var \_b \= 1234;  

 var \_c \= \[];  

 var \_d;  

 if (\_a) { } // Good!  

 if (\_b) { } // Good!  

 if (\_c) { } // Error!  

 if (\_d) { } // Error!

The solution is typically to be explicit about your comparisons.

- String, Array, Function, Struct, Id, Asset, Constant – !\= undefined
- Bool – \=\= true, or implicit cast still valid
- Real – \> 0, or implicit cast still valid (though discouraged)
- Unset – Assign a value to it!

var \_a \= true;  

 var \_b \= 1234;  

 var \_c \= \[];  

 var \_d;  

 if (\_a \=\= true) { } // Good!  

 if (\_a) { } // Good!  

 if (\_b \> 0\) { } // Good!  

 if (\_b) { } // Good!  

 if (\_c !\= undefined) { } // Good!  

 \_d \= true; // Assign a value to change from Unset  

 if (\_d) { } // Good!

### GM1012 \- Malformed variable addressing expression.

The dot operator is used to access a variable that exists in another scope. These dot operators can be chained together or exist alone, in either occurrence this is known in GML as a "variable addressing expression", as it is an expression that gives a variable's address. Usually the left\-hand side of this expression is a variable or constant containing an Object Asset, Instance ID, or Struct. Other types cannot be on the left\-hand side because they do not contain variables.

#### Example

var \_a \= { name: "GameMaker" };  

 var \_b \= \_a.name; // Good!  

 var \_c \= obj\_manager.name; // Good!  

 var \_d \= "name".length; // Error!

Correcting this error depends on what is on the left\-hand side of the expression. You likely intended to reference a variable from an Object Asset, Instance, or Struct but either typo'd the name or your variable contains a different type than was expected.

var \_d \= string\_length("name"); // Good!

### GM1013 \- Reference to variable 'IDENTIFIER' which has not been previously declared in 'IDENTIFIER'.

This error indicates that the specified variable cannot be found in the referenced scope.

 
This could indicate that:

// Create event  

 var atk \= 1;  

 if (atk \< 50\) {    // Error! 'atk' is a local variable in Create  

     with (other) {  

         hp \-\= atk; // Error! 'atk' is in the original scope!  

     }  

       

     attack \*\= 2;   // Error! Typo'd 'atk' as 'attack'  

 }  

  

 // Script \- Item  

 function Item(\_name, \_value) constructor {  

     name \= \_name;  

     value \= \_value;  

 }  

  

 // Create \- objInventory  

 hp \= 100;  

 items \= \[];  

 var \_sword \= new Item("Sword", 10\);  

 array\_push(items, \_sword);  

 var \_shield \= new Item("Shield", 10\);  

 \_shield.defense \= 10;  

 array\_push(items, \_shield);  

  

 // Collision \- par\_mob  

 var \_dmg \= other.dmg;  

 var \_len \= array\_length(items);  

 for (var i \= 0; i \< \_len; \+\+i) {  

     var \_item \= items\[i];  

     \_dmg \-\= \_item.defense; // Error! 'defense' is conditionally defined  

 }  

  

 hp \-\= max(0, \_dmg);
 

Correcting this issue depends on which of the aforementioned conditions applies to your situation.

// Create event  

 atk \= 1; // Fix! Make this an instance variable by removing 'var'  

 // Collision \- par\_mob  

 if (atk \< 50\) { // Good!  

     with (other) {  

         hp \-\= other.atk; // Fix! Reference 'other.atk'  

     }  

       

     atk \*\= 2; // Fix! Rename to 'atk'  

 }  

  

 // Script \- Item  

 function Item(\_name, \_value) constructor {  

     name \= \_name;  

     value \= \_value;  

     defense \= 0; // Possible Fix! Declare a default value  

 }  

  

 // Create \- objInventory  

 hp \= 100;  

 items \= \[];  

 var \_sword \= new Item("Sword", 10\);  

 array\_push(items, \_sword);  

 var \_shield \= new Item("Shield", 10\);  

 \_shield.defense \= 10;  

 array\_push(items, \_shield);  

  

 // Collision \- par\_mob  

 var \_dmg \= other.dmg;  

 var \_len \= array\_length(items);  

 for (var i \= 0; i \< \_len; \+\+i) {  

     var \_item \= items\[i];  

     \_dmg \-\= \_item.defense; // Fix! 'defense' has default value  

     // Or Possible Fix! Check variable exists (not as recommended)  

     if (struct\_exists(\_item, "defense")) {  

         \_dmg \-\= \_item.defense; // Feather knows this variable exists now  

     }  

 }  

  

 hp \-\= max(0, \_dmg);
 

### GM1014 \- The enum 'ENUM' does not contain the value 'IDENTIFIER'.

This error is raised when an Enum Member is referenced which does not exist.

This could indicate that:

#### Example

enum FRUIT {  

     NONE,  

     ORANGE,  

     APPLE,  

     CANTALOUPE,  

     SIZEOF  

 }  

 var \_best\_fruit \= FRUIT.KIWI; // Error! KIWI is not defined  

 var \_underrated\_fruit \= FRUIT.CANALOPE; // Error! CANTALOUPE is typo'd

Correcting this issue depends on which of the aforementioned conditions applies to your situation.

enum FRUIT {  

     NONE,  

     ORANGE,  

     APPLE,  

     CANTALOUPE,  

     KIWI, // Fix! Define KIWI  

     SIZEOF  

 }  

 var \_best\_fruit \= FRUIT.KIWI; // Good!  

 var \_underrated\_fruit \= FRUIT.CANTALOUPE; // Fix! No longer typo'd

### GM1015 \- Cannot divide or modulo expression by 0\.

This error is raised when you directly divide or modulo by 0\.

Note: GM1015 is NOT raised if 0 is stored in a variable and then you divide by that variable; Feather does not track the individual values of variables, only the types of variables.

#### Example

var \_hp \= 100;  

 \_hp /\= 0; // Error! Cannot divide by 0  

 \_hp %\= 0; // Error! Cannot modulo by 0

The solution is to use any number other than 0\.

var \_hp \= 100;  

 \_hp /\= 100; // Good!  

 \_hp %\= 100; // Good!

### GM1016 \- A boolean literal was unexpected at this time.

This message indicates that a boolean value (true or false) has appeared outside of a conditional or expression. Typically you would only see these kinds of values used in if statements and friends.

#### Example

true; // Error! A lone true without a conditional

Use boolean values in a way that the compiler understands. For example:

var \_a \= true; // Good! Right\-hand side is an expression  

 var \_b \= true ? 1 : 0; // Good! Right\-hand side is an expression  

 if (true) {  

     // Good! Appears inside a conditional  

 }

### GM1017 \- The function 'FUNCTION NAME' is deprecated and usage is discouraged.

This message indicates that you are using either a built\-in function or user\-defined function that is deprecated. Deprecation means that while the function, variable, or feature is still available for usage that it is planned to be removed in the future. Typically when something is deprecated a superior approach exists and is intended to be used instead. You should research what the alternative is and use that instead to avoid your code from breaking when you update GameMaker to newer versions.

Note that user\-defined functions can also be marked as deprecated using the @deprecated tag.

#### Example

// @deprecated  

 function make\_game() {  

     // Deprecated in favour of writing more code to do that same thing!  

 }  

  

 username \= get\_string("Username:", ""); // Suggestion!  

 make\_game(); // Suggestion!
 

Find the alternative functions or approach to use, and refactor your code to do that instead.

username \= get\_string\_async("Username:", ""); // Fix!

### GM1019 \- The function 'FUNCTION NAME' takes no more than NUMBER arguments but NUMBER are provided.

This message is shown when more arguments are passed to a function than that function takes, including optional parameters (if they exist).

There are essentially two reasons you might run into this problem:

- You're nesting function calls and missed a closing parenthesis )
- You have miscounted your arguments

The solution to fixing either of these is to refactor your code to reflect your actual intentions.

#### Example

var \_dmg \= clamp(lerp(dmg1, dmg2, 0\.5, 0, 100\)); // Error!

In the above example we have accidentally put the closing parenthesis for lerp in the wrong place.

var \_dmg \= clamp(lerp(dmg1, dmg2, 0\.5\), 0, 100\); // Fix!

### GM1020 \- The function 'FUNCTION NAME' takes no less than NUMBER arguments but NUMBER are provided.

This message is shown when less arguments are passed to a function than that function takes.

Possible causes can be:

- You're nesting function calls and missed a closing parenthesis )
- You have miscounted your arguments

#### Example

var \_dmg \= clamp(lerp(dmg1, dmg2\), 0\.5, 0, 100\); // Error!

The closing parenthesis for lerp is in the wrong place.  Placing it after the 0\.5 value instead fixes the error.

var \_dmg \= clamp(lerp(dmg1, dmg2, 0\.5\), 0, 100\); // Fix!

### GM1021 \- The function or script 'FUNCTION/SCRIPT NAME' does not exist.

This message is shown when a call to a non\-existent script or function is made. This may be shown if you typo the function name, or have deleted the function.

#### Example

function make\_game(\_genre) { /\* ... \*/ }  

 make\_gaem("RPG"); // GM1021  

 var \_x \= clam(x, 0, 100\); // GM1021

Correct any typos, and ensure the functions you're trying to call exist.

function make\_game(\_genre) { /\* ... \*/ }  

 make\_game("RPG"); // Fix!  

 var \_x \= clamp(x, 0, 100\); // Fix!

### GM1022 \- An assignment was expected at this time.

This message is shown when a variable name is written as the left\-hand side of an assignment and isn't followed by the assignment operator \=.

Note that this does not apply to the var statement, as var a; suffices as a declaration.

#### Example

username                                // Error!  

 // OR  

 username;                               // Error!

An identifier cannot stand on its own in a statement. The issue can be fixed by using it in an assignment or by calling it as a function (in case it refers to a valid script function).

username \= get\_string("Username:", ""); // Valid Assignment!  

 username(); // Function Call is also possible

### GM1023 \- The constant 'BUILT\-IN CONSTANT' is deprecated and usage is discouraged.

This message indicates that you're using a built\-in constant that is deprecated.

Deprecation means that while the constant is still available for usage, it is planned to be removed in the future. Typically when something is deprecated a superior approach exists and is intended to be used instead. You should research what the alternative is and use that instead to avoid your code from breaking when you update GameMaker to newer versions.

#### Example

if (os\_type \=\= os\_win32\) { // GM1023 \- Constant 'os\_win32' is deprecated  

     global.config \= 0;  

 }  

 else if (os\_type \=\= os\_macosx) {  

     global.config \= 1;  

     global.config \= 2;  

 }

Depending on the constant, a replacement may be available. Check the manual to see if the page mentions this replacement. For the above example, the modern constant is os\_windows (as to not imply a difference between detection of 32\-bit and 64\-bit Windows).

if (os\_type \=\= os\_windows) {  

     global.config \= 0;  

 }  

 else if (os\_type \=\= os\_macosx) {  

     global.config \= 1;  

     global.config \= 2;  

 }

### GM1024 \- The built\-in variable 'BUILT\-IN VARIABLE' is deprecated and usage is discouraged.

This message indicates that you're using a built\-in variable that is deprecated.

Deprecation means that while the variable is still available for usage, it is planned to be removed in the future. Typically when something is deprecated a superior approach exists and is intended to be used instead. You should research what the alternative is and use that instead to avoid your code from breaking when you update GameMaker to newer versions.

#### Example

/// Create Event  

 score \= 0;  

  

 /// Step Event  

 var \_ins \= instance\_position(mouse\_x, mouse\_y, obj\_balloon);  

 if (\_ins !\= noone)  

 {  

     score\+\+;  

     instance\_destroy(\_ins);  

 }
 

Replace the variable with a custom variable or a macro, depending on what works best in the specific case.

/// Create Event  

 points \= 0;  

  

 /// Step Event  

 var \_ins \= instance\_position(mouse\_x, mouse\_y, obj\_balloon);  

 if (\_ins !\= noone)  

 {  

     points\+\+;  

     instance\_destroy(\_ins);  

 }
 

### GM1025 \- A number literal was unexpected at this time.

This message is shown when you use a number literal outside of an expression where it cannot be used. It can occur when:

- A number literal is on its own in a statement
- A number literal is used as the left\-hand side of an assignment

#### Example

\#AEF033 // Error! Lone number literal  

 // OR:  

 \#AEF033; // Error! Lone number literal  

 // OR:  

 0xFFDE31 \= "value"; // Error! Left\-hand side is not a variable

The number literal has to be used as a function parameter or as the right\-hand side of an assignment.

colour \= \#AEF033;

### GM1026 \- Left\-hand side of postfix expression must be a variable.

This message is shown when you use a postfix increment (var\+\+) or decrement operator (var\-\-) on something that is not a variable. More precisely, it must be possible to assign to that which you'd normally write on the left\-hand side of the equivalent equation:

vari \= vari \+ 1;    // Equivalent of vari\+\+; \- Variable can be written to and so can go on the left\-hand side  

  

 pi \= pi \+ 1;      // Equivalent of pi\+\+; \- Constant cannot be written to so cannot go on left\-hand side
 

#### Example

pi\+\+;    // GM1026 Cannot increment a constant  

 // OR:  

 show\_debug\_message\-\-; // GM1026 Cannot decrement a function name

In the code example, pi is a constant and cannot be changed by definition. show\_debug\_message() is a function and is not a number which can be incremented/decremented. If you want to perform these operations you must first ensure the value is assigned to a variable.

var \_pi \= pi;  

 \_pi\+\+;

### GM1027 \- A string literal was unexpected at this time.

This message is shown when a string literal exists outside of a valid expression.

#### Example

"this is a string" // GM1027! A lone string!

The string literal should be assigned to a variable, or compared to a variable, or passed as an argument to a function call.

text \= "this is a string";  

 if (text \=\= "this is a string")  

 {  

     show\_debug\_message("this is a string");  

 }

### GM1028 \- Accessor is intended for type of 'TYPE' but 'TYPE' appears instead.

This message is shown when you address an element of a data structure using the accessor syntax and don't use the right operator for the data structure's type. Each type of data structure has its own accessor symbol that is used with it. See [Accessors](../../GameMaker_Language/GML_Overview/Accessors.md) for the full list.

 
Possible causes of this error can be:

- You've accidentally used the wrong accessor for the type of data structure you're accessing.
- You forgot the accessor symbol. In this case the lookup is interpreted as an array lookup.

#### Example

lst\_instances \= ds\_list\_create();  

 if (instance\_place\_list(x, y, obj\_enemy, lst\_instances, true))  

 {  

     var \_ins \= lst\_instances\[? 0]; // GM1028! Wrong accessor  

     show\_debug\_message($"The closest instance is {real(\_ins)}.");  

 }

In the code example above, a DS list is populated with instances of an object obj\_enemy. When there are any instances in the list, the first one is accessed. The pipe character \| is for accessing DS lists, however the list is incorrectly accessed with a ?, which is for DS maps. Changing the operator fixes the issue by addressing the data structure using the correct accessor.

lst\_instances \= ds\_list\_create();  

 if (instance\_place\_list(x, y, obj\_enemy, lst\_instances, true))  

 {  

     var \_ins \= lst\_instances\[\| 0]; // Good!  

     show\_debug\_message($"The closest instance is {real(\_ins)}.");  

 }

### GM1029 \- Potentially dangerous or unintended implicit cast from 'TYPE' to 'TYPE'.

This message is shown when you pass an argument to a function parameter whose type differs from the type expected, but can and will be converted to the expected. While legal, this tends to be unfavourable code as the runtime does its best guess as to how the data should be converted which may lead to unexpected bugs or errors. For example, passing the string "1234" to draw\_sprite()'s 3rd parameter x is legal, the runtime will convert the String to the Real of the same value. However, if the string value could not convert to a type Real value then you would encounter a runtime error. The cast is implicit since the runtime does it for you instead of you calling the real() built\-in function, and it's dangerous because it may or may not crash at runtime depending on how sanitary you keep your data.

 
#### Example

var \_x \= "1234";  

 var \_y \= "4321";  

 draw\_sprite(sprite\_index, image\_index, \_x, \_y); // GM1029

The fix for this message is to either make the cast explicit using one of the built\-in functions (e.g. [string](../../GameMaker_Language/GML_Reference/Strings/string.md), [real](../../GameMaker_Language/GML_Reference/Variable_Functions/real.md), etc.) or to rewrite the code so that you do not depend on the dangerous usage of that data type.

var \_x \= 1234;  

 var \_y \= y;  

 draw\_sprite(sprite\_index, image\_index, \_x, real(\_y)); // Fix!

### GM1030 \- The identifier 'NAME' is reserved and cannot be used as a variable or macro name.

Some identifier names are reserved by the compiler and runtime and cannot be used in local or static variable declarations or in macro declarations. Keep in mind that in Constructor Function scopes some built\-in variables are actually available for usage since they do not resolve to a built\-in in those places. These tend to be built\-in variables that modify some property of an Object such as sprite\_index, or x and y.

#### Example

var image\_index \= 1; // GM1030  

 function SpriteData() constructor {  

     var image\_index \= 1; // Good!  

 }

The fix is to find another, non\-conflicting name to use for your variable instead.

var \_image\_index \= 1; // Fix!  

 function SpriteData() constructor {  

      var image\_index \= 1; // Good!  

 }

### GM1031 \- The name 'IDENTIFIER' is an asset or constant and cannot be assigned to.

This message is shown when you try to assign a value to an asset or a constant. Assets and constants cannot be changed and are meant to be used stand alone on the right\-hand side of statements, in conditionals, or in expressions.

#### Example

obj\_control \= 75; // GM1035! Cannot assign value to Asset type  

 pi \= 1\.618; // GM1035! Cannot assign value to constant

Depending on the intention, either the name of the variable to be assigned to can be changed or the asset or constant should be moved to the right\-hand side of the assignment.

control \= 75;  

 value \= pi;

### GM1032 \- No references to arguments INDEX, … but references argument INDEX

This message is shown when referencing an argument in a function via the argument0\..argument15 built\-in variables, and one or more indices have been skipped. While the arguments may be referenced in any order all indices 0\..n must be referenced at least once; where n is the number of arguments in your function. If the code changes so that it no longer accesses e.g. argument0, all other arguments need to be changed; argument1 becomes argument0, argument2 becomes argument1, etc.

See: [argument](../../GameMaker_Language/GML_Overview/Variables/Builtin_Global_Variables/argument.md)

#### Example

function args() {  

     var \_x \= argument0;  

     var \_y \= argument2; // GM1032! Missing reference to argument1  

 }

Replace the argument\# variable with the first unused argument\# variable.

function args() {  

     var \_x \= argument0;  

     var \_y \= argument1; // Fix!  

 }

### GM1033 \- Possibly unintended or misplaced semicolon.

This message is shown when there is a semicolon in the code that might be unnecessary at that position.

#### Example

var \_a \= 3434;;

The double semicolon is not needed and can be removed.

var \_a \= 3434;

### GM1034 \- Argument cannot be referenced outside of script or function.

This message indicates that one of the built\-in variables argument0 \- argument15 or the built\-in variable argument (argument\[0], argument\[1], etc.) has been referenced outside of the scope of a function or script. These built\-in variables are only legal inside functions, i.e. inside the opening and closing curly braces.

#### Example

function args()  

 {  

       

 }  

 var \_first\_parameter \= argument\[0];  

 var \_second\_parameter \= argument\[1];

In this case the reference of the built\-in variables is intended, they should be moved inside the curly braces. If the references aren't intended to be used, they should be removed.

function args()  

 {  

     var \_first\_parameter \= argument\[0];  

     var \_second\_parameter \= argument\[1];  

 }

### GM1035 \- Return type differs from previously established return type.

This message is shown when your JSDoc differs from the type returned in code or if Feather determines that you've returned multiple different non\-compatible types from the same function. A non\-compatible type would be something like Real, and String both being returned from the same function. Where something like Real, and Undefined might be compatible since undefined is commonly used to indicate no result. Returning different types of data is sometimes a valid strategy but it is typically dangerous since consuming code may assume that only one type of data will be returned, which may result in runtime errors or strange behaviour in the calling code.

 
#### Example

/// @returns {real}  

 function get\_random\_number() {  

     return "1"; // GM1035!  

 }  

 function get\_random\_number2() { // no JSDoc here  

     if (irandom(100\) \< 50\)  

         return 0; // Return type is established here as 'Real'  

     return "1"; // GM1035!  

 }

The fix for this is to either update your JSDoc accordingly, or to rewrite your code to ensure that the same type is returned from all return statements.

/// @returns {string}  

 function get\_random\_number() {  

     return "1"; // Fixed! But maybe rename the function!  

 }  

 function get\_random\_number2() { // no JSDoc here  

     if (irandom(100\) \< 50\)  

         return 0; // Return type is established here as 'Real'  

     return 1; // Fix!  

 }

### GM1036 \- Array cannot be indexed in this way.

This message is shown if you index into an array with either 0 indices, or too many indices for the dimensionality of the array. Keep in mind that the 2D array syntax is deprecated in favour of staggered array indexing.

#### Example

function choose2d() {  

     var \_x \= irandom(argument\_count);  

     var \_y \= irandom(argument\_count);  

     return argument\[\_x, \_y]; // GM1036! argument array is not 2d  

 }  

 var \_arr \= \[ 1, 2, 3, 4 ];  

 var \_idx \= \_arr\[]; // GM1036!

The fix for this issue is to either provide the index, or to rethink how you're accessing the array.

function choose2d(\_arr) {  

     var \_x \= irandom(array\_height\_2d(\_arr));  

     var \_y \= irandom(array\_length\_2d(\_arr));  

     return \_arr\[\_x, \_y]; // Fix! Keep in mind this syntax is deprecated  

 }  

 var \_arr \= \[ 1, 2, 3, 4 ];  

 var \_idx \= \_arr\[0]; // Fix!

### GM1038 \- Macro with this name has been previously declared.

This message indicates that you defined a macro with the same name before, somewhere in your code. Project\-wide search (Ctrl\+Alt\+F) can be useful in this case to check how many occurrences of the macro are in your project. Look for \#macro \ to find all definitions of this macro.

#### Example

/// Script Asset: Debug  

 \#macro dbg show\_debug\_message  

  

 /// Script Asset: Utility  

 \#macro dbg show\_debug\_message
 

Remove all duplicate macro definitions until there is one left.

/// Script Asset: Debug  

 \#macro dbg show\_debug\_message

### GM1040 \- argument\# and argument\[\#] referencing cannot be mixed.

This message indicates that the argument array variable and argument0 \- argument15 variables are used together in a function. The former is used in functions that support a variable number of arguments, the latter is used when you know the number of arguments in advance. In any function, you should only ever use one of the two.

See: [argument](../../GameMaker_Language/GML_Overview/Variables/Builtin_Global_Variables/argument.md)

#### Example

function func()  

 {  

    var \_a \= argument0;  

    var \_b \= argument\[1];  

 }

Change all argument\[n]/argumentn variables to the same type of referencing, depending on what's needed in the function.

function func()  

 {  

    var \_a \= argument0;  

    var \_b \= argument1;  

 }  

 // OR:  

 function func()  

 {  

    var \_a \= argument\[0];  

    var \_b \= argument\[1];  

 }

### GM1041 \- The type 'TYPE' appears where the type 'TYPE' is expected.

This message is shown when you pass an argument to a function call's parameter of a different type. For example, passing a Id.Instance to a String parameter.

#### Example

var \_inst \= instance\_create\_depth(x, y, \-100, "obj\_player"); // GM1041!

The fix is to determine what the correct type to pass to the parameter is, and rewrite your code accordingly.

var \_inst \= instance\_create\_depth(x, y, \-100, obj\_player); // Fix!

### GM1042 \- Parameter name 'PARAMETER' differs from 'PARAMETER' specified in jsdoc.

This message is shown when there is a difference between a function's parameter name in the JSDoc and its corresponding parameter name in the argument list. This could have a couple of causes:

- There is a typo in the variable name in the JSDoc or in the argument list.
- You renamed the parameter name in the argument list but not in the JSDoc or vice versa.

#### Example

/// @func sum(\_v1, \_v2\);  

 /// @desc This function returns the sum of two 3\-component vectors  

 /// @arg {Array\} \_v1 The first vector  

 /// @arg {Array\} \_v2 The second vector  

 function sum(\_v, \_v2\)  

 {  

     return \[  

         \_v1\[0] \+ \_v2\[0],  

         \_v1\[1] \+ \_v2\[1],  

         \_v1\[2] \+ \_v2\[2]  

     ];  

 }

To fix this issue you need to change the incorrectly named variable to the correct one to make sure both names correspond.

/// @func sum(\_v1, \_v2\);  

 /// @desc This function returns the sum of two 3\-component vectors  

 /// @arg {Array\} \_v1 The first vector  

 /// @arg {Array\} \_v2 The second vector  

 function sum(\_v1, \_v2\)  

 {  

     return \[  

         \_v1\[0] \+ \_v2\[0],  

         \_v1\[1] \+ \_v2\[1],  

         \_v1\[2] \+ \_v2\[2]  

     ];  

 }

### GM1043 \- Potentially unintentional type reassignment from '{0}' to '{1}'.

This message is shown when you assign a new value to an existing variable and the type of the new value is different from the type that the variable currently holds.

This may not cause any issues, though it could make it more difficult to interpret your GML code correctly when you use the same variable name multiple times.

It is good practice to keep the data type that you store in a variable constant, even though GameMaker doesn't enforce this in any way.

 
#### Example

// Store a real number in my\_var  

 my\_var \= 5;  

  

 // Next store a string in my\_var  

 my\_var \= "I'm a string";  // type reassignment!
 

This issue can be fixed in multiple ways, it depends on what you're trying to do in your code. If the string has a different purpose in your code you could store it in a different variable with an appropriate name.

// Store a real number in my\_var  

 my\_var \= 5;  

  

 // Store a new real number in my\_var  

 my\_var \= 100;  

  

 // Store a string in a new variable my\_string  

 my\_string \= "I'm a string";
 

### GM1044 \- Constant is expected to be one of the following: {0}

This message is shown whenever one constant from a group of constants is expected as an argument and you've provided a value that's not in that group. Examples of these groups of constants are the Mouse Button Constants, the Game Speed Constants and the Primitive Type Constants. A constant from another group or a real number may accidentally work but it is not good practice to use them. Using the right constant in the right place helps increase the readability of your code.

#### Example

// Example 1  

 if mouse\_check\_button\_pressed(mb\_midle)  

 {  

 }  

  

 // Example 2  

 if mouse\_check\_button\_pressed(vk\_left)  

 {  

 }
 

If this was caused by a typo, then fixing the typo fixes it. In other cases the constant needs to be changed to a valid one.

// Example 1  

 if mouse\_check\_button\_pressed(mb\_middle)  

 {  

 }  

  

 // Example 2  

 if mouse\_check\_button\_pressed(mb\_left)  

 {  

 }
 

### GM1045 \- Type '{0}' differs from type '{1}' specified in jsdoc.

This message is shown when Feather detects that the type of a variable in your code doesn't correspond to the type the JSDoc says that variable should be.

This can happen when you write the JSDoc already, but decide to change the code afterwards. In that case, the JSDoc will no longer be up to date and needs to be changed to reflect the changes.

#### Example

/// @func return\_something()  

 /// @desc This function returns something  

 ///  

 /// @returns {Id.Instance} A new instance  

 ///  

 function return\_something()  

 {  

     return "something";  

 }

In the code example above the JSDoc says the function returns an instance ID, but the code actually returns a string. If this is the intent, the type in the JSDoc needs to be changed to String to reflect that. If not, the code needs to be changed so it returns an instance.

/// @func return\_something()  

 /// @desc This function returns something  

 ///  

 /// @returns {String} The string "something"  

 ///  

 function return\_something()  

 {  

     return "something";  

 }

### GM1050 \- The identifier '{0}' is declared as a local variable and cannot be accessed in this way.

This message is shown when you attempt to access a local variable (defined with the var keyword) using the dot operator. The dot operator accesses a different scope, though local variables are already in the current scope.

#### Example

/// Create Event  

 var \_condition \= false;  

 if (self.\_condition)    // Error! Variable is local...  

 {  

 }

A local (or temporary) variable should always be used without a prefix that refers to a scope. The scope of local variables is always the current block of code.

var \_condition \= false;  

 if (\_condition)  

 {  

 }

### GM1051 \- Macro expressions should not be terminated with a ';' semicolon.

This message is shown when you end a macro definition with a semicolon. Macros can go anywhere in your code and are replaced by their value. Any semicolons in the macro's value are also inserted and may end up in places where they cause a syntax error.

See the section on Macros on the [Constants](../../GameMaker_Language/GML_Overview/Variables/Constants.md) page for more info.

#### Example

randomise();  

  

 \#macro NEW\_COLOR make\_color\_rgb(random(255\), random(255\), random(255\));  

  

 draw\_primitive\_begin(pr\_trianglelist);  

  

 repeat(3\)  

 {  

     draw\_vertex\_color(random(room\_width), random(room\_height), NEW\_COLOR, 1\);    // Issue!  

 }  

  

 draw\_primitive\_end();
 

Inserting the macro into the function call leads to a semicolon being inserted right after the third argument. This is incorrect, since this semicolon marks the end of the statement while the function call still needs an additional parameter and also has to be closed with a parenthesis. Removing the semicolon at the end of the macro fixes the issue.

// The semicolon that gets inserted as part of the macro causes a syntax error:  

 // draw\_vertex\_color(random(room\_width), random(room\_height), make\_color\_rgb(random(255\), random(255\), random(255\));, 1\);  

 randomise();  

  

 \#macro NEW\_COLOR make\_color\_rgb(random(255\), random(255\), random(255\))  

  

 draw\_primitive\_begin(pr\_trianglelist);  

  

 repeat(3\)  

 {  

     draw\_vertex\_color(random(room\_width), random(room\_height), NEW\_COLOR, 1\);    // Fixed!  

 }  

  

 draw\_primitive\_end();
 

### GM1052 \- The delete operator can only act on a variable of type 'struct'.

The [new](../../GameMaker_Language/GML_Overview/Language_Features/new.md) and [delete](../../GameMaker_Language/GML_Overview/Language_Features/delete.md) operators are specifically for use with structs. Instances are destroyed using instance\_destroy(), arrays are garbage\-collected once they're no longer referenced and other resource types have their own functions to handle deleting/freeing them (a \*\_destroy or \*\_free function).

values \= \[2, 403, 202, 303, 773, 573];  

 delete values;

To fix this the appropriate function or method should be used which, for arrays, is setting the variable to undefined.

values \= undefined;

### GM1054 \- Cannot inherit from non\-existent function '{0}'.

This message is shown when the constructor that a constructor is inheriting from doesn't exist. Possible causes are:

- The constructor to inherit from still needs to be defined.
- The function must be marked as a constructor by adding the constructor keyword.
- There is a typo in the inherited constructor name.

See: [Structs \& Constructors](../../GameMaker_Language/GML_Overview/Structs.md)

#### Example

function vec2() : vec()  

 {  

 }

The code example above attempts to create an inherited constructor function, but some things are missing. First, the constructor to inherit from, vec, isn't defined yet. Second, the function isn't marked as a constructor with the constructor keyword. To fix the error the parent constructor should be defined and the constructor keyword be added to both.

function vec() constructor {}  

 function vec2() : vec() constructor  

 {  

 }

### GM1055 \- Cannot mix argument\# and named parameters.

This message indicates that you've used one of the argumentn variables while the function parameters are defined as named parameters. For every function either one or the other should be used.

#### Example

function func(\_a, \_b, \_c) {  

     show\_debug\_message($"{argument0}, {argument1}, {argument2}");  

 }

In the code example above the parameters are already defined as named parameters. Replacing the occurrences of argument0 \- argument2 in the function body fixes this issue. argument0 is replaced with \_a, argument1 is replaced with \_b and argument2 is replaced with \_c. So every argument is replaced with the named argument at the corresponding index.

function func(\_a, \_b, \_c) {  

     show\_debug\_message($"{\_a}, {\_b}, {\_c}");  

 }

### GM1056 \- Bad practice to declare non\-optional parameter after an optional parameter.

This message is shown when you list optional parameters before non\-optional parameters. As a consequence, in order to use the default value of those optional parameters it's necessary to omit the argument. All optional parameters should go at the end of the parameter list.

See the section on [Optional Arguments](../../GameMaker_Language/GML_Overview/Script_Functions.md#h) on the [Script Functions And Variables](../../GameMaker_Language/GML_Overview/Script_Functions.md) page.

#### Example

function func(arg1, arg2, arg3\=7, arg4\)  

 {  

 }  

 func(4, 5, , 8\);  // the third parameter has to be omitted to use the default value

This can be fixed by changing the order of the function parameters such that all optional parameters and their default values go at the end of the parameter list.

function func(arg1, arg2, arg4, arg3\=7\)  

 {  

 }  

 func(4, 5, 8\);

### GM1058 \- Cannot 'new' the identifier '{0}' as it is not a constructor function.

This message is shown when you try to call the [new](../../GameMaker_Language/GML_Overview/Language_Features/new.md) operator with a valid function name that's not marked as a constructor.

#### Example

function item()  

 {  

 }  

 sword \= new item();

In order to fix this error the constructor keyword must be added to the function definition.

function item() constructor  

 {  

 }  

 sword \= new item();

### GM1059 \- The parameter '{0}' has been previously declared.

This message is shown when the same parameter name occurs multiple times in a function's parameter list.

#### Example

function func(\_param1, \_param2, \_param1\)  

 {  

 }

Depending on what is intended, the parameter should either be removed or renamed.

// Option 1: Remove double  

 function func(\_param1, \_param2\)  

 {  

 }  

 // Option 2: Rename the parameter  

 function func(\_param1, \_param2, \_param3\)  

 {  

 }

### GM1060 \- Dangerous call to variable of type '{0}'.

Shown when you try to call something that is not a function.

#### Example

my\_function \= 100;  

 my\_function();  

 my\_function \= pi;  

 my\_function();

### GM1062 \- Malformed type '{0}' in jsdoc.

This message indicates that Feather is unable to parse a parameter or return type in the function's JSDoc. The supported syntax is given on the [Feather Data Types](Feather_Data_Types.md) page.

#### Example

/// @function func(\_param1, \_param2, \_param3\)  

 /// @desc This function does something  

 /// @param {Array\[String} \_param1 This is parameter 1  

 /// @param {String Array\[String]} \_param2 This is parameter 2  

 /// @param {Id Instance} \_param3 This is parameter 3  

 function func(\_param1, \_param2, \_param3\)  

 {  

     show\_debug\_message("The parameters are: {0}, {1} and {2}", \_param1, \_param2, \_param3\);  

 }

The JSDoc types in the code example above can be corrected as follows:

/// @function func(\_param1, \_param2, \_param3\)  

 /// @desc This function does something  

 /// @param {Array\[String]} \_param1 This is parameter 1  

 /// @param {String,Array\[String]} \_param2 This is parameter 2  

 /// @param {Id.Instance} \_param3 This is parameter 3  

 function func(\_param1, \_param2, \_param3\)  

 {  

     show\_debug\_message("The parameters are: {0}, {1} and {2}", \_param1, \_param2, \_param3\);  

 }

### GM1063 \- Ternary may yield differing types '{0}' and '{1}'.

This message is shown when a ternary operator returns a type of value in the true case that's different from the type in the false case or vice versa. As a consequence, the variable that's assigned to may receive a different type, depending on the outcome of the condition.

#### Example

/// Create Event  

 tex \= (texture\_defined) ? sprite\_get\_texture(sprite\_index, 0\) : \-1;  

  

 /// Draw Event  

 vertex\_submit(vb, pr\_trianglelist, tex);
 

This can be fixed by explicitly converting the type returned in one of the cases to the type of the other case.

### GM1064 \- Redeclaration of global function '{0}' originally declared in '{1}'.

This message indicates that you've already declared a global function with the same name in another script asset.

#### Example

/// Script1  

 function make\_game()  

 {  

 }  

  

 /// Script2  

 function make\_game()  

 {  

 }
 

One of the function definitions should be removed so that only one remains in the global namespace. If you want to create two functions with the same name then it is possible to create them as static functions within two different functions. The functions in which you define the static functions then act as a namespace.

/// Script1  

 function make\_game()  

 {  

 }

### GM1100 \- Syntax Error

This message indicates a general syntax error in your code. Syntax errors cover a range of possible errors related to the syntax of your code.

#### Example

var \_this \* something;  

 \= 48;

### GM2000 \- Not all code paths call gpu\_set\_blendmode(bm\_normal) before the end of the script.

This message is shown when you change the blend mode to a value different from bm\_normal with a call to [gpu\_set\_blendmode](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_blendmode.md) but don't change it back to bm\_normal afterwards. After drawing something with a different blend mode it is important to set blending back to normal so everything that's drawn after it is drawn correctly.

#### Example

/// Draw Event  

 gpu\_set\_blendmode(bm\_add);  

 draw\_self();  

  

 /// Draw GUI Event  

 draw\_text(5, 5, $"Score: {score}");
 

The code in the example intends to draw an instance with added blending in its normal Draw event and some text with normal blending in its Draw GUI event. However, no call to reset the blend mode back to bm\_normal is made in the Draw event and so the text in the Draw GUI event is also drawn using additive blending. Another call to gpu\_set\_blendmode needs to be added at the end of the Draw event to reset the blending back to bm\_normal.

/// Draw Event  

 gpu\_set\_blendmode(bm\_add);  

 draw\_self();  

 gpu\_set\_blendmode(bm\_normal);  

  

 /// Draw GUI Event  

 draw\_text(5, 5, $"Score: {score}");
 

### GM2003 \- Not all code paths call shader\_reset() before end of script.

This error is shown when a call to the function [shader\_reset](../../GameMaker_Language/GML_Reference/Asset_Management/Shaders/shader_reset.md) is missing after drawing using a custom shader (set with [shader\_set](../../GameMaker_Language/GML_Reference/Asset_Management/Shaders/shader_set.md)). When the shader isn't set back to the default shader after drawing using a custom shader, everything that's drawn after that is also drawn using that shader.

#### Example

/// Draw Event  

 shader\_set(sh\_fancy\_lighting);  

 vertex\_submit(vb\_my\_world\_model, pr\_trianglelist, \-1\);  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "World 1");  // Also drawn using sh\_fancy\_lighting
 

The call to shader\_set should be accompanied with a call to shader\_reset.

/// Draw Event  

 shader\_set(sh\_fancy\_lighting);  

 vertex\_submit(vb\_my\_world\_model, pr\_trianglelist, \-1\);  

 shader\_reset();  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "World 1");
 

### GM2004 \- This for statement does not use its index and can be written as a repeat statement instead.

This message indicates that the [for](../../GameMaker_Language/GML_Overview/Language_Features/for.md) statement has a loop counter that is never used, e.g. to index an array. When the number of iterations is known in advance and doesn't depend on a condition the for loop doesn't need a counter and can be replaced by a [repeat](../../GameMaker_Language/GML_Overview/Language_Features/repeat.md) statement.

#### Example

randomise();  

 var \_num\_elements \= 20;  

 array \= \[];  

  

 for(var i \= 0;i \< \_num\_elements;i\+\+)  

 {  

     array\_push(array, irandom(100\));  

 }
 

The for loop in the example code above doesn't use its index. In this specific situation, the function used (array\_push()) automatically appends to the end of the array so the index doesn't have to be provided explicitly.

randomise();  

 var \_num\_elements \= 20;  

 array \= \[];  

  

 repeat(\_num\_elements)  

 {  

     array\_push(array, irandom(100\));  

 }
 

### GM2005 \- Not all code paths call surface\_reset\_target() before end of script.

This error indicates that you changed the draw target with a call to [surface\_set\_target](../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_set_target.md) but haven't set it back with a call to [surface\_reset\_target](../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_reset_target.md) in all situations.

See: [Surfaces](../../GameMaker_Language/GML_Reference/Drawing/Surfaces/Surfaces.md)

#### Example

/// Draw Event  

 if (!surface\_exists(sf\_canvas))  

 {  

     sf\_canvas \= surface\_create(512, 512\);  

 }  

  

 surface\_set\_target(sf\_canvas);  

 draw\_clear\_alpha(c\_white, 0\);  

 draw\_rectangle(4, 4, 40, 40\);
 

In the example code above the drawing target is still set to sf\_canvas after the block of code has executed. Further draw commands will also draw to this surface. A call to surface\_reset\_target() is needed at the end to reset the drawing target.

/// Draw Event  

 if (!surface\_exists(sf\_canvas))  

 {  

     sf\_canvas \= surface\_create(512, 512\);  

 }  

  

 surface\_set\_target(sf\_canvas);  

 draw\_clear\_alpha(c\_white, 0\);  

 draw\_rectangle(4, 4, 40, 40\);  

 surface\_reset\_target();
 

### GM2007 \- var expression should be terminated with a ';' (semicolon.)

This message indicates that a semicolon ; is missing at the end of a var statement. Local variables can be declared without immediately assigning them a value, but this declaration needs to be terminated with a semicolon.

#### Example

var a

A semicolon needs to be added at the end of the statement to fix this.

var a;

### GM2008 \- Opening another vertex batch before closing a previous vertex batch.

This message is shown when you start another vertex batch with a call to [vertex\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_begin.md) before having called [vertex\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_end.md) for the current batch. Every call to vertex\_begin() must be followed by a call to vertex\_end() before a next call to vertex\_begin().

#### Example

vertex\_begin(vb, format);  

  

 // vertex\_position\_3d(...)  

 // vertex\_color(...)  

 // vertex\_texcoord(...)  

 // etc.  

 vertex\_begin(vb, format);    // Error!  

  

 // vertex\_position\_3d(...)  

 // vertex\_color(...)  

 // vertex\_texcoord(...)  

 // etc.  

 vertex\_end(vb);
 

In the example above two calls to vertex\_begin() follow each other without a call to vertex\_end() between them. Adding a call to vertex\_end() in between fixes the issue.

vertex\_begin(vb, format);  

 // vertex\_position\_3d(...)  

 // vertex\_color(...)  

 // vertex\_texcoord(...)  

 // etc.  

 vertex\_end(vb);              // End the current one first!  

  

 vertex\_begin(vb, format);    // Only then start a new one!  

 // vertex\_position\_3d(...)  

 // vertex\_color(...)  

 // vertex\_texcoord(...)  

 // etc.  

 vertex\_end(vb);
 

### GM2009 \- Closing a vertex batch without opening a vertex batch.

This message is shown when you close a vertex batch with a call to [vertex\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_end.md) before starting the batch with a call to [vertex\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_begin.md). You first need to start the vertex batch with a call to vertex\_begin(), then add vertex data according to the vertex format for the desired number of vertices and finally close the batch with a call to vertex\_end().

#### Example

vertex\_end(vb);

In the example code above a vertex batch is closed using vertex\_end() without ever being opened. The fix is to add a call to vertex\_begin() and add data for the vertices before the call to vertex\_end().

vertex\_begin(vb, format);  

 // vertex\_position\_3d(...)  

 // vertex\_color(...)  

 // vertex\_texcoord(...)  

 // etc.  

 vertex\_end(vb);

### GM2010 \- The function '{0}' cannot be called outside of a vertex\_begin()/vertex\_end() block.

This message is shown when you're attempting to call a function that writes vertex data outside of [vertex\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_begin.md) / [vertex\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_end.md). Vertex data can only be added after first calling vertex\_begin() and before calling vertex\_end().

#### Example

/// Create Event  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 format \= vertex\_format\_end();  

 vb \= vertex\_create\_buffer();  

  

 vertex\_begin(vb, format);  

 vertex\_end(vb);  

 vertex\_position\_3d(vb, x, y, 0\);  

 vertex\_position\_3d(vb, x \+ 100, y, 0\);  

 vertex\_position\_3d(vb, x, y \+ 100, 0\);
 

In the code example above, the function calls to write positions to the vertex buffer come after vertex\_end(). To fix this they need to be moved between vertex\_begin() and vertex\_end().

/// Create Event  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 format \= vertex\_format\_end();  

 vb \= vertex\_create\_buffer();  

  

 vertex\_begin(vb, format);  

 vertex\_position\_3d(vb, x, y, 0\);  

 vertex\_position\_3d(vb, x \+ 100, y, 0\);  

 vertex\_position\_3d(vb, x, y \+ 100, 0\);  

 vertex\_end(vb);
 

### GM2011 \- Not all code paths call vertex\_end() before the end of the script.

This message indicates that you started writing vertex data to a vertex buffer but haven't properly finished writing the data with a closing call to [vertex\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_end.md). Every call to [vertex\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_begin.md) should be accompanied by a call to [vertex\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_end.md). To write data to a vertex buffer you should do the following:

#### Example

/// Create Event  

 vb \= vertex\_create\_buffer();  

 vertex\_begin(vb, format);  

 vertex\_position\_3d(vb, 0, 0, 0\);  

 vertex\_colour(vb, c\_white, 1\);  

 // Etc.  

  

 /// Draw Event  

 vertex\_submit(vb, pr\_pointlist, \-1\);
 

In the code example above, the vertex buffer isn't properly finished because a call to vertex\_end() is missing. This needs to be added to fix the issue.

/// Create Event  

 vb \= vertex\_create\_buffer();  

 vertex\_begin(vb, format);  

 vertex\_position\_3d(vb, 0, 0, 0\);  

 vertex\_colour(vb, c\_white, 1\);  

 // Etc.  

 vertex\_end(vb);  

  

 /// Draw Event  

 vertex\_submit(vb, pr\_pointlist, \-1\);
 

### GM2012 \- Opening another vertex format before closing a previous vertex format.

This message is shown when you begin a new vertex format with [vertex\_format\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_format_begin.md) before finishing the previous one with a call to [vertex\_format\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_format_end.md). A vertex format must always be closed before starting a new one.

#### Example

/// Create Event  

 vertex\_format\_begin();  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 format1 \= vertex\_format\_end();  

 vertex\_format\_add\_position\_3d();  

 vertex\_format\_add\_texcoord();  

 format2 \= vertex\_format\_end();

In the example code above, one vertex format definition is nested inside another one. As a result, a vertex format is being defined while another one's definition hasn't finished. To fix this, all vertex formats should be defined one after the other:

/// Create Event  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 format1 \= vertex\_format\_end();  

  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 vertex\_format\_add\_texcoord();  

 format2 \= vertex\_format\_end();
 

### GM2013 \- Closing a vertex format without opening a vertex format.

This message is shown when you close a vertex format with [vertex\_format\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_format_end.md) without first having called [vertex\_format\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_format_begin.md).

#### Example

/// Create Event  

 format \= vertex\_format\_end();

The code example above closes the vertex format without ever having started it with a call to vertex\_format\_begin(). The vertex format should be opened with a call to this function and at least one vertex attribute should be added to it using one of the vertex\_format\_add\_\* functions.

/// Create Event  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 format \= vertex\_format\_end();

### GM2014 \- The function '{0}' cannot be called outside of a vertex\_format\_begin()/vertex\_format\_end() block.

The vertex\_format\_add\_\* functions can only be called between a call to [vertex\_format\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_format_begin.md) and [vertex\_format\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_format_end.md). The function vertex\_format\_begin() starts the vertex format, calls to vertex\_format\_add\_\* define the vertex format's attributes and the function vertex\_format\_end() ends the definition of the vertex format and returns it.

#### Example

/// Create Event  

 vertex\_format\_add\_position\_3d();  

 vertex\_format\_add\_colour();  

 vertex\_format\_add\_texcoord();  

 vertex\_format\_begin();  

 format \= vertex\_format\_end();

In the code example above, the vertex\_format\_add\_\* functions are called before the call to vertex\_format\_begin() that begins the actual definition of a vertex format. These functions always go between vertex\_format\_begin() and vertex\_format\_end(). Moving the call to vertex\_format\_begin() before the first vertex\_format\_add\_\* call fixes the issue.

/// Create Event  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 vertex\_format\_add\_colour();  

 vertex\_format\_add\_texcoord();  

 format \= vertex\_format\_end();

### GM2015 \- Not all code paths call vertex\_format\_end() before the end of the script.

This message is shown when you started the definition of a vertex format with [vertex\_format\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_format_begin.md) but haven't finished it with a call to [vertex\_format\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_format_end.md). The call to vertex\_format\_end() returns the actual vertex format.

#### Example

/// Create Event  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 vertex\_format\_add\_colour();  

 vertex\_format\_add\_texcoord();

A vertex format definition isn't complete without a call to vertex\_format\_end() that returns the format. This needs to be added to fix the issue.

/// Create Event  

 vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 vertex\_format\_add\_colour();  

 vertex\_format\_add\_texcoord();  

 format \= vertex\_format\_end();

### GM2016 \- Instance variable '{0}' declared outside of Create event, declare with 'var' or move to Create event.

This message is shown when you declare an [instance variable](../../GameMaker_Language/GML_Overview/Variables/Instance_Variables.md "Instance Variables") outside of the Create event. Instance variables should always be created in the Create event to guarantee that you'll be able to access them in all other events.

When you don't define instance variables in the Create event, you might at one point run into a situation where that variable doesn't exist yet. For example, when you first define the instance variable in the Step event and only use it in the Step event, this won't cause problems. Though when you later decide to add a Begin Step event to the object and attempt to access the variable there, an error will be thrown when your game runs. This is because Begin Step events run before Step events and the first Step event hasn't run yet when the first Begin Step event runs.

#### Example

/// Create Event  

 ammo\_initialised \= false;  

  

 /// Begin Step Event  

  

 /// Step Event  

 if (!ammo\_initialised)  

 {  

     ammo \= 0;  

     ammo\_initialised \= true;  

 }  

 var \_ins\_ammo \= instance\_place(x, y, obj\_ammo);  

 if (\_ins\_ammo !\= noone)  

 {  

     // Collect ammo  

     ammo\+\+;  

     instance\_destroy(\_ins\_ammo);  

 }
 

This issue is fixed by moving the declaration of the variable to the object's Create event.

/// Create Event  

 ammo \= 0;  

  

 /// Begin Step Event  

 // Do something with ammo here  

  

 /// Step Event  

 var \_ins\_ammo \= instance\_place(x, y, obj\_ammo);  

 if (\_ins\_ammo !\= noone)  

 {  

     // Collect ammo  

     ammo\+\+;  

     instance\_destroy(\_ins\_ammo);  

 }
 

### GM2017 \- Inconsistent naming. Recommended name is '{0}'.

This message is shown when Feather encounters a name in your code that's not named according to the naming rules as defined under Feather Settings \> Naming Rules. The names can be asset names, names of variables in a particular scope (local, instance, etc.) as well as function, constructor, enum and macro names.

Note that Feather will check against your own naming rules when you customise them in the [Feather Preferences](../../Setting_Up_And_Version_Information/IDE_Preferences/Feather_Settings.md).

#### Example

var s \= sprSprite;  

 enum size  

 {  

     small,  

     medium,  

     large  

 }  

  

 function Show()  

 {  

     show\_debug\_message("Here it is!");  

 }
 

The code in the example above contains a few names that aren't named according to Feather's default naming rules. To make them consistent with these rules, the code should be changed to the following:

var \_s \= spr\_sprite;  

 enum SIZE  

 {  

     SMALL,  

     MEDIUM,  

     LARGE  

 }  

  

 function show()  

 {  

     show\_debug\_message("Here it is!");  

 }
 

### GM2018 \- Potentially dangerous variable declaration.

This warning message indicates that a declaration of a local variable inside a loop may cause unexpected results. Contrary to many other programming languages, GML does not scope local variables to the block level (indicated by the opening and closing curly braces { }) and also doesn't initialise them to a default value when they are only declared. This can lead to confusion as you might assume that the variable is re\-declared and reset to a default value at each new iteration of the loop, though this is not what happens. At the end of the current loop iteration a local variable declared inside of it does *not* go out of scope, keeps existing and in subsequent iterations the variable will still hold the value it was last assigned.

#### Example

for (var i \= 0; i \< array\_length(array); \+\+i)  

 {  

     var \_elem; // GM2018  

     if (i \=\= 0\)  

         \_elem \= array\[i];  

     else if (i \< 5\)  

         \_elem \= array\[i] \* 2;  

       

     add\_loot\_value(\_elem);  

 }

In the above code example, a local variable \_elem is declared inside a [for](../../GameMaker_Language/GML_Overview/Language_Features/for.md) loop without being assigned an initial value. In the if / else statement that follows, a value is assigned to \_elem if the index of the loop is any value from 0 to 4 (inclusive). In the iteration where i \=\= 5, \_elem will not be explicitly assigned a value and still hold the last assigned value.

The issue can be fixed by moving the variable declaration outside of the loop's body so it can no longer appear as if the variable is reset at the start of each loop iteration. Additionally, the logic to assign a value to the variable needs to be extended to make sure a new value is always assigned at every new iteration of the loop, no matter the loop index.

var \_elem;  

 for (var i \= 0; i \< array\_length(array); \+\+i)  

 {  

     if (i \=\= 0\)  

         \_elem \= array\[i];  

     else if (i \< 5\)  

         \_elem \= array\[i] \* 2;  

     else  

         \_elem \= 0;  // Loop indices \>\= 5  

       

     add\_loot\_value(\_elem);  

 }

### GM2019 \- Not all code paths call draw\_set\_valign(fa\_top) before the end of the script.

This warning message indicates that you changed the vertical text alignment to a value different from the default (fa\_top) but haven't changed it back afterwards.

#### Example

/// Draw GUI Begin Event  

 draw\_set\_valign(fa\_bottom);  

 draw\_text(5, room\_height\-5, "In the bottom\-left corner");  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "In the top\-left corner");
 

In the above code example, the vertical text alignment is set to bottom\-aligned and some text is drawn in the Draw GUI Begin event. The text alignment isn't reset to fa\_top, however, which causes text in the Draw GUI Event that follows it to be drawn mostly offscreen. This is because it is drawn bottom\-aligned at a position in the top\-left corner of the window. Resetting the vertical text alignment back to fa\_top fixes the issue.

/// Draw GUI Begin Event  

 draw\_set\_valign(fa\_bottom);  

 draw\_text(5, room\_height\-5, "In the bottom\-left corner");  

 draw\_set\_valign(fa\_top);  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "In the top\-left corner");
 

### GM2020 \- all cannot be referenced in this way.

This message is shown when you attempt to reference the keyword [all](../../GameMaker_Language/GML_Overview/Instance Keywords/all.md) in the dot operator. The keyword all can be used in a [with](../../GameMaker_Language/GML_Overview/Language_Features/with.md) statement to indicate that it should loop through all instances, but it cannot be used with the dot operator to change a variable in all instances at the same time.

#### Example

all.x \= 200;

The fix for this issue is to use the keyword all in a with statement.

with (all)  

 {  

     x \= 200;  

 }

### GM2022 \- Return value of a pure function is not being used.

This message indicates that you've called a [pure](#) function, which doesn't change anything and only returns a value, without using its return value. The return value can be used by assigning it to a variable, using it in an expression or by passing it as a parameter in a function call.

#### Example

variable\_get\_hash("member");  

 choose("a", "b", "c");  

 make\_colour\_rgb(255, 255, 0\);

The return value needs be used in the code in order to fix the issue.

var \_hash \= variable\_get\_hash("member");  

 if (choose("a", "b", "c") \=\= "a") { show\_debug\_message("Good choice!"); }  

 draw\_set\_colour(make\_colour\_rgb(255, 255, 0\));

### GM2023 \- Evaluation order of function calls in argument list not guaranteed between platforms.

This message is shown when there are multiple function calls in the argument list when calling a function. When a function is called, the arguments are not necessarily initialised in the order they're defined in the argument list. As a consequence, when the arguments contain function calls, those function calls may not execute in the order you'd expect. In some specific cases, such as when a function reads data sequentially, this can give unexpected results.

#### Example

vertex\_position\_3d(vb, buffer\_read(buff, buffer\_f32\), buffer\_read(buff, buffer\_f32\), buffer\_read(buff, buffer\_f32\));  

 /// z will be x, y will be y, x will be z  

 /// since the buffer\_read's are called in order last to first

To make sure the assignments are done in the correct order you call the functions and assign the result of each of them to a temporary variable before calling the actual function. Then call the actual function and pass the temporary variables as the arguments.

var \_x \= buffer\_read(buff, buffer\_f32\);  

 var \_y \= buffer\_read(buff, buffer\_f32\);  

 var \_z \= buffer\_read(buff, buffer\_f32\);  

 vertex\_position\_3d(vb, \_x, \_y, \_z);

### GM2025 \- Reference to non\-existent event '{0}'.

Shown when a [user event](../../GameMaker_Language/GML_Reference/Asset_Management/Objects/Object_Events/event_user.md) is called but that user event does not exist in the object.

### GM2026 \- Not all code paths call draw\_set\_halign(fa\_left) before the end of the script.

This message indicates that you changed the horizontal text alignment to a value different from the default (fa\_left) but haven't changed it back afterwards.

#### Example

/// Draw GUI Begin Event  

 draw\_set\_halign(fa\_right);  

 draw\_text(room\_width\-5, 5, "In the top\-right corner");  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "In the top\-left corner");
 

In the example code above, the horizontal text alignment is set to right\-aligned and some text is drawn in the Draw GUI Begin event. However, the text alignment isn't reset to fa\_left, which causes text in the Draw GUI Event that follows it to be drawn mostly offscreen. This is because it is drawn right\-aligned at a position in the top\-left corner of the window. Resetting the horizontal text alignment back to fa\_left fixes the issue.

/// Draw GUI Begin Event  

 draw\_set\_halign(fa\_right);  

 draw\_text(room\_width\-5, 5, "In the top\-right corner");  

 draw\_set\_halign(fa\_left);  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "In the top\-left corner");
 

### GM2027 \- Opening another primitive before closing a previous primitive.

This message is shown when you open another primitive using [draw\_primitive\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_begin.md) without closing the current primitive with a call to [draw\_primitive\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_end.md).

A primitive is always drawn with a call to draw\_primitive\_begin(), followed by multiple calls to one of the draw\_vertex\* functions and finally a call to draw\_primitive\_end().

#### Example

/// Draw Event  

 draw\_primitive\_begin(pr\_linestrip);  

 draw\_vertex(0, 0\);  

 draw\_vertex(10, 0\);  

 draw\_vertex(0, 10\);  

 draw\_primitive\_begin(pr\_linestrip);  

 draw\_vertex(10, 0\);  

 draw\_vertex(20, 0\);  

 draw\_vertex(10, 10\);  

 draw\_primitive\_end();

The first primitive is missing a draw\_primitive\_end() call after the calls to draw\_vertex(). Adding it fixes the issue.

/// Draw Event  

 draw\_primitive\_begin(pr\_linestrip);  

 draw\_vertex(0, 0\);  

 draw\_vertex(10, 0\);  

 draw\_vertex(0, 10\);  

 draw\_primitive\_end();  

  

 draw\_primitive\_begin(pr\_linestrip);  

 draw\_vertex(10, 0\);  

 draw\_vertex(20, 0\);  

 draw\_vertex(10, 10\);  

 draw\_primitive\_end();
 

### GM2028 \- Closing a primitive without opening a primitive.

This message indicates that you made a call to [draw\_primitive\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_end.md) to close a primitive, but haven't opened a primitive first with a call to [draw\_primitive\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_begin.md).

#### Example

/// Draw Event  

 draw\_primitive\_end();  // Which primitive to close?

Calling draw\_primitive\_begin() before draw\_primitive\_end() fixes this issue.

/// Draw Event  

 draw\_primitive\_begin(pr\_linelist);  

  

 // draw\_vertex, draw\_vertex\_colour, etc.  

  

 draw\_primitive\_end();
 

### GM2029 \- The function '{0}' cannot be called outside of a draw\_primitive\_begin()/draw\_primitive\_end() block.

This message is shown when you use one of the draw\_vertex\* functions outside of  [draw\_primitive\_begin](../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_begin.md) / [draw\_primitive\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_end.md). These functions add vertices when drawing a primitive and only do something when called between draw\_primitive\_begin() and draw\_primitive\_end().

#### Example

/// Draw Event  

 draw\_vertex(room\_width/4, room\_height/4\);  

 draw\_vertex(room\_width/2, room\_height/4\);  

 draw\_vertex(room\_width/4, room\_height/2\);  

 draw\_primitive\_begin(pr\_trianglelist);  

 draw\_primitive\_end();

In the code example, the calls to draw\_vertex() need to be moved between the calls to draw\_primitive\_begin() and draw\_primitive\_end().

/// Draw Event  

 draw\_primitive\_begin(pr\_trianglelist);  

 draw\_vertex(room\_width/4, room\_height/4\);  

 draw\_vertex(room\_width/2, room\_height/4\);  

 draw\_vertex(room\_width/4, room\_height/2\);  

 draw\_primitive\_end();

### GM2030 \- Not all code paths call draw\_primitive\_end() before the end of the script.

This message indicates that a call to [draw\_primitive\_end](../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_end.md) is missing in at least one place in your code. This can happen when you draw, for example, different vertices based on an if\-else condition and you added the call to draw\_primitive\_end() to the if case, but not to the else case.

#### Example

/// Draw Event  

 var \_condition \= (irandom(100\) \< 50\);  

 draw\_primitive\_begin(pr\_linelist);  

  

 if (\_condition)  

 {  

     // draw\_vertex, draw\_vertex\_colour, etc.  

     draw\_primitive\_end();  

 }  

 else  

 {  

     // draw\_vertex, draw\_vertex\_colour, etc.  

 }
 

In the example above one of two possible code paths is followed, where each draws a different shape. The if case ends with a call to draw\_primitive\_end(), though the else case is missing that call. Adding it to the else case is one possible fix, though the clean and more robust way to fix the issue is to move it outside of the if\-else statement.

/// Draw Event  

 var \_condition \= (irandom(100\) \< 50\);  

 draw\_primitive\_begin(pr\_linelist);  

  

 if (\_condition)  

 {  

     // draw\_vertex, draw\_vertex\_colour, etc.  

 }  

 else  

 {  

     // draw\_vertex, draw\_vertex\_colour, etc.  

 }  

  

 draw\_primitive\_end();  // Call no longer depends on if\-else condition!
 

### GM2031 \- Opening another File Find before closing a previous File Find.

This message is shown when you start another File Find with [file\_find\_first](../../GameMaker_Language/GML_Reference/File_Handling/File_System/file_find_first.md) without closing the previous one with [file\_find\_close](../../GameMaker_Language/GML_Reference/File_Handling/File_System/file_find_close.md). You can only perform one File Find at a time and one needs to be closed before another can be opened.

#### Example

var \_look\_for\_description \= true;  

 var \_file \= file\_find\_first("/game\_data/\*.bin", fa\_none);  

 if (\_look\_for\_description)  

 {  

     \_file2 \= file\_find\_first("/game\_data/\*.json", fa\_none);  

 }  

  

 file\_find\_close();
 

In the code example above a second file find is started with file\_find\_first() before the current file find is properly closed if a variable \_look\_for\_description is set to true. To properly fix the issue the first file find needs to be closed before the if statement is checked and the second file find needs to be closed inside the true case of the if statement (at the same level as the call to file\_find\_first()).

var \_look\_for\_description \= true;  

 var \_file \= file\_find\_first("/game\_data/\*.bin", fa\_none);  

 file\_find\_close();  

 if (\_look\_for\_description)  

 {  

     \_file2 \= file\_find\_first("/game\_data/\*.json", fa\_none);  

     file\_find\_close();  

 }

### GM2032 \- Closing a File Find without opening a File Find.

This message is shown when you call [file\_find\_close](../../GameMaker_Language/GML_Reference/File_Handling/File_System/file_find_close.md) when no File Find is currently open (i.e. no call to [file\_find\_first](../../GameMaker_Language/GML_Reference/File_Handling/File_System/file_find_first.md) was made).

#### Example

file\_find\_close();

A call to file\_find\_first() should be added if the intention is to do a File Find.

file\_find\_first("\*.json", fa\_none);  

 file\_find\_close();

### GM2033 \- The function '{0}' cannot be called outside of a file\_find\_first()/file\_find\_close() block.

This message indicates that the given function can only go between a call to [file\_find\_first](../../GameMaker_Language/GML_Reference/File_Handling/File_System/file_find_first.md) and a call to [file\_find\_close](../../GameMaker_Language/GML_Reference/File_Handling/File_System/file_find_close.md).

#### Example

fnames \= \[];  

 var \_fname \= file\_find\_first("\*.txt", fa\_none);  

  

 while(\_fname !\= "")  

 {  

     array\_push(fnames, \_fname);  

     \_fname \= file\_find\_next();  

 }  

  

 file\_find\_close();  

 file\_find\_next();
 

The second file\_find\_next() is called outside of the calls to file\_find\_first() and file\_find\_close(). It needs to be removed to fix the issue.

fnames \= \[];  

 var \_fname \= file\_find\_first("\*.txt", fa\_none);  

  

 while(\_fname !\= "")  

 {  

     array\_push(fnames, \_fname);  

     \_fname \= file\_find\_next();  

 }  

  

 file\_find\_close();
 

### GM2034 \- Not all code paths call file\_find\_close() before the end of the script.

This message indicates that a call to [file\_find\_close](../../GameMaker_Language/GML_Reference/File_Handling/File_System/file_find_close.md) may not be encountered. Ideally, the call to file\_find\_close() should occur in the same scope as the call to file\_find\_first().

#### Example

fnames \= \[];  

 var \_fname \= file\_find\_first("\*.txt", fa\_none);  

 while(\_fname !\= "")  

 {  

     array\_push(fnames, \_fname);  

     \_fname \= file\_find\_next();  

 }

In the code example, a call to file\_find\_close() is missing. This needs to be added to fix the issue.

fnames \= \[];  

 var \_fname \= file\_find\_first("\*.txt", fa\_none);  

 while(\_fname !\= "")  

 {  

     array\_push(fnames, \_fname);  

     \_fname \= file\_find\_next();  

 }  

 file\_find\_close();

### GM2035 \- Not all code paths call gpu\_pop\_state() before end of script.

This message indicates that there are situations where [gpu\_pop\_state](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_pop_state.md) isn't called, depending on your game's logic. This can occur when you have logic in your code where, for example, the if case contains a call to gpu\_pop\_state but the else case doesn't. Depending on whether the expression inside the if statement evaluates to true or false the function may not get called.

#### Example

/// Draw End Event  

 gpu\_push\_state();  

 gpu\_set\_blendmode(bm\_add);  

 if (show\_name)  

 {  

     draw\_text(x, y, name);  

     gpu\_pop\_state();  

 }  

 /// Draw GUI Event  

 draw\_text(5, 5, $"Instances: {instance\_count}");

In the code example, the GPU's current state is pushed onto the stack and the blend mode is then changed to bm\_add. The GPU's state is then set back to the previous one, but only if an instance variable is true. This has consequences for the subsequent Draw GUI Event. The call to gpu\_pop\_state needs to be moved out of the if statement so it always executes.

/// Draw End Event  

 gpu\_push\_state();  

 gpu\_set\_blendmode(bm\_add);  

 if (show\_name)  

 {  

     draw\_text(x, y, name);  

 }  

 gpu\_pop\_state();  

  

 /// Draw GUI Event  

 draw\_text(5, 5, $"Instances: {instance\_count}");  // All good!
 

### GM2039 \- Call to execute a global script resource like a function is deprecated.

This message is shown when you call a script asset as a function. A script asset is not meant to be executed directly as a function. While the behaviour is still included in GameMaker, it is only there to support legacy code.

#### Example

/// my\_function  

 show\_debug\_message("my\_function calling!");  // Function call. Debug message is shown already!  

  

 /// Create Event  

 my\_function();                               // Debug message is shown again!
 

If a script asset contains code that should be its own function, this code should be moved inside a new function definition inside the script. The new function gets the name of the script asset and the script asset can be renamed to a descriptive name that describes well what it contains (a group of functions, a collection of (global) variables, a collection of macros, etc.).

/// Functions (Script Asset)  

 function my\_function()  

 {  

     show\_debug\_message("my\_function calling!");  // Function call as part of function definition. Nothing is shown (yet)!  

 }  

  

 /// Create Event  

 my\_function();                                   // Actual function call, debug message is shown (only) at the intented time!
 

### GM2040 \- Call to event\_inherited() in object with no parent event.

This message is shown when you call the function [event\_inherited](../../GameMaker_Language/GML_Reference/Asset_Management/Objects/Object_Events/event_inherited.md) in an object that either has no parent object or that has no ancestor in its parent\-child hierarchy that defines the event.

#### Example

/// obj\_parent  

 // No Room Start event  

  

 /// obj\_child.Room\_Start  

 event\_inherited();
 

In the code example, an object obj\_child has an object obj\_parent as its parent object. The parent object doesn't define a Room Start event yet the child object does and calls event\_inherited(). The call to event\_inherited() can be removed, or it can be commented out in case the event might get added later in the parent object.

/// obj\_parent  

 // No Room Start event  

  

 /// obj\_child.Room\_Start  

 event\_inherited();
 

### GM2042 \- Inconsistent stack depth for gpu\_push\_state()/gpu\_pop\_state() blocks. All branches should call these functions an equal number of times.

This message indicates that [gpu\_push\_state](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_push_state.md) is called a different number of times than [gpu\_pop\_state](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_pop_state.md). Every call to gpu\_push\_state must be accompanied by a call to gpu\_pop\_state.

#### Example

/// Draw Event  

 // Situation 1  

 gpu\_push\_state();  

 gpu\_push\_state();  

 // draw something  

 gpu\_pop\_state();  

  

 // Situation 2  

 gpu\_push\_state();  

 // draw\_something  

 gpu\_pop\_state();  

 gpu\_pop\_state();
 

Every call to gpu\_push\_state in the code above must have a corresponding call to gpu\_pop\_state. Assuming that two stack pushes were meant in the first case and a single stack push in the second case, the code can be fixed as follows:

/// Draw Event  

 // Situation 1  

 gpu\_push\_state();  

 gpu\_push\_state();  

 // draw something  

 gpu\_pop\_state();  

 gpu\_pop\_state();  

  

 // Situation 2  

 gpu\_push\_state();  

 // draw\_something  

 gpu\_pop\_state();
 

### GM2043 \- Attempting to access the local variable '{0}' outside of the scope it was defined in.

This warning is shown when you access a local variable either before it's defined or after it's gone out of scope.

#### Example

// Attempt to access before it's defined  

 // Didn't come across variable definition yet  

 i \= 0;  

 var i \= 34;  

  

 // Attempting to access after the variable's gone out of scope  

 if (something\_occurred)  

 {  

     // Variable is defined inside curly braces,  

     // remains "in scope" between these curly braces  

     var \_msg \= "Something happened!";  

 }  

  

 // Variable went out of scope after the closing curly brace  

 \_msg \= "test";
 

You should make sure to always define local variables before accessing them. In case of the if statement the variable can simply be declared before the if so it stays in scope the entire time and can also be accessed from within the if statement.

// Fix for access before it's defined  

 var i \= 0;  

 i \= 34;  

  

 // Fix for access after the variable's gone out of scope  

 var \_msg;  

 if (something\_occurred)  

 {  

     // Variable can be accessed and modified from within if  

     \_msg \= "Something happened!";  

 }  

  

 // Variable is still in scope now  

 \_msg \= "test";
 

### GM2044 \- Local variable '{0}' is already declared.

This message is shown when you declare a local variable with the same name as a local variable that already exists.

#### Example

// Situation 1: declared again  

 var i \= 0;  

 var \_num\_elements \= 20;  

 array \= array\_create(\_num\_elements);  

 repeat(\_num\_elements)  

 {  

     array\[i\-\-] \= irandom(100\);  

 }  

 var i \= 0;  

  

 // Situation 2: redeclared in a nested loop  

 for(var i \= 0;i \< 50;i\+\+)  

 {  

     for(var i \= 0;i \< 50;i\+\+)  

     {  

           

     }  

 }
 

In the above example two situations are shown. In the first situation the local variable is declared and used in a repeat loop. After that, it is redeclared. In this case, it suffices to keep only the first declaration and change the other one to an assignment since the variable already exists at that point. In the second situation the same variable name is accidentally used for both loop counters in a nested for loop. This will cause the variable to increment not only in the outer loop but also in the inner loop. To fix this, the inner loop counter variable should be renamed.

// Situation 1: declared again  

 var i \= 0;  

 var \_num\_elements \= 20;  

 array \= array\_create(\_num\_elements);  

 repeat(\_num\_elements)  

 {  

     array\[i\-\-] \= irandom(100\);  

 }  

 i \= 0;  

  

 // Situation 2: redeclared in a nested loop  

 for(var i \= 0;i \< 50;i\+\+)  

 {  

     for(var j \= 0;j \< 50;j\+\+)  

     {  

           

     }  

 }
 

### GM2046 \- Inconsistent stack depth for surface\_set\_target()/surface\_reset\_target() blocks. All branches should call these functions the same number of times.

This message indicates that you've set the draw target to a surface more times than you've reset it back to the previous target. Every change to the draw target must be accompanied by a change back to the previous draw target. If you miss a call to [surface\_reset\_target](../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_reset_target.md) this may cause certain things to be drawn to a different surface.

#### Example

/// Create Event  

 sf \= \-1;  

  

 /// Draw Event  

 if (!surface\_exists(sf))  

 {  

     sf \= surface\_create(128, 128\);  

 }  

 surface\_set\_target(sf);  

 draw\_clear\_alpha(c\_blue, 1\);  

 draw\_circle(50, 50, 20, false);  

 vertex\_submit(vb, pr\_trianglelist, surface\_get\_texture(sf));
 

In the code example above, a surface is created and drawn to in the Draw event. The surface is set as the drawing target but the drawing target isn't reset properly. A vertex buffer is then submitted with the surface texture used as the texture. However, the drawing target is still set to the surface itself and the vertex buffer will be rendered to the surface.

Adding a call to surface\_reset\_target() after drawing to the surface fixes the issue.

/// Create Event  

 sf \= \-1;  

  

 /// Draw Event  

 if (!surface\_exists(sf))  

 {  

     sf \= surface\_create(128, 128\);  

 }  

 surface\_set\_target(sf);  

 draw\_clear\_alpha(c\_blue, 1\);  

 draw\_circle(50, 50, 20, false);  

 surface\_reset\_target();  

 vertex\_submit(vb, pr\_trianglelist, surface\_get\_texture(sf));
 

### GM2047 \- Unreachable code.

This message is shown when a part of your code cannot be reached in any way because the logic always prevents it from happening. For example, when the expression inside an if statement always evaluates to false, the code inside that if statement will never be executed.

#### Example

if (false)  

 {  

     // Unreachable code  

 }

To fix this you should change the expression so that there are cases where it can evaluate to true and the code inside the if case executes.

if (choose(true, false))  

 {  

     // Code executed if 'true'  

 }

### GM2048 \- Not all code paths call gpu\_set\_blendenable(true) before the end of the script.

This message indicates that gpu\_set\_blendenable(true) isn't called in all possible cases after you disable blending with gpu\_set\_blendenable(false). This can occur when you have logic in your code where, for example, the if case contains a call to gpu\_set\_blendenable(true) but the else case doesn't. Depending on whether the expression inside the if statement evaluates to true or false, the function may not get called and blending won't be enabled again for subsequent drawing.

#### Example

/// Draw Event  

 gpu\_set\_blendenable(false);  

 vertex\_submit(vb, pr\_trianglelist, tex);  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "Hello!");  // Text isn't drawn correctly
 

To fix this issue you need to re\-enable alpha blending with another call to [gpu\_set\_blendenable](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_blendenable.md).

/// Draw Event  

 gpu\_set\_blendenable(false);  

 vertex\_submit(vb, pr\_trianglelist, tex);  

 gpu\_set\_blendenable(true);  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "Hello!");  // Text is drawn correctly again
 

### GM2049 \- Not all code paths call gpu\_set\_zfunc(cmpfunc\_lessequal) before the end of the script.

This message indicates that you've changed the function for z\-testing but haven't set it back to the default cmpfunc\_lessequal again. When depth testing is enabled with a call to gpu\_set\_ztestenable(true), by default a pixel that's written to the depth buffer is considered closer when its z value is less or equal (cmpfunc\_lessequal) than the current depth value for that pixel.

#### Example

/// Draw Event  

 gpu\_set\_ztestenable(true);  

 gpu\_set\_zfunc(cmpfunc\_greater);  

 vertex\_submit(vb, pr\_trianglelist, tex);  

 gpu\_set\_ztestenable(false);

The comparison function used for z\-testing needs to be properly reset to cmpfunc\_lessequal in another call to [gpu\_set\_zfunc](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_zfunc.md).

/// Draw Event  

 gpu\_set\_ztestenable(true);  

 gpu\_set\_zfunc(cmpfunc\_greater);  

 vertex\_submit(vb, pr\_trianglelist, tex);  

 gpu\_set\_zfunc(cmpfunc\_lessequal);  

 gpu\_set\_ztestenable(false);

### GM2050 \- Not all code paths call gpu\_set\_fog(false, c\_black, 0, 1\) before the end of the script.

This message indicates that you've changed the GPU fog settings with a call to [gpu\_set\_fog](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_fog.md), but haven't reset them to the default fog settings afterwards. GPU fog is disabled by default.

#### Example

/// Draw Event  

 gpu\_set\_fog(true, c\_aqua, 0, 1000\);  

 draw\_self();

The fog needs to be disabled after drawing with fog enabled in order not to affect subsequent draw commands.

/// Draw Event  

 gpu\_set\_fog(true, c\_aqua, 0, 1000\);  

 draw\_self();  

 gpu\_set\_fog(false, c\_black, 0, 1\);

### GM2051 \- Not all code paths call gpu\_set\_cullmode(cull\_noculling) before the end of the script.

This message indicates that you've changed the cullmode using a call to [gpu\_set\_cullmode](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_cullmode.md), but haven't reset it to cull\_noculling afterwards. When culling is enabled, the GPU will not draw the backside of triangles based on the winding order of the vertices, which is either clockwise or counter\-clockwise.

#### Example

/// Draw Event  

 gpu\_set\_cullmode(cull\_clockwise);  

 shader\_set(sh\_lighting);  

 vertex\_submit(vb\_static\_geometry, pr\_trianglelist, \-1\);  

 shader\_reset();  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "World 1");
 

In order to fix this issue the cullmode needs to be properly reset to cull\_noculling or to the value that it had before.

/// Draw Event  

 gpu\_set\_cullmode(cull\_clockwise);  

 // OR  

 // var \_cm \= gpu\_get\_cullmode();  

 // gpu\_set\_cullmode(cull\_clockwise);  

  

 shader\_set(sh\_lighting);  

 vertex\_submit(vb\_static\_geometry, pr\_trianglelist, \-1\);  

 shader\_reset();  

  

 gpu\_set\_cullmode(cull\_noculling);  

 // OR  

 // gpu\_set\_cullmode(\_cm);  

  

 /// Draw GUI Event  

 draw\_text(5, 5, "World 1");
 

### GM2052 \- Not all code paths call gpu\_set\_colourwriteenable(true, true, true, true) before the end of the script.

This message indicates that you've disabled writing to at least one colour channel but haven't re\-enabled writing to all colour channels afterwards.

#### Example

/// Draw Event  

 gpu\_set\_colourwriteenable(true, true, true, false);  

 draw\_sprite(sprite\_index, 0, x, y);

In the code example above writing to the alpha channel is disabled for all draw calls that follow the call to [gpu\_set\_colourwriteenable](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_colourwriteenable.md). No call to gpu\_set\_colourwriteenable() is made to reset this, however. Because of this, subsequent draw commands will also not write to the alpha channel. Another call to gpu\_set\_colourwriteenable() is needed to fix this, which restores writing to all colour channels.

/// Draw Event  

 gpu\_set\_colourwriteenable(true, true, true, false);  

 draw\_sprite(sprite\_index, 0, x, y);  

 gpu\_set\_colourwriteenable(true, true, true, true);

### GM2053 \- Not all code paths call gpu\_set\_alphatestenable(false) before the end of the script.

This message indicates that you've enabled alpha testing but haven't disabled it again afterwards.

#### Example

/// Draw Event  

 gpu\_set\_alphatestenable(true);  

 draw\_self();

To fix this you should disable alpha testing after drawing everything that needs to be drawn with alpha testing enabled.

/// Draw Event  

 gpu\_set\_alphatestenable(true);  

 draw\_self();  

 gpu\_set\_alphatestenable(false);

### GM2054 \- Not all code paths call gpu\_set\_alphatestref(0\) before the end of the script.

This message indicates that you've changed the alpha test ref value from the default value of 0 (using [gpu\_set\_alphatestref](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_alphatestref.md)) but haven't changed it back to 0 afterwards.

Note that the alpha test ref value is only used when alpha testing is enabled using [gpu\_set\_alphatestenable](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_alphatestenable.md).

#### Example

/// Draw Event  

 gpu\_set\_alphatestenable(true);  

 gpu\_set\_alphatestref(127\);  

 draw\_sprite(sprite\_index, 0, x, y);

The alpha test ref value should be reset back to 0 to prevent subsequent draw commands from being affected.

/// Draw Event  

 gpu\_set\_alphatestenable(true);  

 gpu\_set\_alphatestref(127\);  

 draw\_sprite(sprite\_index, 0, x, y);  

 gpu\_set\_alphatestref(0\);  

 gpu\_set\_alphatestenable(false);

### GM2055 \- Not all code paths call gpu\_set\_texfilter(false) before the end of the script.

This message indicates that you've changed the texture filter setting to true but haven't changed it back to false afterwards. By default, texture filtering is set to disabled for all texture samplers.

#### Example

/// Create Event  

 tex \= sprite\_get\_texture(spr\_texpage, 0\);  

  

 /// Draw Event  

 gpu\_set\_texfilter(true);  

 vertex\_submit(vb\_world, pr\_trianglelist, tex);
 

After the call to [gpu\_set\_texfilter](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_texfilter.md) and all draw commands that follow it you need to reset texture filtering to false, the default setting.

/// Create Event  

 tex \= sprite\_get\_texture(spr\_texpage, 0\);  

  

 /// Draw Event  

 gpu\_set\_texfilter(true);  

 vertex\_submit(vb\_world, pr\_trianglelist, tex);  

 gpu\_set\_texfilter(false);
 

### GM2056 \- Not all code paths call gpu\_set\_texrepeat(false) before the end of the script.

This message indicates that you've changed the texture repeat setting to true but haven't changed it back to false afterwards. By default, texture repeating is set to disabled for all texture samplers.

#### Example

/// Create Event  

 tex \= sprite\_get\_texture(spr\_texpage, 0\);  

  

 /// Draw Event  

 gpu\_set\_texrepeat(true);  

 vertex\_submit(vb\_world, pr\_trianglelist, tex);
 

After the call to [gpu\_set\_texrepeat](../../GameMaker_Language/GML_Reference/Drawing/GPU_Control/gpu_set_texrepeat.md) and all draw commands that follow it you should reset the texture repeat to false, the default setting.

/// Create Event  

 tex \= sprite\_get\_texture(spr\_texpage, 0\);  

  

 /// Draw Event  

 gpu\_set\_texrepeat(true);  

 vertex\_submit(vb\_world, pr\_trianglelist, tex);  

 gpu\_set\_texrepeat(false);
 

### GM2061 \- Opportunity to use nullish coalesce operator.

Shows when you are trying to check if an expression is undefined, and then applying a different value in that case:

#### Example

array \= modify\_array(array);  

 if (array \=\= undefined) array \= \[];

For this, the [nullish operator](../../GameMaker_Language/GML_Overview/Expressions_And_Operators.md) can be used:

array \= modify\_array(array) ?? \[];

To keep a variable unchanged if the RHS expression is undefined, use this:

array ??\= modify\_array(array);

### GM2062 \- Not all code paths call draw\_set\_colour(c\_white) before the end of the script.

This message indicates that you've changed the draw colour to a colour that's different from c\_white but haven't changed it back to c\_white afterwards.

The draw colour is the colour that's used to blend the sprite with. A colour of c\_white essentially multiplies all of the sprite's pixels' colours by 1, resulting in no change.

#### Example

/// Draw Event  

 draw\_set\_colour(c\_red);  

 draw\_text(5, 5, "Hello!");

In the code example above, the draw colour used for drawing is set to c\_red but isn't set back to c\_white afterwards. This causes all subsequent draw commands to draw with that same draw colour.

/// Draw Event  

 draw\_set\_colour(c\_red);  

 draw\_text(5, 5, "Hello!");  

 draw\_set\_colour(c\_white);

### GM2063 \- Not all code paths call draw\_set\_alpha(1\) before the end of the script.

This message indicates that you've changed the draw alpha to a value different from 1 using [draw\_set\_alpha](../../GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/draw_set_alpha.md) but haven't changed it back to 1\.

The alpha value is the value that's used for blending each pixel of the sprite (the source) with the destination pixel.

#### Example

/// Draw Event  

 draw\_set\_alpha(0\.5\);  

 draw\_self();

In the code example above, the alpha value used for drawing is set to 0\.5 but isn't set back to 1 afterwards. This causes all subsequent draw commands to draw with that same alpha value.

/// Draw Event  

 draw\_set\_alpha(0\.5\);  

 draw\_self();  

 draw\_set\_alpha(1\);

### GM2064 \- Variable '{0}' does not exist in object's Variable Definitions.

This message is shown when you create a new instance of an object using one of the instance\_create\_\* functions and attempt to access variables that aren't defined in the object's [Variable Definitions](../Object_Properties/Object_Variables.md "Object Variables") when assigning to the optional variable struct.

In the variable struct you can access variables from any scope, though in instance scope the only variables that exist at this point are the ones defined in the Variable Definitions.

Important: object variables don't belong to the object but are initialised in every new instance created from that object. The first point in your code where you can access these variables is the var struct.

#### Example

/// Create Event  

 ins\_companion \= instance\_create\_layer(x, y, layer, obj\_companion, {  

     intro\_message: message  

 });  

  

 // The message variable does not exist
 

Variables can only be accessed when they've first been defined. In the example above, the object doesn't have any variables defined but an attempt is made to access an instance variable named message. In order to fix this, the variable has to be defined in the object variables.

/// Create Event  

 ins\_companion \= instance\_create\_layer(x, y, layer, obj\_companion, {  

     intro\_message: message  

 });
