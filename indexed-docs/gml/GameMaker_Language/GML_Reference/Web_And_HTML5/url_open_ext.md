# url\_open\_ext

This will open the specified URL on the default browser of the chosen target device, or, if you are using the HTML5 module, in the currently open browser.

The "target" parameter that you specify is the same as the standard JavaScript "name" value when you use the open() method, and you should be aware that all but "**\_self**" may result in the browser blocking, or asking the user if they wish to allow it. This parameter is only used when running in HTML5\.

Valid targets are:

| Target | Description |
| --- | --- |
| \_blank | Opens the linked document in a new window or tab (this will not work if pop\-ups are being blocked by the user, in which case you can use the [clickable\_\*](Web_And_HTML5.md) functions instead). |
| \_self | Opens the linked document in the same frame as it was clicked (this is default). |
| \_parent | Opens the linked document in the parent frame. |
| \_top | Opens the linked document in the full body of the window. |

 
 

#### Syntax:

url\_open\_ext(url, target)

| Argument | Type | Description |
| --- | --- | --- |
| url | [String](../../GML_Overview/Data_Types.md) | The URL (website address) to link to. |
| target | [String](../../GML_Overview/Data_Types.md) | This is the target area to open the URL in. It is only used when using the HTML5 module. |

 

#### Returns:

N/A

 

#### Example:

url\_open\_ext("http://gamemaker.io", "\_blank");

This would open the GameMaker homepage in a new window.
