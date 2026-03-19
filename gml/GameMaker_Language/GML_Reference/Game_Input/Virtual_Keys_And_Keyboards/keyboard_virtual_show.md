# keyboard\_virtual\_show

This function can be used to show the virtual keyboard on the device running the game. See [Virtual Keyboard](Virtual_Keys_And_Keyboards.md#h) for information on platform support.

On Windows, this function is used to enable the use of IMEs after they have been disabled with [keyboard\_virtual\_hide](keyboard_virtual_hide.md). In that case, none of the arguments are used and you can pass undefined to all of them.

 
For virtual keyboard use, you need to provide one of the following constants for each of the first three arguments:

- **Keyboard type**: This constant is used to set which keyset will be available on the virtual keyboard. The available keyboard types are:

| [Virtual Keyboard Type Constant](keyboard_virtual_show.md) | |
| --- | --- |
| Keyboard Type | Description |
| kbv\_type\_default | The default keyboard type for the current system. |
| kbv\_type\_ascii | An ASCII\-only keyboard. |
| kbv\_type\_url | A normal keyboard optimized for URL entry. Usually features a ".com" or other domain keys, as well as "/" and "." keys. |
| kbv\_type\_email | A normal keyboard optimized for e\-mail entry. Usually features "@" and "." characters. |
| kbv\_type\_numbers | A numbers\-only keyboard, usually displayed as a number pad. |
| kbv\_type\_phone | A phone pad keyboard. Usually numbers\-only with the "\*" and "\#" keys. |
| kbv\_type\_phone\_name | A keyboard optimized for entering both a phone number and a name. Usually similar to an ASCII keyboard, but with a limited special characters selection. |

 

- **Return type**: This constant is used to set what is shown on the return/action key of the virtual keyboard. The available return types are:

| [Virtual Keyboard Return Type Constant](keyboard_virtual_show.md) | |
| --- | --- |
| Return Type | Description |
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

| [Virtual Keyboard Autocapitalization Type Constant](keyboard_virtual_show.md) | |
| --- | --- |
| Autocapitalization Type | Description |
| kbv\_autocapitalize\_none | Autocapitalization is disabled. |
| kbv\_autocapitalize\_words | Words will be auto\-capitalized. |
| kbv\_autocapitalize\_sentences | Sentences will be auto\-capitalized. |
| kbv\_autocapitalize\_characters | All characters will be capitalized. |

 

The last argument is to enable/disable predictive text, and this would be set to true to permit it, and false otherwise, but note that just because it is permitted doesn't mean that it will be used as that will depend on the preferences of the user on the device. When in predictive text mode, the virtual keyboard will not generate normal GameMaker keypress events. Instead, it will only update the *last* character pressed and keyboard string variables. This is due to the inability to detect whether a change in the internal text field used for detecting key presses came from an actual virtual keyboard key, or a text suggestion. In these cases you would want to read the keyboard\_string input as opposed to reading any kind of raw key input.

It is important to note too that the user will get different keyboards with different capabilities depending on the platform OS, with the following caveats for use per target:

- **Android**: On Android, the keyboard type kbv\_type\_phone\_name is not supported and will display an ASCII keyboard instead, and the return key type can only be kbv\_returnkey\_go, kbv\_returnkey\_search, kbv\_returnkey\_next, kbv\_returnkey\_send or kbv\_returnkey\_done. If other return key types are used on that platform, the system will default to the replacement return keys listed below:

| Unavailable return key | Replacement key |
| --- | --- |
| kbv\_returnkey\_google  kbv\_returnkey\_yahoo | kbv\_returnkey\_search |
| kbv\_returnkey\_join  kbv\_returnkey\_route  kbv\_returnkey\_emergency | kbv\_returnkey\_go |
| kbv\_returnkey\_continue | kbv\_returnkey\_next |

 

- **AndroidTV / FireTV**: Custom return key types are *not* supported on ASCII keyboards \- the default return key will always be displayed.
  
- **tvOS**: Predictive text and auto\-capitalization are not supported on tvOS, and the height of the keyboard returned by system events and the function keyboard\_virtual\_height() will default to the screen height due to it spanning the entire screen and due to keyboard rect dimension functions being disabled on tvOS. Also note that physical (Bluetooth) keyboard events will not be broadcast unless the virtual keyboard has been opened.
- **Xbox GDK**: See [this Wiki article](https://github.com/GameMakerEnterprise/GMS2-Runner-Xbox/wiki/Keyboard-Input-on-Xbox-GDK)

Calling this function will generate a [System Asynchronous Event](../../../../The_Asset_Editors/Object_Properties/Async_Events/System.md), in which the async\_load DS map will be populated with the following key/value pairs:

- "**event\_type**" \- this will be "**virtual keyboard status**" when triggered by virtual keyboard functions.
  
- "**screen\_height**" \- the height of the virtual keyboard (in pixels). This will be 0 if the keyboard is invisible.
  
- "**keyboard\_status**" \- the current status of the keyboard, returned as one of the following strings:
	- "hiding"
	- "hidden"
	- "showing"
	- "visible"

 

#### Syntax

keyboard\_virtual\_show(keyboard\_type, return\_key\_type, autocapitalization\_type, predictive\_text\_enabled)

| Argument | Type | Description |
| --- | --- | --- |
| keyboard\_type | [Virtual Keyboard Type Constant](keyboard_virtual_show.md) | Determines the keyset available on the virtual keyboard *(see tables at the top)*. |
| return\_key\_type | [Virtual Keyboard Return Type Constant](keyboard_virtual_show.md) | Determines what is shown on the return/action key of the virtual keyboard (*see tables at the top)*. |
| autocapitalization\_type | [Virtual Keyboard Autocapitalization Type Constant](keyboard_virtual_show.md) | Determines how/if the words typed via the virtual keyboard will be autocapitalized *(see tables at the top)*. |
| predictive\_text\_enabled | [Boolean](../../../GML_Overview/Data_Types.md) | Set to true/false to enable/disable predictive text input. |

 

#### Returns:

N/A

 

#### Example:

if (input \=\= false)  

 {  

     input \= true;  

     keyboard\_virtual\_show(kbv\_type\_numbers, kbv\_returnkey\_default, kbv\_autocapitalize\_none, false);  

 }

The above code will bring up the OS virtual keyboard if the given variable is not set to true.
