# Expressions And Operators

## Expressions

An expression is a mathematical phrase that can contain ordinary numbers, variables, strings, or functions as well as one or more **operators** (like add, subtract, multiply, etc.). The values used in an expression can be real numbers (e.g. 3\.4 \* 6), hexadecimal numbers starting with a $ sign (e.g. $00FFAA \| $88FFAA), strings between double quotes (e.g. "hello" \+ "world") or more complicated expressions using multiple operators and values.

## Operators

The following operators are provided for use with expressions:

[Assigning (\=)](#)

\= is used to assign a value to a variable. Note that this can *also* be used for comparing variables in GameMaker and you may see this in examples and other peoples codes. However, this is a legacy from old GameMaker versions and you should use the \=\= operators for comparing and \= for assigning, as shown in these examples:

a \= 12;  

 speed \= 5;  

 val \= (old\_val \+ 5\);

 

[Combining (\&\&, \|\|, ^^)](#)

**\&\&, \|\|, ^^ (and, or and xor)** are used to combine boolean values to give either true or false. If any of the following examples resolves to true then the code would be run:

if (a \=\= b \&\& c \=\= d) { do something... }  // and  

 if (a \=\= b \|\| c \=\= d) { do something... }  // or  

 if (a \=\= b ^^ c \=\= d) { do something... }  // xor

 

[Nullish (??, ??\=)](#)

  "Nullish" simply refers to a value being equal to undefined or pointer\_null.

?? is a nullish coalescing operator that returns a specified expression if the given value is undefined or pointer\_null. This operator expects the following syntax:

(input ?? null\_output)

If input is undefined or pointer\_null, the expression will return the null\_output value; however in all other cases it will simply return the input value. This can be used to define a "default" value for a variable in case the variable itself does not hold a valid value.

Consider the following example:

username \= data.username ?? "INVALID USERNAME";

Here, the username variable will get the value stored in data.username, however if data.username happens to be undefined or pointer\_null, the variable will get the string "INVALID USERNAME" instead. This example ensures that any function calls using the username variable do not cause an error because of being given a nullish value, and that the user knows when their username was not returned.

  The expression on the right hand side of the nullish coalescing operator is only executed when the input value is nullish, meaning that any function calls included in the RHS expression will only be executed if the input value is nullish.

---

??\= is similar to the nullish coalescing operator described above but is used specifically for variable assignments. This operator expects the following syntax:

variable ??\= null\_value

If variable is undefined or pointer\_null, the null\_value value will be assigned to it, otherwise the variable will remain unchanged. This can be used to assign a custom "default" value to a variable when it holds a nullish value.

 

[Comparing (\, \>\=)](#)

**\, \>\=** are comparisons and can only give a true or false result (where true can also be interpreted as 1, and false as 0\). Examples of use:

if (a \< b) {do something...}  

 if (a !\= b) {do something...}

[Bitwise (\|, \|\=, \&, \&\=, ^, ^\=, \\>)](#)

**\|, \&, ^, \\>** are used to perform bitwise operations, where \| \= bitwise or, \& \= bitwise and, ^ \= bitwise xor, \\> \= shift right. Examples of use:

x \= (x \& $ffffffe0\) \+ 32;  

 if (y ^ $1f) \> 0 {do something...};

 The \|, \& and ^ operators have shortened versions, \|\=, \&\= and ^\= respectively, that first perform the operation and then assign the result to the left operand. For example:

a \= 0b1111;  

 b \= 0b1001;  

 c \= a;  

 c \&\= b;  // c equals 9 after this statement, or 0b1001  

 a ^\= c;  // a equals 6 after this statement, or 0b0110

  See [Bitwise Operators](../../Additional_Information/Bitwise_Operators.md) for additional information on what they do and on how to use them.

 

[Arithmetical (\+, \+\=, \-, \-\=, \*, \*\=, /, /\=)](#)

**\+, \-, \*, /** are add, subtract, multiply and divide, respectively. Examples of use:

c \= a \* b;

The four arithmetical operators have shortened versions, namely \+\=, \-\=, \*\= and /\=. These perform the operation and then assign the result to the left operand. For example:

a \= 1;  

 a \+\= 1;  

 a \*\= 3;  

 a \-\= 2;  

 a /\= 2;

  Floating point numbers do not stop on Divide by Zero as they will get an infinity as the answer. If A and B are integers (either int32 or int64\) then the division will be done as integers (and divide by 0 will be checked and error'd). Otherwise it will be done as a floating point division (with no divide by 0 check).

 

[String Concatenation (\+, \+\=)](#)

When used on strings \+ performs string concatenation, i.e. it adds two strings together. For example:

message \= "Hello " \+ "World";

This operator also has a shortened version \+\=, which combines the concatenation with an assignment to the left operand. For example:

message \+\= "!";

Note that for string concatenation to work both operands need to be of type [String](Data_Types.md). The following code, for example, will raise an error:

description \= "Count to " \+ 10;

The operand on the right is not a [String](Data_Types.md) and needs to be *explicitly* converted, for example using the [string](../GML_Reference/Strings/string.md) function:

description \= "Count to " \+ string(10\);

Alternatively you can use the [string\_concat](../GML_Reference/Strings/string_concat.md) function or a [template string](../GML_Reference/Strings/Strings.md#h4 "Template Strings") to implicitly convert values to string.

See the [string](../GML_Reference/Strings/string.md) page for detailed conversion rules.

 

[Increment/Decrement (\+\+, \-\-)](#)

**\+\+**, **\-\-** are used to add or subtract one (1) from a value. It is worth noting that placing this before or after the value to be added to or subtracted from will have slightly different results. For example:

- \+\+a will increment the variable and return the incremented value.
- a\+\+ will increment the variable but return the value before it was incremented.

Therefore, if you have something like this:

var a \= 1;  

 show\_debug\_message(string(a\+\+));  

 show\_debug\_message(string(\+\+a));

The debug output would be 1 and 3\. Here are some examples of use:

for (var i \= 0; i \< 10; i\+\+)  

 {  

     do something...  

 }

if (hit \=\= true)  

 {  

     \-\-score;  

 }

  On the YoYo Compiler target platforms (those marked (YYC)), these expressions are evaluated from left to right, while on all other target platforms they are evaluated from right to left, meaning that this:

val \= max(num, \+\+num, num\+\+);

will give different results depending on the platform.

 

[Division and Modulo (div, %, %\=, mod)](#)

**div** and **mod** (or %) are division and modulo, where div gives you the amount a value can be divided into producing only an integer quotient, while mod (or %) gives you only the remainder of a division. Note that the div operator first converts its operands into integers, then performs integer division. Examples of use:

secs \= time mod 60;  

 secs \= time % 60;    // Identical to the above line  

 time\_str \= string(time div 60\);

  The right operand of the div operator must be greater than or equal to 1, otherwise a divide by zero error is thrown.

The % operator has a shorthand version %\= that calculates the remainder of a division and assigns it to the left operand:

number \= 66;  

 number %\= 8;  // Identical to number \= number % 8;

[Unary (!, \-, \~)](#)

The following **unary** operators are provided:

- **!**: boolean "not", so !true \=\= false
- **\-**: negates the next real or integer value (not valid for strings or booleans)
- **\~**: negates the next value bitwise

 

[Conditional (?:)](#)

The conditional operator is the only ternary operator in GameMaker.

 
 

## Expression Grouping

As values in all expressions you can use numbers, variables, or functions that return a value, and sub\-expressions can be placed between brackets too. All operators work for real number values, but *comparisons* also work for strings and the \+ operator can be used to concatenate strings.

When doing multiple operations in a single expression, it is **very important** that you use brackets () to separate out the order of operation, as different platforms may perform them differently if not explicitly stated in this way. For example, consider the following code:

a \= b \=\= c \|\| d;

The different target compilers will perform the operations in different orders since they are not explicitly shown, giving rise to "odd" results that you may not expect when you play your game. to avoid this, use the () to separate out the parts, like this:

a \= (b \=\= c \|\| d);   //better  

 a \= ((b \=\= c) \|\| d); //best

## Statement Grouping

When using various operations and expressions in a single code block, these too should be separated. For example, the following *looks* like valid code:

if my\_var \=\= your\_var \+\+their\_var;

However, the compiler could interpret this in one of two ways:

if my\_var \=\= your\_var**\+\+** then their\_var;  

  

 // or  

  

 if my\_var \=\= your\_var then **\+\+**their\_var;
 

Now, you can tell looking at the code that one of those is a bit stupid, but that's because we know what we are wanting to achieve and what we want to happen, but the compiler doesn't. All it sees is two variables with the \+\+ operator between them so it has to choose which one to apply it to. Therefore, you should **always explicitly bracket expressions, operations and statements**. The correct version of the above code should be:

if (my\_var \=\= your\_var)  

 {  

     \+\+their\_var;  

 }

This may appear more verbose, but there is no ambiguity about the operations being performed and it will compile and behave consistently across all platforms. Also note that while you can chain expressions and statements without the use of brackets at the moment, this is a legacy feature and going forward may be deprecated and removed from GML, so using brackets appropriately now will "future\-proof" your code (and is generally good practice anyway).

Here are some final examples of the various different expressions:

{  

     x \= 23 div 2;  

     colour \= $FFAA00 \+ $00BB12;  

     str \= "hello" \+ "world";  

     y \+\= 5;  

     x \*\= y;  

     x \= y \<\< 2;  

     x \= 23 \* ((2 \+ 4\) / sin(y));  

     b \= (x \< 5\) \&\& !((x \=\= 2\) \|\| (x \=\= 4\));  

 }

One final thing to note is that there are also some expression "shortcuts" called **accessors** for use with certain [Data Structures](../GML_Reference/Data_Structures/Data_Structures.md) and [Arrays](Arrays.md). These enable you to add, or replace data within these formats quickly and easily and without the use of any function calls. For full details, please see the following page:

- [Accessors](Accessors.md)
