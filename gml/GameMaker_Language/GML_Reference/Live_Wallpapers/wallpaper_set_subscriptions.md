# wallpaper\_set\_subscriptions

This function subscribes to the given metric(s) from the Companion app. This is used to get real\-time system information, and enable mouse input, which is disabled for Live Wallpapers by default.

  [See this guide](https://gamemaker.io/en/help/articles/how-to-make-live-wallpapers-with-gamemaker) for making a basic Live Wallpaper and (optionally) setting up the Companion app on Windows.

  Graphics drivers must be up\-to\-date on the target computer for GPU metrics to work correctly.

  Each call to this function cancels any previously active subscriptions, so only those included in the last call remain active.

## Arguments

You pass an array into this function, containing one or more of the following strings: "desktop\_mouse", "cpu", "gpu", "battery", "ram", "disk", "network", "audio".

"desktop\_mouse" enables mouse input for your Live Wallpaper. The other options allow the [Wallpaper Subscription Data](../../../The_Asset_Editors/Object_Properties/Wallpaper_Config_Event.md#h) event to be triggered, where you receive data on the metrics you chose to subscribe to.

## Receiving Metrics

Within the [Wallpaper Subscription Data](../../../The_Asset_Editors/Object_Properties/Wallpaper_Config_Event.md#h) event you will receive updates for subscribed metrics, around once every second, except for audio which is ten times a second.

The event will contain a wallpaper\_subscription\_data variable which is a [struct](../../GML_Overview/Structs.md), containing the following members:

[wallpaper\_subscription\_data Struct](#)

- **cpu** ([Array](../../GML_Overview/Arrays.md)): Array of CPU devices. Each entry in this array is a struct, containing the following members:
	- **name** ([String](../../GML_Overview/Data_Types.md)): The name of the CPU.
	- **num\_logical\_cores** (Integer [Real](../../GML_Overview/Data_Types.md)): Number of logical cores.
	- **num\_physical\_cores** (Integer [Real](../../GML_Overview/Data_Types.md)): Number of physical cores.
	- **usage\_pct** (Integer [Real](../../GML_Overview/Data_Types.md)): The load percentage of the CPU.
	- **current\_clock\_speed\_MHz** (Integer [Real](../../GML_Overview/Data_Types.md)): The current clock speed of the CPU in MHz.
	- **max\_clock\_speed\_MHz** (Integer [Real](../../GML_Overview/Data_Types.md)): The maximum clock speed of the CPU in MHz.
	- **voltage\_V** (Integer [Real](../../GML_Overview/Data_Types.md)): The current voltage of the CPU in volts.
- **gpu** ([Array](../../GML_Overview/Arrays.md)): Array of GPU devices. Each entry in this array is a struct, containing the following members:
	- **name** ([String](../../GML_Overview/Data_Types.md)): The name of the GPU.
	- **usage\_pct** (Integer [Real](../../GML_Overview/Data_Types.md)): The load percentage of the GPU.
	- **clock\_speed\_MHz** (Integer [Real](../../GML_Overview/Data_Types.md)): The current clock speed of the GPU in MHz.
	- **fan\_speed\_pct** or **fan\_speed\_rpm** ([Array](../../GML_Overview/Arrays.md) of Integer [Real](../../GML_Overview/Data_Types.md)s): The target speed of each GPU fan. Expressed as a percentage of the maximum speed on NVIDIA GPUs and in RPM on AMD GPUs (AMD will only return one element in the array).
	- **power\_usage\_W** (Integer [Real](../../GML_Overview/Data_Types.md)): The power usage of the GPU in Watt.
	- **temperature\_C** (Integer [Real](../../GML_Overview/Data_Types.md)): The temperature of the GPU in Celsius.
	- **memory\_used\_bytes** ([String](../../GML_Overview/Data_Types.md)): How much of the GPU memory is used up in bytes.
	- **memory\_available\_bytes** ([String](../../GML_Overview/Data_Types.md)): How much of the GPU memory is available in bytes.
	- **memory\_total\_bytes** ([String](../../GML_Overview/Data_Types.md)): The total GPU memory in bytes.
- **battery** ([Array](../../GML_Overview/Arrays.md)): Array of battery devices. Each entry in this array is a struct, containing the following members:
	- **name** ([String](../../GML_Overview/Data_Types.md)): The name of the battery.
	- **is\_charging** ([Boolean](../../GML_Overview/Data_Types.md)): Indicates if the battery is charging.
	- **remaining\_charge\_pct** (Integer [Real](../../GML_Overview/Data_Types.md)): Percentage of the charge left in the battery.
	- **remaining\_time\_min** (Integer [Real](../../GML_Overview/Data_Types.md)): The estimated time left of the battery in minutes.
- **ram** ([Array](../../GML_Overview/Arrays.md)): Array of RAM devices. Each entry in this array is a struct, containing the following members:
	- **name** ([String](../../GML_Overview/Data_Types.md)): The name of the RAM.
	- **available\_bytes** ([String](../../GML_Overview/Data_Types.md)): How much of the RAM memory is available in bytes.
	- **total\_bytes** ([String](../../GML_Overview/Data_Types.md)): The total RAM memory in bytes.
	- **used\_bytes** ([String](../../GML_Overview/Data_Types.md)): How much of the GPU memory is used up in bytes.
- **disk** ([Array](../../GML_Overview/Arrays.md)): Array of disks. Each entry in this array is a struct, containing the following members:
	- **name** ([String](../../GML_Overview/Data_Types.md)): The name of the disk.
	- **available\_bytes** ([String](../../GML_Overview/Data_Types.md)): How much of the disk memory is available in bytes.
	- **total\_bytes** ([String](../../GML_Overview/Data_Types.md)): The total disk memory in bytes.
	- **used\_bytes** ([String](../../GML_Overview/Data_Types.md)): How much of the GPU memory is used up in bytes.
- **network** ([Array](../../GML_Overview/Arrays.md)): Array of network devices. Each entry in this array is a struct, containing the following members:
	- **bandwidth\_bps** ([String](../../GML_Overview/Data_Types.md)): The bandwidth of the network in bits per second.
	- **send\_bps** (Integer [Real](../../GML_Overview/Data_Types.md)): The current bytes sent per second on the network.
	- **received\_bps** (Integer [Real](../../GML_Overview/Data_Types.md)): The current bytes received per second on the network.
- **audio** ([Array](../../GML_Overview/Arrays.md)): Array of audio devices. Each entry in this array is a struct, containing the following members:
	- **freq\_resolution** (Integer [Real](../../GML_Overview/Data_Types.md)): The frequency resolution, is always 10\.
	- **spectrum\_amplitude** ([Array](../../GML_Overview/Arrays.md)): Represents a spectrum analysis of measured sound amplitudes on the system. The frequency will span from 0 Hz up to the Nyquist frequency, i.e half that of the system's sampling rate. If it is, for example, 44\.1 kHz (the most common), the frequencies will range from 0 Hz to 22050 Hz. Each bin will always represent a range of **freq\_resolution**. E.g. if it is 10, this array will consist of 2205 data points if the sampling rate is 44\.1 kHz, and 2400 if it is 48 kHz (also common).

If some information could not be retrieved from the system, its corresponding variable will not be present in this structure. That may cause a crash if you try to access a variable that doesn't exist. To prevent that, use [struct\_exists](../Variable_Functions/variable_struct_exists.md) to check that a variable exists in a struct, before accessing it.

 

 

#### Syntax:

wallpaper\_set\_subscriptions(subscriptions)

| Argument | Type | Description |
| --- | --- | --- |
| subscriptions | [Array](../../GML_Overview/Arrays.md) | An array containing strings, which are the metrics you want to subscribe to |

 

#### Returns:

N/A

 

#### Example:
