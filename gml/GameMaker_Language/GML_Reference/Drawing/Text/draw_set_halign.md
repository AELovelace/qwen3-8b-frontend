# draw\_set\_halign

This function is used to align text along the horizontal axis and changing the horizontal alignment will change the position and direction in which all further text is drawn with the default value being fa\_left. The following constants are accepted:

 
 

#### Syntax:

draw\_set\_halign(halign)

| Argument | Type | Description |
| --- | --- | --- |
| halign | [Horizontal Alignment Constant](draw_set_halign.md) | Horizontal alignment constant (from the table above). |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_halign(fa\_left);  

 draw\_text(100, 32, "Score: " \+ string(score));  

 draw\_set\_halign(fa\_right);  

 draw\_text(room\_width \- 100, 32, "Health: " \+ string(health));

The above code will draw two strings on the same line, with the score being left\-hand aligned and the health being right\-hand aligned.
