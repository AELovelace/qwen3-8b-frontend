# os\_version

This variable will tell you the version number for the OS that is running your game. For example, if you are running it on Windows 10, os\_version will be equal to 655360\.

The following table outlines the values that are returned for the most recent versions of the different OS:

| Operating System | Version Name  (version Number) | Return Value (examples) |
| --- | --- | --- |
| Android | Nougat (7\.0 \- 7\.11\)  Oreo (8\.0 \- 8\.11\)  Pie (9\.0\)  Android X (10\.0\) | 24 \- 25  26 \- 27  28  29 |
| iOS  The return value is calculated as:  (major\_version \* 16777216\) \+ (minor\_version \* 4096\) \+ build\_number | iOS 10 (10\.3\)  iOS 11 (11\.4\)  iOS 12 (12\.0\)  iOS 13 (13\.0\) iPhone  iOS 13 (13\.5\) iPhone/iPad | 167784448  184565760  201326592  218103808   218124288 |
| macOS X  The return value is calculated as:  (major\_version \* 16777216\) \+ (minor\_version \* 4096\) \+ build\_number | El Capitan (10\.11\)  Sierra (10\.12\)  High Sierra (10\.13\)  Mojave (10\.14\)  Catalina (10\.15\) | 167817216  167821312  167825408  167829504  167833600 |
| Windows  (the return value is calculated as:  majorVersion \* 65536 \+ minorVersion) | Windows 7 (6\.1\)  Windows 8 (6\.2\)  Windows 8\.1 (6\.3\)  Windows 10 (10\.0\) | 393217  393218  393219  655360 |

 

  Should you require further information about the Windows OS you can use the function [environment\_get\_variable](environment_get_variable.md).

 

#### Syntax:

os\_version

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

if (os\_type \=\= os\_android \&\& os\_version \> 10\)  

 {  

     global.GFX \= 1;  

 }

The above code checks the OS type and version number and if they are both correct then the global variable is set to 1\.
