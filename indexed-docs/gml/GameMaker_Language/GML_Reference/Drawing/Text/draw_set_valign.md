# draw\_set\_valign

This function is used to align text along the vertical axis and changing the vertical alignment will change the position and direction in which all further text is drawn, with the default value being fa\_top. The following constants are accepted:

 
 

#### Syntax:

draw\_set\_valign(valign)

| Argument | Type | Description |
| --- | --- | --- |
| valign | [Vertical Alignment Constant](draw_set_valign.md) | Vertical alignment constant (from the table above). |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_halign(fa\_center);  

 draw\_set\_valign(fa\_middle);  

 draw\_text(100, 32, "Score: " \+ string(score));

The above code will draw the score centered around the very center of the text.
