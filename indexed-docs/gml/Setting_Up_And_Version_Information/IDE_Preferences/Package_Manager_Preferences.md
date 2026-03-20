# Package Manager Preferences

This contains preferences for the [Package Manager](../../IDE_Tools/Package_Manager.md):

- **Packages Install Directory**: The directory where packages are installed. The [GMRT Preferences](GMRT_Preferences.md) should be set to look in this directory.
- **Default Source URL**: This is the default package source URL used when a new Package Source is added in the Package Manager.
- **Remote search endpoint**: This is the default "URL Search Path" option used when a new Package Source is added. This differs between registries. For example:
	- Verdaccio\-based registries return a JSON list of all packages when using the \-/verdaccio/data/packages endpoint, such that the final URL is [http://registry.com/\-/verdaccio/data/packages](http://registry.com/-/verdaccio/data/packages)
	- npmjs is a common public provider of npm packages and uses the endpoint \-/v1/search?text\=@gamemaker to perform a search query on the registry such that the final URL is [https://registry.npmjs.com/\-/v1/search?text\=@gamemaker](https://registry.npmjs.com/-/v1/search?text=@gamemaker)
	- GitHub repos can also be used as npm registries, however, these "registries" only contain a single package as specified by the endpoint @username/project\-name, such that the final URL is [https://npm.pkg.github.com/@username/project\-name](https://npm.pkg.github.com/@username/project-name).
- **Registry config URL**: The URL used to retrieve the set of package sources in the Package Manager. Only modify this upon instruction from the GameMaker team.
- **Default Package Source:** The package source that opens by default when you open the Package Manager.
