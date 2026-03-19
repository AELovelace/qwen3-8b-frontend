# Saving Data

The following functions are specifically to do with saving data using the UWP export for Xbox One and using the the XBox Live features.

While the save data related to player progress must always be associated with a particular user, you can save generic data to the "machine storage" area to by providing the value \-1 as the user argument. This area is title\-specific, but not associated with a particular user.

**NOTE**: No saved file can be larger than 16 megs!

The following functions are for dealing with Xbox Live save data:

- [xboxlive\_set\_savedata\_user](xboxlive_set_savedata_user.md)
- [xboxlive\_get\_savedata\_user](xboxlive_get_savedata_user.md)
- [xboxlive\_get\_file\_error](xboxlive_get_file_error.md)
