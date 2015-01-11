# include music21 library
from music21 import *

# corpus is the library of stored musicXML files that we can work with
# if we had used "import music21 instead" this would have been music21.corpus.parse
s = corpus.parse('bach/bwv65.2.xml')

# show the parsed musicXML in Finale NotePad by default
s.show()

# shows the parsed musicXML in LilyPond (downloaded online)
#s.show('lily.pdf')

