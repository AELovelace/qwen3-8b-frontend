# title

With this action you can create or set an instance variable for score. You supply the value to either set the score variable to or to add to the score variable (if you tick the *relative* checkbox then the value will be added to the current "score"
 value). Note that unlike regular instance variables the variable name for "score" is stored internally so to retrieve the score value you need to use the action [Get Score](Get_Score.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Score | The amount to set the score to (or to add on to the score if *relative* is checked) |

 

#### Example:

The above action block code will check to see if the room is the first in the game and if it is it
 sets up "score", "lives" and "health" variables for the instance.
