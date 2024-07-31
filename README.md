
# py-kcs - Encode/Decode Kansas City Standard Audio Cassette Data

Original Author: David Beazley (http://www.dabeaz.com)
Copyright (C) 2010

Updated 2022: Greg Strike (www.gregorystrike.com)


This is free software. You are free to use it however you wish, but if you
decide to include it in some other package, please give me some credit.

## Overview
This package provides a pair of scripts, kcs_encode.py and kcs_decode.py
that encode and decode WAV audio files containing data encoded in the
Kansas City Standard as used on some of the first home computers.  In my
case, an Ohio Scientific Superboard II from 1978.  For more information
on KCS encoding, see http://en.wikipedia.org/wiki/Kansas_City_standard

## Usage
First of all, you need to install Python-3.1.2 or newer on your system.

To encode a text file into a WAV file suitable for playback, do this:

    % python3 kcs_encode.py input.txt output.wav

This reads the file 'input.txt' and writes a WAV file 'output.wav'. The
resulting WAV file is encoded in mono with a framerate of 9600 Hz.


To decode a WAV file containing KCS data that you have recorded, do
this:

    % python3 kcs_decode.py input.wav

Decoded text contained in the WAV file will be printed to standard
output. To save the output to a file instead, type this:

    % python3 kcs_decode.py input.wav > output.txt

### About input wave files 

* The decoding script only suports .wav files encoded in PCM.
Other WAV file formats (such as compressed ones) won't work.
* Please make sure that the audio track starts with the leading tone and ends 
with the trailing tone, otherwise extra bytes will be added to the output.
* The decoding script will only process the left audio channel.
* The script seems to work decently well with audio files containing moderate
white noise. If the audio is extremely noisy you could use an audio application
such as Audacity to clean it up. Audacity's noise reduction or equalization
around the 1.2 KHz and 2.4 KHz frequencies can help with this.


## Space Considerations

Each byte in the payload is encoded into a 11 bits frame.
The Kansas City Standard encodes information at 300 bauds (bits per second).
That means that the output audio will have a duration of 0,036666667 seconds
per payload byte.
The encoding script also adds a 5s. leading tone and a 5s. trailing tone.
As a reference, a 90 min. cassette tape can hold 143,55 kB in each side.


## More Information
See the following blog posts for more information:

http://dabeaz.blogspot.com/2010/08/using-python-to-encode-cassette.html
http://dabeaz.blogspot.com/2010/08/decoding-superboard-ii-cassette-audio.html
https://www.gregorystrike.com/2023/01/07/kansas-city-standard-decoder/

Installation Notes
-------------------
The kcs_encode.py and kcs_decode.py are standalone programs that
should work with any Python 3 installation (version 3.1.2 or newer).
If you decide to install the scripts, they are simply placed
in the Python scripts directory.

Feedback
--------
This is just a fun personal project for me. If you use these scripts
for a vintage computing project, send me email (dave@dabeaz.com) and
let me know about it.  --Dave
