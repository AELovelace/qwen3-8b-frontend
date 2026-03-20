# Get Draw Font

With this action you can get the font currently assigned for drawing. The value returned will be either a valid font handle (index \>\= 0\) that represents a font constant from [The Asset Browser](../../../Introduction/The_Asset_Browser.md) or an invalid handle (index set to \-1\) for no font assigned. The return value will be stored in the **target variable** that you specify, which can have been created previously or can be a new temporary one (if you check the "Temp" check\-box).

 

#### Action Syntax:

#### Example:

The above action block code checks the current font being used for drawing, and if it's not the given asset, then it is set to that asset.
