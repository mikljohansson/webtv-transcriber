#!/usr/bin/env python
#
# sudo pip install mutagen
#
import os, sys, math
from mutagen.mp3 import MP3

def audiotracks(path):
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            audiotrack = os.path.join(dirpath, filename)
            if audiotrack.endswith('.mp3'):
                yield audiotrack

filesize = 0
length = 0.0
count = 0

for audiotrack in audiotracks(sys.argv[1]):
	audio = MP3(audiotrack)
	filesize += os.path.getsize(audiotrack)
	length += audio.info.length
	count += 1

print "%d tracks, total length %dh:%dm, size on disk %dMb" % (count, math.floor(length / 60 / 60), math.ceil(length / 60 % 60), filesize / 1024 / 1024)
