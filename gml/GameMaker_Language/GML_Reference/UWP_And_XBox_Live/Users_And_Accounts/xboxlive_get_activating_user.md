# title

With this function you can retrieve the user ID pointer for the user that launched the game from the console.

**NOTE**: How you use this pointer will depend on what you want to do in the game, but you should not rely on it to be the currently playing User ID as the activating user can logout while the game is running.

 

#### Syntax:

xboxlive\_get\_activating\_user();

 

#### Returns:

Xbox User ID

 

#### Example:

global.activUser \= xboxlive\_get\_activating\_user();

The above stores the activating user ID pointer in a global variable
