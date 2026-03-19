# If Key Down

With this action you can poll the keyboard to see if any key is currently being held down. The action will return true every step that the keyboard key is being held down, or false otherwise, although if you click the not modifier you can then check to see if the key is *not* being help, ie: the action will return true while no key is down and false if there is. If you only need to check for a single key press then use the action [If Key Pressed](If_Key_Pressed.md).

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

Any actions dropped elsewhere will be performed after the "if"
 block.

 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| Key | The name of the keyboard key to check. |
| Not | Negate the check (true becomes false and vice versa) |

 

#### Example:

The above action block code polls the keyboard state every step and if a key is being
 held down it checks for the initial key down press. If the check is true on the initial down press, a sound is played, then, while the key is held down, the sprite blending is changed to red. If the key is not being held down, a check is
 done on the key release to reset the blending colour to white.
