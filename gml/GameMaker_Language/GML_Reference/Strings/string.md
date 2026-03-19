# string

This function creates a new string from a variety of data types.

When only one argument is provided to the function, this argument is considered to be a value, which will be converted to a string from its original [data type](../../GML_Overview/Data_Types.md). When more than one argument is given, the first argument is considered a [Format String](string.md#h) and the arguments that follow it are considered the values to insert into the format string.

## Conversion From Non\-String Types

 
## Format String

When you pass more than one argument to the string function, the first argument will be treated as a *format string*. In a format string you can use *placeholders* of the form "{0}", "{1}", "{2}", etc.

These placeholders will be replaced with the arguments at the positions they refer to, i.e. "{0}" will be replaced with the second argument, "{1}" will be replaced with the third argument, "{2}" will be replaced with the fourth argument, and so on.

string\_variable \= string("This is a string with two placeholders that will be replaced. They are {0} and {1}.", "this", "that");  

  

 // Results in:  

 // "This is a string with two placeholders that will be replaced. They are this and that."
 

Any curly braces { } with text written between them that doesn't refer to a valid argument index won't represent a placeholder and are preserved, for example string("{Not} {1} has been replaced.", "") becomes "{Not} {1} has been replaced.".

You can escape curly braces to use them as normal characters in a format string by doubling them: {{ }}.

If you only pass a single argument to the function, then this argument will not be considered a format string. If you add placeholders of the kind "{0}" in this case, then they will be output as normal text as there are no values to replace them with: 

string\_variable \= string("This is a string with two placeholders that won't be replaced. They are {0} and {1}.");  

  

 // Results in:  

 // "This is a string with two placeholders that won't be replaced. They are {0} and {1}."
 

 
 

#### Syntax:

string(value\_or\_format \[, value1, value2, ...])

| Argument | Type | Description |
| --- | --- | --- |
| value\_or\_format | [Any](../../GML_Overview/Data_Types.md#variable) (if value) or [String](../../GML_Overview/Data_Types.md) (if format) | The value to be turned into a string. |
| \[, value1, value2, ...] | [Any](../../GML_Overview/Data_Types.md#variable) | The values to be inserted at the placeholder positions. |

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example 1:

draw\_text(100, 100, "Score: " \+ string(score) \+ " / Health: " \+ string(health));

The above code uses the string function to draw both real numbers and strings together, as [draw\_text()](../Drawing/Text/draw_text.md) will only accept *either* a string *or* a real, but not both, so we convert the non\-strings into strings.

 

#### Example 2:

draw\_text(100, 100, string("Score: {0} / Health: {1}", score, health));

In this code the string function is used in a slightly different way to achieve the same result as in Example 1\. Here the function is called with a format string as the first argument, in which "{0}" is replaced with the value of [score](../../GML_Overview/Variables/Builtin_Global_Variables/score.md) and "{1}" is replaced with the value of [health](../../GML_Overview/Variables/Builtin_Global_Variables/health.md).
