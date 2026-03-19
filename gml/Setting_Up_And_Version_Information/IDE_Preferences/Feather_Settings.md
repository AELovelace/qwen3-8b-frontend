# Feather Preferences

Feather provides intelligent code completion and improved syntax checking in your [GML Code](../../GameMaker_Language/GameMaker_Language_Index.md) scripts, along with smart refactoring options.

This page contains information on the following parts of Feather:

Mini TOC (placeholder)

1. Heading

See Also (placeholder)

1. [Topic List](#)

## Base Options

The base Feather Settings contain the following options:

- **Do not analyze project for Room Instances with auto\-generated names**: Enabling this will make Feather not analyse the project for newly added instances. Feather will however analyse your project again when you rename a room instance to a name that's different from its original auto\-generated name.
- **Do not analyze Room Instances**: When this is enabled, Feather will never analyse any Instance Creation Code or reparse the project for new room instances, even when you rename them.
- **Maximum dive depth**: The maximum dive depth the language server will process before throwing a GM1100 warning (for example, nested blocks e.g. conditionals, expressions with multiple values, accessor chains e.g. array\[0]\[? "test"].function().value, etc.). The language server will not process the full context where the maximum dive depth has been exceeded. This function acts as a safeguard against crashes that may happen due the language server not being able to process high depth in code, so changing or disabling this is not recommended. Set to \-1 to disable this feature and get better performance, however depth that is too high may cause instability and even crashes. This is also known as the "maximum [AST node dive](https://en.wikipedia.org/wiki/Abstract_syntax_tree) depth".
- **Enable Feather**: Enable or disable Feather here. When disabled, no Feather features will be available throughout the IDE. This option is only functional for the Legacy Code Editor as Code Editor 2 always has Feather features enabled.
- **Document Parse Delay**: The amount of time Feather waits to check your script after you make a change to it.
- **Compact Tooltips**: Enabling this will remove certain tooltip information that appears when hovering over keywords, such as parameter descriptions for functions, ultimately making your tooltips smaller.
- **The maximum number of struct fields that are displayed by tooltips**: When you hover over a struct reference, a tooltip displays the variables inside that struct, up to the number entered here.
- **Refactor references to asset name when asset is renamed in Asset Browser**: Enabling this will ensure that when you rename an asset in [The Asset Browser](../../Introduction/The_Asset_Browser.md), any mentions of it in your code are also edited so those references don't break.
- **Prefer multiline JSDoc comment style when creating from Quick Fix**: When you generate [JSDoc Comments](../../The_Asset_Editors/Code_Editor_Properties/JSDoc_Script_Comments.md) for a function through the [Quick Fixes](../../The_Asset_Editors/Code_Editor_Properties/Feather_Features.md#h1) menu, the generated JSDoc will either use single\-line or multi\-line [comments](../../GameMaker_Language/GML_Overview/Commenting_Code.md), depending on this option.
- **Enable Strict Type mode**: When this is enabled, Feather is stricter about ensuring you use the correct data types in your code.

## Highlighting

This section contains settings for changing the colours used for underlining part of your code to mark an error, warning or suggestion:

- **Error Colour**: The colour used for errors.
- **Warning Colour**: The colour used for warnings.
- **Suggestion Colour**: The colour used for suggestions.

## Message Severity

This section contains all the rules Feather uses for checking your code, and lets you adjust the severity of each rule. For descriptions of each rule, see [Feather Messages](../../The_Asset_Editors/Code_Editor_Properties/Feather_Messages.md).

### Profile

In this drop\-down box you can choose between presets for the syntax checker. The following profiles are available: 

- **None**: This profile will show no error messages.
- **SyntaxErrors**: If you use this profile, syntax errors will be shown. This is the default.
- **TypeErrors**: This profile also shows type errors in addition to the **SyntaxErrors**profile.
- **All**: This profile shows everything that Feather can analyse.

### GM\* Rules

You can set a rule as an "**Error**", "**Warn**" or "**Suggestion**", which affects the way that rule\-breaking code is reported to you in the Code Editor and the Feather Messages window.

You can set a rule to "**Ignore**" which will ignore all instances of that rule being broken.

All rules starting from "**GM1000**" check your syntax for possible fatal errors, and those starting from "**GM2000**" are best\-practice rules that help you prevent bugs in your game.

## Naming Rules

This section allows you to set naming rules for assets, variables and various other parts of GML Code. Any newly created assets in the Asset Browser will follow the naming rules set here.

The GM2017 rule under "Message Severity" must be enabled for naming rules to take effect. By default, it's disabled (set to "Ignore").

The settings in this section are as follows:

- **Identifier Blocklist**: This is a space\-separated list of identifiers that will be ignored for all naming rules.  

  

 For example, say you have a rule to use obj\_ as a prefix for objects, but you want your objects manager and network to remain as\-is and not use the obj\_ prefix.  

  

 In that case, you would write manager network into the **Identifier Blocklist** field. Feather will ignore those objects *and* any other identifiers (variables, enums, parameters, etc.) with the same names.
- **\ Naming Rule**: You can set naming rules for each type of identifier in the list, such as assets, macros, enums, function parameters, variables, etc.  

  

 Each naming rule drop\-down has the following options:
	- **Naming Style**: Choose the naming style for the identifier. Your options are:
		- **Unconstrained**: No formatting is forced on this type of identifier.
		- **UpperCamelCase**: *MyHealth, ObjGrappleHook*
		- **lowerCamelCase**: *myHealth, objGrappleHook*
		- **ALL\_UPPER**: *MY\_HEALTH, OBJ\_GRAPPLE\_HOOK*
		- **all\_lower**: *my\_health, obj\_grapple\_hook*
	- **Prefix**: Text that should appear before the identifier name, which may be obj\_ for objects, \_ for local variables, etc. depending on your preferences.
	- **Suffix**: Text that should appear after the identifier name.
	- **Preserve trailing and leading underscores**: If enabled, preserves underscores around your asset's name even after suggestions.  
	
	  
	
	 With this, you can use asset names such as \_\_objCamera, keeping any leading and trailing underscores where they are.
