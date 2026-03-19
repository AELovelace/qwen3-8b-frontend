# title

This action can convert a string into a number. You provide the string to change and then give a target variable to return the real number back to (this variable can be flagged as a temporary local variable). Note that if the string has any characters
 other than numbers and a decimal point, it will *not* be converted, although if the string *starts* with a number then those will be converted and the rest of the string excluded. It is important to note that when passing decimals into this
 action, the returned string will be rounded to *two* decimal places only. Below is a table of input values and what you'd expect returned

| String | Returned Value |
| --- | --- |
| "123" | 123 |
| "123 Hello World" | 123 |
| "Hello World" | 0 (by default if the string can't be converted, 0 will be returned) |
| "Hello World 123" | 0 |
| "123\.45678" | 123\.46 |

 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| Value | The string to convert |
| Target | The target variable to hold the returned value |

 

#### Example:

The above action block code initialises a global variable and then loads a file with
 a buffer saved in it. Two strings are read from the buffer and stored in a temporary local variables before one of them is converted into a real number and stored in another temporary local variable. These are then assigned to global variables, and
 the buffer is deleted.
