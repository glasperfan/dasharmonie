#import everything
from music21 import *

# support for command-line arguments
import sys

# for example, to execute the script run: "python inputmelody.py testmidi.md"
s = converter.parse(sys.argv[1])

# display in Finale (it's not going to be pretty)
s.show()