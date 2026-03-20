# Show Virtual Keyboard

This action can be used to show the virtual keyboard on the device running the game. When you call this action you will be asked to provide one of the following constants for each of the first three arguments:

- **Keyboard type**: This constant is used to set which key\-set will be available on the virtual keyboard. The available keyboard types are:
 

| Keyboard Type | Description |
| --- | --- |
| kbv\_type\_default | The default keyboard type for the current system. |
| kbv\_type\_ascii | An ASCII\-only keyboard. |
| kbv\_type\_url | A normal keyboard optimized for URL entry. Usually features a ".com" or other domain keys, as well as "/" and "." keys. |
| kbv\_type\_email | A normal keyboard optimized for e\-mail entry. Usually features "@" and "." characters. |
| kbv\_type\_numbers | A numbers\-only keyboard, usually displayed as a number pad. |
| kbv\_type\_phone | A phone pad keyboard. Usually numbers\-only with the "\*" and "\#" keys. |
| kbv\_type\_phone\_name | A keyboard optimized for entering both a phone number and a name. Usually similar to an ASCII keyboard, but with a limited special characters selection. |
- **Return type**: This constant is used to set what is shown on the return/action key of the virtual keyboard. The available return types are:
 

| Return Type | Description |
| --- | --- |
| kbv\_returnkey\_default | The default return key title for the current system. |
| kbv\_returnkey\_go | Sets the return key title to "Go". |
| kbv\_returnkey\_google | Sets the return key title to "Google", or to a generic search icon in some cases. |
| kbv\_returnkey\_join | Sets the return key title to "Go". |
| kbv\_returnkey\_next | Sets the return key title to "Next". |
| kbv\_returnkey\_route | Sets the return key title to "Route". |
| kbv\_returnkey\_search | Sets the return key title to "Search", or to a generic search icon in some cases. |
| kbv\_returnkey\_send | Sets the return key title to "Send". |
| kbv\_returnkey\_yahoo | Sets the return key title to "Yahoo", or to a generic search icon in some cases. |
| kbv\_returnkey\_done | Sets the return key title to "Done". |
| kbv\_returnkey\_continue | Sets the return key title to "Continue". |
| kbv\_returnkey\_emergency | Sets the return key title to "Emergency Call". |
- **Autocapitalization type**: This constant is used to determine how the words typed via the virtual keyboard should be autocapitalized. The available autocapitalization types are:
 

| Autocapitalization Type | Description |
| --- | --- |
| kbv\_autocapitalize\_none | Autocapitalization is disabled. |
| kbv\_autocapitalize\_words | Words will be auto\-capitalized. |
| kbv\_autocapitalize\_sentences | Sentences will be auto\-capitalized. |
| kbv\_autocapitalize\_characters | All characters will be capitalized. |

The last argument is to enable/disable predictive text, and this would be set to true to permit it, and false otherwise, but note that just because it is permitted doesn't mean that it will be used as that will depend on the preferences of the user on the device. When in predictive text mode, the virtual keyboard will not generate normal GameMaker key\-press events. Instead, it will only update the *last* character pressed and keyboard string variables. This is due to the inability to detect whether a change in the internal text field used for detecting key presses came from an actual virtual keyboard key, or a text suggestion. In these cases you would want to read the keyboard\_string input as opposed to reading any kind of raw key input.

It is important to note too that the user will get different keyboards with different capabilities depending on the platform OS, with the following caveats for use per target:

- **Android / Amazon Fire**: On Android, the keyboard type kbv\_type\_phone\_name is not supported and will display an ASCII keyboard instead, and the return key type can only be kbv\_returnkey\_go, kbv\_returnkey\_search, kbv\_returnkey\_next, kbv\_returnkey\_send or kbv\_returnkey\_done. If other return key types are used on that platform, the system will default to the replacement return keys listed below:
 

| Unavailable return key | Replacement key |
| --- | --- |
| kbv\_returnkey\_google kbv\_returnkey\_yahoo | kbv\_returnkey\_search |
| kbv\_returnkey\_join kbv\_returnkey\_route kbv\_returnkey\_emergency | kbv\_returnkey\_go |
| kbv\_returnkey\_continue | kbv\_returnkey\_next |
- **AndroidTV / FireTV**: Custom return key types are *not* supported on ASCII keyboards \- the default return key will always be displayed.
- **tvOS**: Predictive text and auto\-capitalization are not supported on tvOS, and the height of the keyboard returned by system events and the function [keyboard\_virtual\_height()](../../../GameMaker_Language/GML_Reference/Game_Input/Virtual_Keys_And_Keyboards/keyboard_virtual_height.md) will default to the screen height due to it spanning the entire screen and due to keyboard rect dimension functions being disabled on tvOS. Also note that physical (Bluetooth) keyboard events will not be broadcast unless the virtual keyboard has been opened.

Calling this function will generate a [System Asynchronous Event](../../../The_Asset_Editors/Object_Properties/Async_Events.md), in which the [async\_load](../../../GameMaker_Language/GML_Overview/Variables/Builtin_Global_Variables/async_load.md)  [DS map](../../../GameMaker_Language/GML_Reference/Data_Structures/DS_Maps/DS_Maps.md) will be populated with the following key/value pairs:

- "**event\_type**" \- this will be "**virtual keyboard status**" when triggered by virtual keyboard actions.
- "**screen\_height**" \- the height of the virtual keyboard (in pixels). This will be 0 if the keyboard is invisible.
- "**keyboard\_status**" \- the current status of the keyboard, returned as one of the following strings:
	- "hiding"
	- "hidden"
	- "showing"
	- "visible"

 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| keyboard\_type | Determines the key\-set available on the virtual keyboard. |
| return\_key\_type | Determines what is shown on the return/action key of the virtual keyboard. |
| autocapitalization\_type | Determines how/if the words typed via the virtual keyboard will be autocapitalized. |
| predictive\_text\_enabled | Set to true/false to enable/disable predictive text input. |

 

#### Example:

The above action block code checks for a mouse down action, and if one is detected, then a check is performed to see if the OS virtual keyboard is showing. If it isn't then it is set to show, and if it is already showing then it is hidden.
