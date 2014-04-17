from music21 import *
import sys

s = converter.parse(sys.argv[1])

s.show('text')

print s.Part

