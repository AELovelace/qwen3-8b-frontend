# title

This function can be used to retrieve data about specific stats from the Xbox Live servers. You supply the user ID as returned by the function [xboxlive\_get\_user()](../Users_And_Accounts/xboxlive_get_user.md), then your games Service Configuration ID (as shown on the XDP console), and finally the stats required. You can request up to a maximum of 14 stats, but this does not guarantee that you will get 14 stat results, as there is a limit to the total length of the request and therefore the maximum stat count depends on the length of the names of the stats themselves.

The function will return 0 if the stat request was sent or \-1 if there was an error, and the callback will trigger a [System Asynchronous Event](../../../../The_Asset_Editors/Object_Properties/Async_Events/System.md). This event will have the special DS map [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) which should then be parsed for the following key:

- "**event\_type**" \- should hold the string "**stat\_result**" if the event was triggered by this function

If the event type relates to this function, then there will also be the following additional key:

- "**user**" \- holds the user ID for the requested stats.

There may also be an extra set of key value pairs, where the key is the stat name requested, and the value the value for that stat on the server. Note that if a stat has never been created for this user (because they haven't fired the events that set it), no value may be returned for that stat ([ds\_map\_exists()](../../Data_Structures/DS_Maps/ds_map_exists.md) can be used to check for the stats in the async\_load map).

If the request fails due to the request length being to large, there should be a message in the console output stating the error code:

xboxlive\_get\_stats\_for\_user \- exception occurred getting results \- 0x80190190

When this happens, the async event DS map should have a "succeeded" key with a value of "0", and in this case you should attempt to retrieve fewer stats in a single call.

 

#### Syntax:

xboxlive\_get\_stats\_for\_user(user\_id, serviceconfig\_id, statname1, …);

| Argument | Type | Description |
| --- | --- | --- |
| user\_id | Xbox User ID | The user ID pointer. |
| serviceconfig\_id | String | The service config file ID |
| statname1 (2, 3, etc...) | Strings | The stat names to retrieve the information for. |

 

#### Returns:

Real

 

#### Example:

var \_uid \= xboxlive\_get\_user(0\);  

 var \_configid \= "00000000\-0000\-0000\-0000\-000000000000";  

 xboxlive\_get\_stats\_for\_user(xbuser, \_configid, "GameProgress", "CurrentMode");

The above code gets the user ID and then uses that to request information about specific stats for that user.
