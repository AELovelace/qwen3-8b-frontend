# event\_action

This **read\-only** variable returns the index of the action currently being executed, starting at 0 on previous versions of GameMaker. However, this is **now an obsolete variable**in GameMaker. It has been left in for legacy support only, and will **always return 0** as all actions are concatenated together to improve execution speed.

 

#### Syntax:

event\_action

 

#### Returns:

[Real](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

num \= event\_action;

The above code stores the current action number in the variable "num".
