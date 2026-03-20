# os\_browser

This **read\-only** variable holds one of various constants (listed below) that GameMaker has to tell you which browser you are currently running the game in (if any).

  The GX.games target, even though it runs on a browser, always returns browser\_not\_a\_browser.

 

#### Syntax:

os\_browser

 

#### Returns:

[Browser Type Constant](os_browser.md)

| [Browser Type Constant](os_browser.md) | |
| --- | --- |
| Constant | Description |
| browser\_not\_a\_browser | Game is not being played in a browser, or is being played through the GX.games target |
| browser\_unknown | Unknown browser |
| browser\_ie | Internet Explorer |
| browser\_ie\_mobile | Internet Explorer on a mobile device |
| browser\_edge | Microsoft Edge |
| browser\_firefox | Mozilla Firefox |
| browser\_chrome | Google Chrome |
| browser\_safari | Safari |
| browser\_safari\_mobile | Safari on a mobile device |
| browser\_opera | Opera |
| browser\_tizen | Tizen mobile device browser |
| browser\_windows\_store | Windows App |

 

#### Example:

if (os\_browser \=\= browser\_not\_a\_browser)  

 {  

     global.Config \= 0;  

 }  

 else  

 {  

     global.Config \= 1;  

 }

The above code checks to see if the game is running in a browser or not and sets a global variable to a value depending on the result of the check.
