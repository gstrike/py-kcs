py-kcs - Encode/Decode Kansas City Standard Audio Cassette Data

Author: David Beazley (http://www.dabeaz.com)
Copyright (C) 2010

This is free software. You are free to use it however you wish, but if you
decide to include it in some other package, please give me some credit.

Overview
--------
This package provides a pair of scripts, kcs_encode.py and kcs_decode.py
that encode and decode WAV audio files containing data encoded in the
Kansas City Standard as used on some of the first home computers.  In my
case, an Ohio Scientific Superboard II from 1978.  For more information
on KCS encoding, see http://en.wikipedia.org/wiki/Kansas_City_standard

Usage
-----
First of all, you need to install Python-3.1.2 or newer on your system.

To encode a text file into a WAV file suitable for playback, do this:

    % python3 kcs_encode.py input.txt output.wav

This reads the file 'input.txt' and writes a WAV file 'output.wav'. The
resulting WAV file is encoded in mono with a framerate of 9600 Hz.

To decode a WAV file containing KCS data that you have recorded, do
this:

    % python3 kcs_decode.py input.wav

Decoded text contained in the WAV file will be printed to standard
output.  This decoding process will strip NULL bytes and convert 
line endings to the native line endings for your platform.

If you want to decode raw binary data, type this:

    % python3 kcs_decode.py -b input.wav

In this case, output is still directed to standard output, but
is exactly as found in the audio (including all NULL bytes).

More Information
----------------
See the following blog posts for more information:

http://dabeaz.blogspot.com/2010/08/using-python-to-encode-cassette.html
http://dabeaz.blogspot.com/2010/08/decoding-superboard-ii-cassette-audio.html

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




