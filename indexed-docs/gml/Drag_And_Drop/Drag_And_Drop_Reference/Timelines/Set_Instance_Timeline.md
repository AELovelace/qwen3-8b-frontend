# title

This action assigns a timeline from the Asset Browser to the instance. You give the timeline to assign , and then you can choose to have the timeline loop when it reaches the last moment (the next frame after the last moment is run will loop back to
 the first moment of the timeline again) as well as whether to start the timeline immediately or not. If you do not start the timeline immediately you can use the action [Set Timeline State](Set_Timeline_State.md) to start it later in another
 event or script.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Timeline | The timeline resource to assign to an instance |
| Loop | Flag to have the timeline loop after the last moment (default is flagged) |
| Start Timeline | Flag to have the timeline start immediately or not (default is flagged) |

 

#### Example:

The above action block code will assign a timeline to the instance calling
 the actions as well as set the initial moment to 10 and then the timeline speed to 2\.
