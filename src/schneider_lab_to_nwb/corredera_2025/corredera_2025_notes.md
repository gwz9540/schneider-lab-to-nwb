# Notes concerning the corredera_2025 conversion

## Behavior
- Lots of relevant variables in the .mat files
- Based on the SfN poster, it looks like there are at least 4 different types of sessions:
    1. 60 min exploration on leaves/rubber (top left)
    2. exploration on VR environment (bottom left)
    3. 3-set session with self-generated playback (middle)
    4. exploration with Loom threat (right)
shared data looks like session type 1.
- visual stimulus should be stored as a pynwb.image.OpticalSeries

## Video

## Ephys
- brain region = left auditory cortex
- For channel positions, see CN_ASSY236_P1_kilosortChanMap.mat
- Recording Probe = 64-channel P1 probes from Cambridge Neurotech (ASSY-236)
- WhiteMatter logger = eCube?

## Sleap
- Output file not loading in sleap interface for some reason -- missing 'tracks_json'...

## Audio
- Might want to switch to ndx-sound --> then add link for microphones and speakers
- .wav style compression?
- Are the microphones at different spots around the square arena? Which is where?


## Temporal Alignment
- Timestamps in the .mat file are relevant for temporal alignment

## Active Questions/Requests
