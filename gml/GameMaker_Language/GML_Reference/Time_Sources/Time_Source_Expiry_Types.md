# Time Source Expiry Types

| [Time Source Expiry Constant](../../../../GameMaker_Language/GML_Reference/Time_Sources/Time_Source_Expiry_Types.md) | | |
| --- | --- | --- |
| Constant | Description | Value |
| time\_source\_expire\_nearest | The Time Source will expire on the frame nearest to its expiry time | 0 |
| time\_source\_expire\_after | The Time Source will expire on the first frame after its expiry time | 1 |

Time Sources that use seconds as a [unit](Time_Source_Units.md) may not always expire on a game frame. They may expire after a game frame has been processed but before a new frame can start processing.

However, the callback for a Time Source can only run on a game frame, so the expiry type of a Time Source controls when its callback runs, in case it expires in the middle of two frames.

When using time\_source\_expire\_nearest, the callback for a Time Source will run on the frame that's nearest to its expiry time, which may be the frame before it, or the frame after it.

When using time\_source\_expire\_after, the callback for a Time Source will always run on the frame *after* its expiry time.

During a frame, a Time Source is "ticked" (i.e. *updated*) and its callback is executed between the Begin Step and Step events (see [Event Order](../../../The_Asset_Editors/Object_Properties/Event_Order.md)).
