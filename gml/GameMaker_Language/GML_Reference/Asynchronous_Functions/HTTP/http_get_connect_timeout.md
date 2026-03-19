# http\_get\_connect\_timeout

This function returns the connection timeout value in milliseconds used for HTTP requests.

The default timeout value is 60000 ms, i.e. one minute.

 

#### Syntax:

http\_get\_connect\_timeout()

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_timeout\_ms \= http\_get\_connect\_timeout();  

 show\_debug\_message($"The connection timeout value for HTTP requests is currently set to {\_timeout\_ms} milliseconds.");

The above code retrieves the HTTP request timeout value and stores it in a variable \_timeout\_ms. It then outputs this value in a debug message.
