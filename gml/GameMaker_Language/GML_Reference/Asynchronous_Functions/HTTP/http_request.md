# http\_request

This function creates a generic HTTP request and sends it.

A HTTP request can be used for many things like (for example) authentication via HTTP headers if you use RESTful APIs.

The function requires:

- The URL to request. See [URLs](HTTP.md#urls)
- The request method: "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "OPTIONS" or "CONNECT".
- A [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) of key/value pairs containing the HTTP headers "key:value" (as strings, where the key is the header field and the value is the required data for the header). Note that key and value strings shouldn't include the colon ":".
- An optional request body, which can be:
	- A data [String](../../../GML_Overview/Data_Types.md) (can be an empty string "" for an empty body)
	- A [Buffer](../../Buffers/buffer_create.md) (for binary data). If the seek position is at the start (0\), no body is sent and the buffer is filled with the response from the HTTP call. If the seek position is non\-zero, the entire buffer contents (up to [buffer\_set\_used\_size](../../Buffers/buffer_set_used_size.md)) are sent as the body.

The function returns an [Async Request ID](../Asynchronous_Functions.md) which can be used to identify its callback, as described below.

 
## Async Callback

This function will generate "callbacks" which are picked up by any [Async HTTP Events](../../../../The_Asset_Editors/Object_Properties/Async_Events/HTTP.md), in which case it will generate a [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) that is exclusive to this event and is stored in the special variable [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md).

 
 

#### Syntax:

http\_request(url, method, header\_map, body)

| Argument | Type | Description |
| --- | --- | --- |
| url | [String](../../../GML_Overview/Data_Types.md) | The web address of the server that you wish to get information from. See |
| method | [String](../../../GML_Overview/Data_Types.md) | The request method (normally"GET" or "POST", but all methods are supported) |
| header\_map | [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) | A DS map with the required header fields |
| body | [String](../../../GML_Overview/Data_Types.md) or [Buffer](../../Buffers/buffer_create.md) | The data to be transmitted in the body, following the headers (can be a binary buffer handle). |

 

#### Returns:

[Async Request ID](../Asynchronous_Functions.md) (or \-1 if something went wrong)

 

#### Example:

var \_headers \= ds\_map\_create();  

 ds\_map\_add(\_headers, "Authorization", "Basic eW95b19hZG1pbjpjNG5lZmllbGQ\=");  

 ds\_map\_add(\_headers, "Content\-Type", "application/x\-www\-form\-urlencoded");  

 ds\_map\_add(\_headers, "Cookie", "request\_method\=GET; \_InAppPurchases\_session\=69bb6ef6eec2b");  

 var \_data\="utf8\=%E2%9C%93\&authenticity\_token\=kPmS14DcYcuKgMFZUsN3XFfj3mhs%3D\&product%5Bname%5D\=CatchTheHaggis\&product%5Bproduct\_id%5D\=http\_test\&commit\=Create\+Product";  

 request\_id \= http\_request("http://225\.0\.0\.97:3000/products", "POST", \_headers, \_data);  

 ds\_map\_destroy(\_headers);

The above code creates a DS map with the relevant HTTP headers for the request, then creates a data string for use as this is a POST request. Finally, the function is called, with its ID value being stored in the instance variable request\_id for checking in the HTTP asynchronous event.
