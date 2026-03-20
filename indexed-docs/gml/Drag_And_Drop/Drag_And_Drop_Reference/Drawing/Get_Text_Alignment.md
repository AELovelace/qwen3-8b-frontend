# Get Text Alignment

This action will get the font alignment for all current draw text actions. You can choose whether to retrieve the horizontal or vertical alignment to check, and the action will return one of the following *constant* values, that represent a different
 type of horizontal or vertical alignment:

|  | Text is horizontally aligned to the left |
| --- | --- |
|  | Text is horizontally aligned to the center |
|  | Text is horizontally aligned to the right |
|  | Text is vertically aligned to the top |
|  | Text is vertically aligned to the middle |
|  | Text is vertically aligned to the bottom |

The return constant will be stored in the **target variable** that you specify, which can have been created previously or can be a new temporary one (if you check the "Temp" check\-box).

 

#### Action Syntax:

#### Example:

The above action block code checks the horizontal text alignment and
 if it's not set to fa\_left, then it is set to that value.
