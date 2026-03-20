# AudioLFOType Enum

This built\-in enum contains the possible LFO types to select when using an [audio effect](Audio_Effects.md) that is *modulated by* an LFO.

LFO stands for [Low\-Frequency Oscillation](https://en.wikipedia.org/wiki/Low-frequency_oscillation). Similarly, the thing that *oscillates*, i.e. goes up and down according to a certain shape, is called a Low\-Frequency Oscillator. An LFO outputs a shape that repeats indefinitely; the shape is *periodic* (after a certain *period* the same shape returns)

In audio processing an LFO is used to *modulate* audio effect parameters at *audio rates* (as opposed to game\-frame rates)

You could do this yourself through code, e.g. change the [gain](../audio_sound_gain.md) value of sound instances, but this will only happen as many times per second as the game speed that you set (see [game\_set\_speed](../../../General_Game_Control/game_set_speed.md)). If e.g. the game speed is set to 60 then an update will happen 60 times per second.

On the other hand, the audio that GameMaker plays has a much higher frequency (e.g. 44100, 48000, etc.). This means that a sample is played 44100 times a second or 48000 times a second. An LFO updates the parameter with every sample that is played instead of only a couple of times per second.

  An LFO outputs a signal at a low frequency (0\-20Hz) but calculates/updates the value at a high frequency (the audio's frequency, e.g. 44100 or 48000\).

GameMaker has a few built\-in Audio LFO types (or shapes): 

Audio LFO Types/Shapes

| Sine | Square | Triangle | Sawtooth | Inverse Sawtooth |
| --- | --- | --- | --- | --- |
| AudioLFOType.Sine | AudioLFOType.Square | AudioLFOType.Triangle | AudioLFOType.Sawtooth | AudioLFOType.InvSawtooth |
|  |  |  |  |  |

## AudioLFOType.InvSawtooth

This LFO type outputs an inverse sawtooth shape. The shape looks like this: 

## AudioLFOType.Sawtooth

This LFO type outputs a sawtooth shape. The shape looks like this: 

## AudioLFOType.Sine

This LFO type outputs a sine shape ([sin](../../../Maths_And_Numbers/Angles_And_Distance/sin.md)). The shape looks like this: 

## AudioLFOType.Square

This LFO type outputs a square shape. The shape looks like this: 

## AudioLFOType.Triangle

This LFO type outputs a triangle shape. The shape looks like this:
