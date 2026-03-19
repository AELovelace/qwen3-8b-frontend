# The Gesture Events

Events in the Gesture Event category will be triggered whenever GameMaker detects a "gesture" of the mouse or a touch screen event (while these gesture events are designed specifically for mobile use, they can also be used on other targets to detect the mouse, although they will not detect multiple touches in this case). The goal of the gesture system is to try and recognise inputs at a higher level than the direct mouse/touch reading functions, and is designed to simplify the implementation of commonly used inputs on touch\-based devices.

  These events will not be triggered on the HTML5 platform due to lack of support for multi\-touch using these events on that platform. If you are looking for gestures on that target then you should be using the [device functions](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/Device_Input.md).

You can choose to detect either **instance** gestures or **global** gestures, where instance gesture events will only be triggered when the initial touch/click is on an instance within the room. Note that the instance must have a valid collision mask (see [The Sprite Editor \- Collision Mask](../Sprites.md) and [The Object Editor \- Collision Mask](../Objects.md) sections for more details) for this event to be triggered. Global events, however, will be triggered by touching/clicking anywhere within the game room, and for all instances that have the event.

When a gesture is recognised, it will trigger one or more of the available events, and the event triggered will depend on the type of gesture that has been detected. In every case, however, a [DS Map](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Maps/ds_map_create.md) will be generated for you and stored in the built\-in variable [event\_data](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/event_data.md). The keys available will depend on which kind of event it has been created by and are shown in each of the sub\-sections below.

  The variable [event\_data](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/event_data.md) is only valid in these events, as the DS map that it points to is automatically created at the start of the event, then destroyed again at the end, with this variable being reset to an invalid DS map handle (\-1\) at all other times.

It is worth noting that if you have multiple instances under the position being touched and they all have a gesture event, then *all* of them will trigger, not just the "topmost" instance. Also note that when using multiple camera views and dragging an instance, the values returned will be based on the view you were in when the initial touch/click was received \- this is true for all subsequent events in that gesture for that instance. So touching and dragging an instance in one view then releasing the touch in another view, will return values relative to the initial view where the gesture was first detected.

 

    [Tap, Drag, And Flick Events](#)

The "Tap", "Drag" and "Flick" events are all based on a single touch or mouse click on the screen and the event\_data DS Map will contain the following keys:

| Key | Description |
| --- | --- |
| "gesture" | This is an ID value that is *unique* to the gesture that is in play. This allows you to link the different parts of multi\-part gestures (such as drag start, dragging and drag end) together. |
| "touch" | This is the index of the touch that is being used for the gesture. In general this will start at 0 and increase for each finger that is held down, then reset back to 0 when all fingers are removed, but if the user is touching the screen  anywhere else when this event is triggered by another touch, then the value will be greater than 0\. |
| "posX" | This is the room\-space X position of the touch. |
| "posY" | This is the room\-space Y position of the touch. |
| "rawposX" | This is the *raw* window\-space X position of the touch (equivalent to getting the mouse position using [device\_mouse\_raw\_x()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_raw_x.md)). |
| "rawposY" | This is the *raw* window\-space Y position of the touch (equivalent to getting the mouse position using [device\_mouse\_raw\_y()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_raw_y.md)). |
| "guiposX" | This is the gui\-space X position of the touch (equivalent to getting the mouse position using [device\_mouse\_x\_to\_gui()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_x_to_gui.md)). |
| "guiposY" | This is the gui\-space Y position of the touch (equivalent to getting the mouse position using [device\_mouse\_y\_to\_gui()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_y_to_gui.md)). |
| "diffX" | This is the room\-space X difference between the position of the current touch and the position of the last touch in this gesture. |
| "diffY" | This is the room\-space Y difference between the position of the current touch and the position of the last touch in this gesture. |
| "rawdiffX" | This is the raw X difference between the position of the current touch and the position of the last touch in this gesture. |
| "rawdiffY" | This is the raw Y difference between the position of the current touch and the position of the last touch in this gesture. |
| "guidiffX" | This is the gui\-space X difference between the position of the current touch and the position of the last touch in this gesture. |
| "guidiffY" | This is the gui\-space Y difference between the position of the current touch and the position of the last touch in this gesture. |
| "viewstartposX" | This is the room X start position of the current gesture. |
| "viewstartposY" | This is the room Y start position of the current gesture. |
| "rawstartposX" | This is the raw X start position of the current gesture. |
| "rawstartposY" | This is the raw Y start position of the current gesture. |
| "guistartposX" | This is the gui\-space X start position of the current gesture. |
| "guistartposY" | This is the gui\-space Y start position of the current gesture. |
| "isflick" | **Only available in the Drag End event**. This is set to 1 if the end of the drag is detected as a flick, meaning that you don't need a separate **Flick Event** if you're handling dragging anyway. |

 

[Tap](#)

The Tap event will be triggered when an instance has been touched or clicked or \- if it is a global event \- when the game registers a touch or click anywhere in the room. A tap is considered a quick touch and release, and if the touch lasts too
 long then it will be considered a Drag (and trigger the Drag gesture events instead of the Tap event). This event will generate an event\_data DS map which you can then use to get information about the event. For example:

#### Create Event

x\_goto \= x;  
 y\_goto \= y;

#### Tap Event

x\_goto \= event\_data\[? "posX"];  
 y\_goto \= event\_data\[? "posY"];

#### Step Event

var \_pd \= point\_distance(x, y, x\_goto, y\_goto);  
 move\_towards\_point(x\_goto, y\_goto, clamp(\_pd, 0, 5\);

The above code will detect a tap on the screen and then get the position of the tap to move the instance to that position. Note that if you want to have a longer or shorter tap detection time then you can set it with the function [gesture\_drag\_time()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_drag_time.md).
 This sets the time between the initial detection and the tap becoming a drag, so set it to a higher value to make tap detection longer or a lower value to make it shorter (value is in seconds and defaults to 0\.16\).

 

[Double Tap](#)

The Double Tap event will be triggered when an instance has been touched or clicked twice in quick succession (or \- if it is a global event \- when the game registers two quick touches or clicks anywhere in the room). A double tap is considered two
 quick touches and releases, but if any of the touches lasts too long then it will be considered a Drag (and trigger the Drag gesture events instead of the Double Tap event). This event will generate an event\_data DS
 map which you can then use to get information about the event. For example:

#### Create Event

x\_goto \= x;  
 y\_goto \= y;

#### Double Tap Event

instance\_destroy();

The above code simply detects a double tap and then destroys the instance. Note that you can set the time between taps to trigger a double tap using the function [gesture\_double\_tap\_time()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_double_tap_time.md) (which
 has a default value \- in seconds \- of 0\.16\) and you can also set the distance for detection between taps with the function [gesture\_double\_tap\_distance()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_double_tap_distance.md) (if
 a second tap is detected outside of this distance it will be considered a regular tap event).

 

[Drag Start](#)

The Drag Start event will be triggered when the user maintains a touch or click without releasing it. It will be triggered once when a set time has passed after the initial touch, which is 0\.16 seconds by default (although you can set this to any
 other value in seconds using the function [gesture\_drag\_time()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_drag_time.md)). After this event has been triggered, and as long as
 the user has a touch/click held down, then the Dragging event will be triggered every step until the touch/click has been released. This event will generate an event\_data DS map which you can then use to get information
 about the event. For example:

#### Create Event

drag\_offsetX \= 0;  
 drag\_offsetY \= 0;

#### Drag Start Event

drag\_offsetX \= x \- event\_data\[?"posX"];  
 drag\_offsetY \= y \- event\_data\[?"posY"];

The above code uses the Drag Start event to get the position of the touch/click and use it to set an offset value for the x and y axis. This can then be used when dragging the instance to ensure that it doesn't "jump" to the position
 that the touch/click was detected at (see the Dragging event below for a continuation of this example).

 

[Dragging](#)

The Dragging event is triggered after the Drag Start event, and will be triggered for every step that the user maintains the touch/click on the instance (or the screen, if it's a global event) and moves more than the defined dragging threshold.
 This distance is 0\.1 inches by default but can be set using the function [gesture\_drag\_distance()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_drag_distance.md). If there is no
 movement or the movement is under the defined threshold, the event will not be triggered. This event will generate an event\_data DS map which you can then use to get information about the event. For example:

#### Create Event

drag\_offsetX \= 0;  
 drag\_offsetY \= 0;

#### Drag Start Event

drag\_offsetX \= x \- event\_data\[?"posX"];  
 drag\_offsetY \= y \- event\_data\[?"posY"];

#### Dragging Event

x \= event\_data\[?"posX"] \+ drag\_offsetX;  
 y \= event\_data\[?"posY"] \+ drag\_offsetY;

The example code above uses the offset variables set in the Drag Start event to move the instance when the Dragging event is triggered.

 

[Drag End](#)

The Drag End event is triggered when the user releases the touch/click on the instance (or the screen if the event is global). This event will generate an event\_data DS map which you can then use to get information about
 the event, but in this event the map will have an extra key: "isflick". Flick is calculated as the distance per second that the drag has occurred over, and the value for the "isflick"
 key will be true if it is greater than the defined distance per second value, or false otherwise. Note that the default is 2 inches per second, but you can set it to another value using the function [gesture\_flick\_speed()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_flick_speed.md).
 Also note that there is a dedicated Flick event which will also be triggered if the "isflick" variable is true. An example of use would be:

#### Create Event

flickVelX \= 0\.0;  
 flickVelY \= 0\.0;

#### Drag End Event

isFlick \= event\_data\[?"isflick"];  
 if (isFlick)  
     {  
     flickVelX \= event\_data\[?"diffX"];  
     flickVelY \= event\_data\[?"diffY"];  
     }  
 else
   
     {  
     flickVelX \= 0;  
     flickVelY \= 0;  
     }
 

#### Step Event

x \+\= flickVelX;  
 y \+\= flickVelY;  
 flickVelX \*\= 0\.7;  
 flickVelY \*\= 0\.7;

The above code simply gets the difference in x and y position of the last Dragging event and the current Drag End event, and if the movement has been greater than the flick threshold, it sets some variables that are use to the move the instance
 in the step event.

 

[Flick](#)

The Flick event is only triggered when a touch/click has been held, dragged and then released and the distance between the last drag position and the release position is greater than 2 inches per second (this is the default setting, although this
 can be changed using the function [gesture\_flick\_speed()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_flick_speed.md)). This event will generate an event\_data DS map which you can then use to get information about the event. For example:

#### Create Event

flickVelX \= 0\.0;  
 flickVelY \= 0\.0;

#### Flick Event

flickVelX \= event\_data\[?"diffX"];  
 flickVelY \= event\_data\[?"diffY"];

#### Step Event

x \+\= flickVelX;  
 y \+\= flickVelY;  
 flickVelX \*\= 0\.7;  
 flickVelY \*\= 0\.7;

The above code simply gets the difference in x and y position of the last Dragging event and the current Flick event, and if the movement has been greater than the flick threshold, it sets some variables that are use to the move the instance in
 the step event.

 

[Pinch Events](#) 

The "Pinch" events are based on two touches to the devices screen being recognised at once, where one (or both) have moved more than a certain distance. The angle of movement of the touches along with the movement of each touch is what will
 determine the detection of a Pinch or Rotate event, where (in the case of the Pinch Event type):

- If one of the touches isn't moving, the other must be moving towards it or away from it within a threshold angle (which can be set using the functions [gesture\_pinch\_angle\_towards()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_pinch_angle_towards.md) and
 \- [gesture\_pinch\_angle\_away()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_pinch_angle_away.md)).
- If both touches are moving, their velocities must be in approximately opposite directions and the same angular threshold check is also done to ensure the touches are moving in approximate alignment.

When two touches and a movement are detected with the above criteria, a Pinch Event will be triggered, and in each of the events the event\_data DS Map will be populated with the following keys:

| Key | Description |
| --- | --- |
| "gesture" | This is an ID value that is *unique* to the gesture that is in play. This allows you to link the different parts of multi\-part gestures (such as drag start, dragging and drag end) together. |
| "touch1" | This is the index of the first touch that is being used as part of the pinch gesture. In general this will be 0, but if the user is touching the screen anywhere else when this event is triggered by another touch, then the value will be  greater than 0\. |
| "touch2" | This is the index of the second touch that is being used as part of the pinch gesture. In general this will be 1 more than the value for touch1, but may be some other value depending on the number of touches being detected elsewhere. |
| "posX1" | This is the room\-space X position of the first touch. |
| "posY1" | This is the room\-space Y position of the first touch. |
| "rawposX1" | This is the *raw* window\-space X position of the first touch (equivalent to getting the mouse position using [device\_mouse\_raw\_x()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_raw_x.md)). |
| "rawposY1" | This is the *raw* window\-space Y position of the first touch (equivalent to getting the mouse position using [device\_mouse\_raw\_y()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_raw_y.md)). |
| "guiposX1" | This is the gui\-space X position of the first touch (equivalent to getting the mouse position using [device\_mouse\_x\_to\_gui()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_x_to_gui.md)). |
| "guiposY1" | This is the gui\-space Y position of the second touch (equivalent to getting the mouse position using [device\_mouse\_y\_to\_gui()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_y_to_gui.md)). |
| "posX2" | This is the room\-space X position of the second touch. |
| "posY2" | This is the room\-space Y position of the second touch. |
| "rawposX2" | This is the *raw* window\-space X position of the first touch. |
| "rawposY2" | This is the *raw* window\-space Y position of the second touch. |
| "guiposX2" | This is the gui\-space X position of the second touch. |
| "guiposY2" | This is the gui\-space Y position of the second touch. |
| "midpointX" | The X position of the mid point between the two touches in room space. |
| "midpointY" | The Y position of the mid point between the two touches in room space. |
| "rawmidpointX" | This is the raw window\-space X position of the mid point. |
| "rawmidpointY" | This is the raw window\-space Y position of the mid point. |
| "guimidpointX" | This the gui\-space X position of the mid point. |
| "guimidpointY" | This the gui\-space Y position of the mid point. |
| "relativescale" | This is difference in scale compared to the last event in this gesture (so for **Pinch In** events this will always be smaller than 1\.0, whereas for **Pinch Out** events it will always be larger than 1\.0\) |
| "absolutescale" | This is the scale compared to where the fingers were when the gesture started (so if the distance between the fingers has halved then this will be 0\.5 whereas if the distance has doubled it will be 2\.0\). |

 

[Pinch Start](#)

The Pinch Start event will be triggered when an instance (or the screen if the event is global) has been touched by two "fingers" (and the touch is maintained) and then one or both of the "fingers" is moved. If the touches move
 away from each other or towards each other more than the minimum check distance (which is 0\.1 inches by default, but it can be set using the function [gesture\_pinch\_distance()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_pinch_distance.md)),
 and the angle between them is within the defined value (this defaults to 45° but can be set using [gesture\_pinch\_angle\_towards()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_pinch_angle_towards.md) and
 [gesture\_pinch\_angle\_away()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_pinch_angle_away.md)), then a Pinch Start event will be triggered. In this event you can set variables or store position date for future use. For example:
 

#### Pinch Start Event

pinching \= true;  
 pinch\_x \= event\_data\[? "midpointX"]; pinch\_y \= event\_data\[? "midpointY"];

The above code will detect a pinch and store the midpoint position for that pinch.

 

[Pinch In / Pinch Out](#)

The Pinch In and Pinch Out events will be triggered every step that the distance between the two touches that make up the pinch changes over the minimum threshold (set to \+/\- 0\.1 inches by default, but you can change it using the function gesture\_pinch\_distance).
 If there is no movement of the pinch touches then these events will not trigger. These events will generate an event\_data DS map which you can then use to get information about the event. For example:

#### Global Pinch In /Pinch Out Event

var \_scale \= event\_data\[? "relativescale"];  
 var \_w \= camera\_get\_view\_width(view\_camera\[0]);  
 var \_h \= camera\_get\_view\_height(view\_camera\[0]);  
 var \_x \= camera\_get\_view\_x(view\_camera\[0]) \+ (\_w / 2\);  
 var \_y \= camera\_get\_view\_y(view\_camera\[0])
 \+ (\_h / 2\);  

  
 \_w \*\= \_scale;  
 \_h \= \_w \* (room\_height / room\_width);  
 \_x \-\= \_w / 2;  
 \_y \-\= \_h / 2;  

  
 camera\_set\_view\_pos(view\_camera\[0], \_x, \_y);  
 camera\_set\_view\_size(view\_camera\[0], \_w, \_h);
 

The above code will scale the view based on the relative scale of the pinch touches.

 

[Pinch End](#)

The Pinch End event will be triggered when the user releases one (or both) of the touches from the device. This events will generate an event\_data DS map which you can then use to get information about the event. For
 example:

#### Pinch End Event

var \_pinchx \= event\_data\[? "midpointX"];  
 var \_pinchy \= event\_data\[? "midpointY"];  
 var \_w \= camera\_get\_view\_width(view\_camera\[0]);  
 var \_h \= camera\_get\_view\_height(view\_camera\[0]);  
 var \_x \= \_pinchx \- (\_w / 2\);  
 var \_y \= \_pinchy \- (\_h / 2\);  

  
 camera\_set\_view\_pos(view\_camera\[0], \_x, \_y);
 

The above code will set the view position to be centered on the midpoint of the two touches that made up the pinch when the touches are released.

 

[Rotate Events](#)

The "Rotate" events are based on two touches to the devices screen being recognised at once, and where there has been a consistent angular rotation between the two within a specific time. The angle of movement of the touches along with the
 movement of each touch is what will determine the detection of a Pinch or Rotate event, where (in the case of the Rotate Event type):

- Two touches must be held down for a specified minimum time (the default time is 0\.16 seconds, but you can change it using the function [gesture\_rotate\_time()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_rotate_time.md)).
- Within this minimum time period they must rotate in a consistent direction (if the rotation direction changes within that time then no rotate is started).
- The rotation amount must exceed the minimum threshold angle (which is set to 5° by default, but this can be changed using the function [gesture\_rotate\_angle()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_rotate_angle.md)).

When two touches and a movement are detected with the above criteria, a Rotate Event will be triggered, and in each of the events the event\_data DS Map will be populated with the following keys:

| Key | Description |
| --- | --- |
| "gesture" | This is an ID value that is *unique* to the gesture that is in play. This allows you to link the different parts of multi\-part gestures (such as drag start, dragging and drag end) together. |
| "touch1" | This is the index of the first touch that is being used as part of the pinch gesture. In general this will be 0, but if the user is touching the screen anywhere else when this event is triggered by another touch, then the value will be  greater than 0\. |
| "touch2" | This is the index of the second touch that is being used as part of the pinch gesture. In general this will be 1 more than the value for touch1, but may be some other value depending on the number of touches being detected elsewhere. |
| "posX1" | This is the room\-space X position of the first touch. |
| "posY1" | This is the room\-space Y position of the first touch. |
| "rawposX1" | This is the *raw* window\-space X position of the first touch (equivalent to getting the mouse position using [device\_mouse\_raw\_x()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_raw_x.md)). |
| "rawposY1" | This is the *raw* window\-space Y position of the first touch (equivalent to getting the mouse position using [device\_mouse\_raw\_y()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_raw_y.md)). |
| "guiposX1" | This is the gui\-space X position of the first touch (equivalent to getting the mouse position using [device\_mouse\_x\_to\_gui()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_x_to_gui.md)). |
| "guiposY1" | This is the gui\-space Y position of the second touch (equivalent to getting the mouse position using [device\_mouse\_y\_to\_gui()](../../GameMaker_Language/GML_Reference/Game_Input/Device_Input/device_mouse_y_to_gui.md)). |
| "posX2" | This is the room\-space X position of the second touch. |
| "posY2" | This is the room\-space Y position of the second touch. |
| "rawposX2" | This is the *raw* window\-space X position of the first touch. |
| "rawposY2" | This is the *raw* window\-space Y position of the second touch. |
| "guiposX2" | This is the gui\-space X position of the second touch. |
| "guiposY2" | This is the gui\-space Y position of the second touch. |
| "pivotX" | The X position of the rotation pivot point in room space. |
| "pivotY" | The Y position of the rotation pivot point in room space. |
| "rawpivotX" | This is the raw window\-space X position of the rotational pivot point. |
| "rawpivotY" | This is the raw window\-space Y position of the rotational pivot point. |
| "guipivotX" | This the gui\-space X position of the rotational pivot point. |
| "guipivotY" | This the gui\-space Y position of the rotational pivot point. |
| "relativeangle" | This is difference in rotation compared to the last event in this gesture, measured in degrees |
| "absoluteangle" | This is the difference in angle compared to where the fingers were when the gesture started, measured in degrees. So, for example, if the fingers have rotated a quarter\-circle since the start of the gesture then this value will be 90°  or \-90°, depending on the direction of rotation. |

 

[Rotate Start](#)

The Rotate Start event will be triggered when an instance (or the screen if the event is global) has been touched by two "fingers" (and the touch is maintained) and then one or both of the "fingers" is rotated from its start
 position. The rotation of the touches needs to have started within a short period of time (0\.16 seconds by default, but it can be set using the function [gesture\_rotate\_time()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_rotate_time.md))
 and be greater than the minimum angular threshold (by default 5°, but, this can be changed using the function [gesture\_rotate\_angle()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_rotate_angle.md)).
 If these checks are true, then a Rotate Start event will be triggered and you can use it to store values or set variables for use with the rest of the rotate events. For example:

#### Create Event

rotating \= false;  
 view\_a \= camera\_get\_view\_angle(view\_camera\[0]);

#### Rotate Start Event

rotating \= true;

The above code simply sets up some variables for rotating the view camera, and then in the Rotate Start event, it sets one of them to true.

 

[Rotating](#)

The Rotating event will be triggered every step that the touches on the screen rotate around each other, as long as the movement is greater than the minimum angular threshold (by default 5°, but, this can be changed using the function [gesture\_rotate\_angle()](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/gesture_rotate_angle.md)).
 This event can be used to set variables and manipulate instances, for example:

#### Rotating Event

var \_relangle \= event\_data\[?"relativeangle"];  
 var \_a \= camera\_get\_view\_angle(view\_camera\[0]);  
 \_a \+\= \_relangle;  
 camera\_set\_view\_angle(view\_camera\[0], \_a);

The above code rotates the camera view depending on the rotational movement of the touches in the event.

 

[Rotate End](#)

The Rotate End event will be triggered when one (or both) touches that comprise the gesture are released from the device screen. This event can be used to set variables and manipulate instances, for example:

#### Rotate End Event

rotating \= false;

#### Step Event

if (!rotating)   
     {  
     var \_a \= camera\_get\_view\_angle(view\_camera\[0]);  
     var \_adif \= angle\_difference(view\_a, \_a);  
     \_a \+\= median(\-5, \_adif, 5\);  
     camera\_set\_view\_angle(view\_camera\[0], \_a);  
     }

The above code uses the Rotate End event to detect when the user stops the gesture and then sets a variable. This variable is then used in the step event to rotate the view camera back to its original position.
