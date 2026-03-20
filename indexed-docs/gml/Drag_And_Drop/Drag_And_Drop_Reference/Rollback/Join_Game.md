# title

This action attempts to join a game. You must be on a URL that contains the ID of the virtual room to join.

If a room was joined, any actions attached to this action will run.

When a new player joins a game that you are already present in, the **Rollback Event** event is triggered. See [Rollback Events](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Events.md) for more information.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Not | Enabling this will make any attached actions run if a room was *not* joined. You can use this to create a new room when one wasn't found. |
