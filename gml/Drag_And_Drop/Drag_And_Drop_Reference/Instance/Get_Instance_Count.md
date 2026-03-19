# Get Instance Count

With this action you can find the number of instances of any given object currently active within the room. You can select any object from the resource list or you can use the special keyword [all](../../../GameMaker_Language/GML_Overview/Instance_Keywords.md) to get the number of all the instances active. You also need to supply a *target* variable to return the value to so that you can then use it in further actions. If you flag the target variable as "Temp" then this will create a new temporary (local) variable to hold the return value for you, as shown in the example below.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Object | The name of the object to check for. |
| Target | The variable to target for the return value. |

 

#### Example:

The above action block code creates a local (temporary) variable and then assigns the number of instances of the object "obj\_Squirrel" to it. This value is then checked and the instance is destroyed if the number of instances is greater than 100\.
