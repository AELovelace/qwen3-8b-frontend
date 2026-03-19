# title

The throw runtime statement permits you to generate your own [runtime exceptions](../../../Additional_Information/Errors/Runner_Errors.md), ending the game and showing an error message, using the following syntax:

throw (\);

The expression used can be a value or a string or any other data type, and this will then generate an exception error which is \- by default \- shown on the screen and on closing the error message the game will end. For example calling this:

throw ("Hello World!");

will cause the following unhandled exception error to be shown:

You can, however, take over this error message and use your own handler code by calling
 the function [exception\_unhandled\_handler()](../../GML_Reference/Debugging/exception_unhandled_handler.md). This [runtime function](../Runtime_Functions.md) permits you to supply a custom [method](../Method_Variables.md) to use that will be called whenever any unhandled exceptions occur in your game.
