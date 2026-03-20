# title

You can use this action to retrieve the value of the instance variable created for the "score". You supply the target variable to store the returned "score" value (which can be flagged as a temporary local variable), but note that
 if the variable has not been set previously (using [Set Score](Set_Score.md)) then the variable will be created for you and the action will return 0 (unlike regular instance variables which will give an error if you try to access them
 without having set them first).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Target | The target variable to store the returned "score" value (can be flagged as a temporary local variable) |

 

#### Example:

The above action block code will retrieve the current score value and store it in a temporary local
 variable. This variable is then converted into a string and stored in another temporary local variable before being drawn to the screen.
