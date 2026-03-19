# event\_perform

This function will perform the code in the specified event, with the designated argument, for the instance running the code. There are many options here which allow complete simulation of all possible events, but note that this literally just performs all the code in the event; the game will not modify anything to make it trigger itself manually.

For example, if you choose to perform a Key Pressed event ev\_keypress, the event will be triggered but the relevant key will not be recognised as having been pressed. Or, if you perform an Alarm event ev\_alarm, the alarm counter will not be set to \-1 but rather continue to count down.

  Asynchronous events can be called using [event\_perform\_async](event_perform_async.md).

The table below outlines all the constants that are included in GameMaker for referencing event *types*, as well as their *number* value. The events themselves are marked in **bold text** and are the same as the values of the [event\_type](event_type.md) variable (to be passed into the first argument of this function), while their number values are marked with *italic text* and are the same as the values of the [event\_number](event_number.md) variable (to be passed into the second argument of this function): 

| [Event Type Constant](event_perform.md) \& [Event Number Constant](event_perform.md) | |
| --- | --- |
| Constant | Description |
| **ev\_create** | Create event |
| **ev\_destroy** | Destroy event |
| **ev\_cleanup** | Clean Up event |
| **ev\_step** | Step event |
| *\-\-\-\- ev\_step\_normal* | Step |
| *\-\-\-\- ev\_step\_begin* | Begin Step |
| *\-\-\-\- ev\_step\_end* | End Step |
| **ev\_alarm** | Alarm event |
| *\-\-\-\- 0 ... 11* | The number relevant to which of the 12 alarms you wish to trigger the event of |
| **ev\_keyboard, ev\_keypress, ev\_keyrelease** | Key Down/Key Pressed/Key Up events |
| *\-\-\-\- any key code* | vk\_space or ord("W") for example |
| **ev\_mouse** | Mouse event |
| *\-\-\-\- ev\_left\_button* | Left button held down on instance |
| *\-\-\-\- ev\_right\_button* | Right button held down on instance |
| *\-\-\-\- ev\_middle\_button* | Middle button (or clickable wheel) held down on instance |
| *\-\-\-\- ev\_no\_button* | No buttons held down |
| *\-\-\-\- ev\_left\_press* | Left button just pressed on instance |
| *\-\-\-\- ev\_right\_press* | Right button just pressed on instance |
| *\-\-\-\- ev\_middle\_press* | Middle button (or clickable wheel) just pressed on instance |
| *\-\-\-\- ev\_left\_release* | Left button just released on instance |
| *\-\-\-\- ev\_right\_release* | Right button just released on instance |
| *\-\-\-\- ev\_middle\_release* | Middle button just released on instance |
| *\-\-\-\- ev\_mouse\_enter* | Mouse just entered instance's bounding box |
| *\-\-\-\- ev\_mouse\_leave* | Mouse just left instance's bounding box |
| *\-\-\-\- ev\_mouse\_wheel\_up* | Mouse wheel scrolled upwards |
| *\-\-\-\- ev\_mouse\_wheel\_down* | Mouse wheel scrolled downwards |
| *\-\-\-\- ev\_global\_left\_button* | Left button held down anywhere |
| *\-\-\-\- ev\_global\_right\_button* | Right button held down anywhere |
| *\-\-\-\- ev\_global\_middle\_button* | Middle button (or clickable wheel) held down anywhere |
| *\-\-\-\- ev\_global\_left\_press* | Left button just pressed anywhere |
| *\-\-\-\- ev\_global\_right\_press* | Right button just pressed anywhere |
| *\-\-\-\- ev\_global\_middle\_press* | Middle button (or clickable wheel) just pressed anywhere |
| *\-\-\-\- ev\_global\_left\_release* | Left button just released anywhere |
| *\-\-\-\- ev\_global\_right\_release* | Right button just released anywhere |
| *\-\-\-\- ev\_global\_middle\_release* | Middle button just released anywhere |
| **ev\_gesture** | A gesture event (Tap, Drag, Flick, Pinch or Rotate) |
| *\-\-\-\- ev\_gesture\_tap* | A single click/touch and release has been detected for an *instance* |
| *\-\-\-\- ev\_gesture\_double\_tap* | Two quick touches/clicks and releases have been detected for an *instance* |
| *\-\-\-\- ev\_gesture\_drag\_start* | The beginning of a drag gesture has been detected for an *instance* |
| *\-\-\-\- ev\_gesture\_dragging* | A touch/click has been held and moved for an *instance* |
| *\-\-\-\- ev\_gesture\_drag\_end* | The release of the touch/click from a drag has been detected for an *instance* |
| *\-\-\-\- ev\_gesture\_flick* | The release of a touch/click from a drag had enough movement for a flick event to be detected for the *instance* |
| *\-\-\-\- ev\_gesture\_pinch\_start* | Two touches and a straight movement have been detected for an *instance* |
| *\-\-\-\- ev\_gesture\_pinch\_in* | The movement between two touches for an *instance* has been detected as inwards |
| *\-\-\-\- ev\_gesture\_pinch\_out* | The movement between two touches for an *instance* has been detected as outwards |
| *\-\-\-\- ev\_gesture\_pinch\_end* | The release of one (or both) touches for a pinch has been detected for an *instance* |
| *\-\-\-\- ev\_gesture\_rotate\_start* | The movement between two touches for an *instance* has been detected as a rotation |
| *\-\-\-\- ev\_gesture\_rotating* | The movement between two touches for an *instance* has been detected as rotating |
| *\-\-\-\- ev\_gesture\_rotate\_end* | The release of one (or both) touches for a rotation has been detected for an *instance* |
| *\-\-\-\- ev\_global\_gesture\_tap* | A single click/touch and release has been detected *anywhere* in the room |
| *\-\-\-\- ev\_global\_gesture\_double\_tap* | Two quick touches/clicks and releases have been detected *anywhere* in the room |
| *\-\-\-\- ev\_global\_gesture\_drag\_start* | The beginning of a drag gesture has been detected *anywhere* in the room |
| *\-\-\-\- ev\_global\_gesture\_dragging* | A touch/click has been held and moved *anywhere* in the room |
| *\-\-\-\- ev\_global\_gesture\_drag\_end* | The release of the touch/click from a drag has been detected *anywhere* in the room |
| *\-\-\-\- ev\_global\_gesture\_flick* | The release of a touch/click from a drag had enough movement for a flick event to be detected *anywhere* in the room |
| *\-\-\-\- ev\_global\_gesture\_pinch\_start* | Two touches and a straight movement have been detected *anywhere* in the room |
| *\-\-\-\- ev\_global\_gesture\_pinch\_in* | The movement between two touches *anywhere* in the room has been detected as inwards |
| *\-\-\-\- ev\_global\_gesture\_pinch\_out* | The movement between two touches *anywhere* in the room has been detected as outwards |
| *\-\-\-\- ev\_global\_gesture\_pinch\_end* | The release of one (or both) touches for a pinch has been detected *anywhere* in the room |
| *\-\-\-\- ev\_global\_gesture\_rotate\_start* | The movement between two touches *anywhere* in the room has been detected as a rotation |
| *\-\-\-\- ev\_global\_gesture\_rotating* | The movement between two touches *anywhere* in the room has been detected as rotating |
| *\-\-\-\- ev\_global\_gesture\_rotate\_end* | The release of one (or both) touches for a rotation has been detected *anywhere* in the room |
| **ev\_collision** | Collision with an object |
| *\-\-\-\- The index of the object to check.* | obj\_enemy for example |
| **ev\_other** | One of the actions listed under 'Other' |
| *\-\-\-\- ev\_outside* | Whether the instance is outside of the room |
| *\-\-\-\- ev\_boundary* | Whether the instance is intersecting the boundary |
| *\-\-\-\- ev\_outside\_view0\...7* | Whether the instance is outside the given view (0 to 7\) |
| *\-\-\-\- ev\_boundary\_view0\...7* | Whether the instance is intersecting the boundary of the given view (0 to 7\) |
| *\-\-\-\- ev\_game\_start* | Only triggered at the start of the game |
| *\-\-\-\- ev\_game\_end* | Only triggered at the end of the game |
| *\-\-\-\- ev\_room\_start* | Only triggered at the start of a room |
| *\-\-\-\- ev\_room\_end* | Only triggered at the end of a room |
| *\-\-\-\- ev\_animation\_end* | If the instance's sprite has reached the end of its animation |
| **\-\-\-\- ev\_animation\_update** | Animation event that runs every step for instances of objects that use skeletal animations |
| **\-\-\-\- ev\_animation\_event** | Animation event that runs for skeletal animations as assigned in the skeletal animation tool |
| *\-\-\-\- ev\_end\_of\_path* | If the instance has reached the end of a path it is following |
| *\-\-\-\- ev\_user0\... ev\_user15* | One of the 16 available user events |
| *\-\-\-\- ev\_broadcast\_message* | Broadcast Message event used for sprites and sequences |
| **ev\_draw** | Draw event. *This event cannot be forced outside of a draw event and the constants are only for identifying the event when performed in these cases.* |
| *\-\-\-\- ev\_draw\_normal* | The (normal) Draw event |
| *\-\-\-\- ev\_draw\_begin* | The Draw Begin event |
| *\-\-\-\- ev\_draw\_end* | The Draw End event |
| *\-\-\-\- ev\_draw\_pre* | The Pre\-Draw event |
| *\-\-\-\- ev\_draw\_post* | The Post\-Draw event |
| *\-\-\-\- ev\_gui* | The Draw GUI event |
| *\-\-\-\- ev\_gui\_begin* | The Draw GUI Begin event |
| *\-\-\-\- ev\_gui\_end* | The Draw GUI End event |

 

#### Syntax:

event\_perform(type, numb)

| Argument | Type | Description |
| --- | --- | --- |
| type | [Event Type Constant](event_perform.md) | The type of event to perform (see the table above). |
| numb | [Real](../../../../GML_Overview/Data_Types.md) or [Event Number Constant](event_perform.md) | The specific event constant or value. No matter if an event has subevents or not, its "default" event is always referred to by event number 0 (e.g. the Create event only has a single subevent which has event number 0, the "normal" Step and Draw events can be referred to by their constants (ev\_step\_normal and ev\_draw\_normal respectively) *or* by their event number 0\) |

 

#### Returns:

N/A

 

#### Extended Example

event\_perform(ev\_keypress, ord("W"));

This would perform the event associated with Keyboard Check Pressed "W" key (without actually generating a keyboard press).

event\_perform(ev\_step, ev\_step\_begin);

This would perform the *Begin Step* event (if called from any of the Step events it would cause the Begin Step event code to be run twice).

event\_perform(ev\_create, 0\);

This would perform the *Create *event of the instance.**
