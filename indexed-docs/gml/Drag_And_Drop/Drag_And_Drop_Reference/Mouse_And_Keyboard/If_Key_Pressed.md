# If Key Pressed

This action checks for the initial press on a keyboard key. It will return true on the single game step (frame) that the key is initially pressed down and false at all other times. If you enable the not modifier, this action
 will be reversed, and check if the key has *not* been pressed down, returning false on the game step (frame) that it has been pressed down and true at all other times. If you need to check for a key being held down and not just
 the initial press event, then use the action [If Key Down](If_Key_Down.md).

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

Any actions dropped elsewhere will be performed after the "if" block.

 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| Key | The name of the key to check. |
| Not | Negate the check (true becomes false and vice versa) |

 

#### Example:

The above action block code polls the keyboard state every step and if a key is
 being held down it checks for the initial key down press. If the check is true on the initial down press, a sound is played, then, while the key is held down, the sprite blending is changed to red. If the key is not being held down, a check
 is done on the key release to reset the blending colour to white.
