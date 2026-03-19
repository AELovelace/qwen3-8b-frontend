# The Keyframe Struct

Each track (as defined on the page covering [track structs](The_Track_Struct.md)) will have one or more keyframe [structs](../../../../GML_Overview/Structs.md) assigned to it (which you can get from the keyframes property of the track struct), and each one will have the following properties:

| [Sequence Keyframe Struct](The_Keyframe_Struct.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| frame | [Real](../../../../GML_Overview/Data_Types.md) | The position (in frames) along the timeline for the keyframe. Default value is 0\. |
| length | [Real](../../../../GML_Overview/Data_Types.md) | The length of the keyframe. Default value is 1, and when set to larger values then the track property that the keyframe refers to will be maintained at the initial value for the duration of the length given. Note that the stretch property will override this if set to true. |
| stretch | [Boolean](../../../../GML_Overview/Data_Types.md) | If this property is set to true then the keyframe stretches to either the next keyframe for the track or to the end of the track if it's the last keyframe. You can get or set this value, and the default value is false. |
| channels | [Array](../../../../GML_Overview/Arrays.md) of [Sequence Keyframe Data Struct](The_Keyframe_Data_Struct.md)s | This property allows access to the list of [keyframe data structs](The_Keyframe_Data_Struct.md) for the channels of the track. When getting this property an [array](../../../../GML_Overview/Arrays.md) of keyframe data structs is returned, and when setting this property an array of keyframe data structs should be specified. |
