# current\_hour

This **read\-only** variable will return the hour that corresponds to the current moment based on the default time zone for the system (ie: local time). You can change the base time zone to use with the function [date\_set\_timezone()](date_set_timezone.md).

 

#### Syntax:

current\_hour

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

draw\_text(32, 32, "The time is " \+ string(current\_hour) \+ ":" \+ string(current\_minute) \+ "." \+ string(current\_second));

The above code would draw the current international time on the screen.
