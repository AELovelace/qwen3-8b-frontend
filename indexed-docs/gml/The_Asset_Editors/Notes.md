# The Note Editor

The **Note Editor** will open a code/script window where you can keep notes and code snippets or any other information that you consider relevant to the project. You can create multiple notes and name them from the right mouse button  menu in the [Asset Browser](../Introduction/The_Asset_Browser.md). Notes can also be grouped and reordered like any other asset.

If you have imported a project created using a previous version of GameMaker, then you will also find a [Compatibility Report](../Additional_Information/Compatibility_Scripts.md) included as a note in this section.

## Open On First Load

[The Inspector](../IDE_Tools/The_Inspector.md) will display an "**Open On First Load**" option when a note asset is selected. If enabled, the note will automatically open when the project is imported by someone from a .yyz file or a template.

This is automatically enabled for any note asset that is named "**readme**" (case\-insensitive) and the IDE option for this is disabled for such notes.

The note will open in a Markdown preview window, so any markdown syntax will be rendered. Such a readme note can be used as an introduction to your project or template with crucial information and links for users who import your project.

## [Code Editor 2 (Beta)](The_Text_Editor.md)

When using the new Code Editor 2, Note assets will be displayed with a preview to the right of the editor itself. This will display the Note with any [Markdown](https://www.markdownguide.org/basic-syntax/) formatting applied to it.

  HTML tags are not supported in notes, only Markdown syntax is.

You can make the preview larger or smaller by dragging the bar between the Text Editor and the Preview window. If you drag the Preview window all the way to the right, it will collapse and disappear. To bring it back, right\-click anywhere inside the Text Editor and select "**Open Preview**".

Markdown in GameMaker allows you to include some additional things:

- @AssetName will display that asset's information in preview. This only works for sprites, objects, sounds, shaders and fonts.
- \#RRGGBB will display a colour
- You can use the following in hyperlinks (i.e. \[text](url) format):
	- The file:/// protocol, along with the ${project\_dir} variable to include the current project, e.g. !\[](file:///${project\_dir}/wow.png to insert an image from the project directory
		- file:// is supported as shorthand, only for non\-image hyperlinks
	- The project:// protocol to link to any asset in the project, e.g. \[Wow, a sprite](project://spr\_player). Clicking on this link will open the spr\_player asset in the IDE.
- Multiple line breaks can be achieved by using a backslash (\\) on each line
