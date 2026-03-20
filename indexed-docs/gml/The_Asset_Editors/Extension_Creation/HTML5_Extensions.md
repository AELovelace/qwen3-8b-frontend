# HTML5 / GX.games Code Injection

You can inject custom HTML into your game's index.html file through extensions. This is done by clicking on "HTML5" under "Platform Settings" in an extension's editor:

This also applies to the GX.games target.

## Insertion Tags

In the "Code Injection" window, you can add custom HTML for your index.html file. Such HTML is inserted into different parts of the index.html file by using the following tags:

| Tag | Description |
| --- | --- |
| GM\_HTML5\_PreHead | HTML is inserted before the \ starting tag |
| GM\_HTML5\_PostHead | HTML is inserted after the \ ending tag |
| GM\_HTML5\_PreStyle | HTML is inserted inside \ \, but before \ |
| GM\_HTML5\_PostStyle | HTML is inserted inside \ \, but after \ |
| GM\_HTML5\_PreBody | HTML is inserted before the \ starting tag |
| GM\_HTML5\_BodyStart | HTML is inserted after the \ starting tag |
| GM\_HTML5\_PreCanvas | HTML is inserted before the \ starting tag in the body |
| GM\_HTML5\_Canvas | HTML is inserted in the \ tag in the body |
| GM\_HTML5\_PostCanvas | HTML is inserted after the \ ending tag in the body |
| GM\_HTML5\_BodyEnd | HTML is inserted before the \ ending tag |
| GM\_HTML5\_PostBody | HTML is inserted after the \ ending tag |

Here is an example of HTML code injected into some of the above tags:

Multiple extensions may inject code into the same tag, however the order of their insertions into the final HTML file cannot be guaranteed.

## Variables

Within your injected JavaScript code, you may use variables that GameMaker provides. You can see such variables in the example above, wrapped inside ${ }.

You can use environment variables set up by the IDE that start with YY or YYMACROS\_. You can also read your custom extension options by using the ${YYEXTOPT\_HTML5Injection\_OPTIONNAME} syntax.

  Using the environment variables and extension options mentioned above is not supported on HTML5\.

The following built\-in variables can be used with the ${VARIABLE} syntax:

| Variable | Description |
| --- | --- |
| GM\_HTML5\_BrowserTitle | The title of the browser window |
| GM\_HTML5\_BackgroundColour | The background colour of the page |
| GM\_HTML5\_GameWidth | The width of the game's canvas (in pixels) |
| GM\_HTML5\_GameHeight | The height of the game's canvas (in pixels) |
| GM\_HTML5\_GameFolder | The name of the folder containing the HTML file |
| GM\_HTML5\_GameFilename | The name of the HTML file |
| GM\_HTML5\_CacheBust | A random value used for [cache\-busting](https://www.keycdn.com/support/what-is-cache-busting); can be added as a URL parameter in custom links to prevent the browser from getting the cached version of a file |

## Template HTML File (HTML5 Target)

You can get the template index.html file from the [runtime directory](../../Settings/Building_via_Command_Line.md), under runtime\-\[version]/html5/index.html. Here you can view the template file to understand where the tags are inserted. You can make a modified copy and use it for your game instead of the default file, by adding it as an [Included File](../../Settings/Included_Files.md) and selecting it in the .

The template HTML file will contain some tags starting with GM\_HTML5\_Inject\*. These are used by GameMaker to inject values from the [HTML5 Game Options](../../Settings/Game_Options/HTML5.md), and as such can't be used for inserting custom code.
