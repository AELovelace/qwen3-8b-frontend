# window\_mouse\_set\_locked

This function locks the mouse cursor in place inside the window, and makes it invisible.

Mouse movement can still be read through the functions [window\_mouse\_get\_delta\_x](window_mouse_get_delta_x.md) and [window\_mouse\_get\_delta\_y](window_mouse_get_delta_y.md).

The cursor is set back to its previous "visible" state when mouse lock is disabled again, i.e. when the function is called with enable set to false.

 
  Use [window\_mouse\_get\_locked](window_mouse_get_locked.md) to get the locked state of the mouse.

  On HTML5 this function cannot be used in the Create event as this platform requires that the canvas is clicked first.

 
 

#### Syntax:

window\_mouse\_set\_locked(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to lock the mouse or not |

 

#### Returns:

N/A

 

#### Example: Basic Use
