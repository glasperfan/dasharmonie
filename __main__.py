#__main__.py
# This is the main module for analysis. It is executed directly.

import sys
# import subprocess
# import os

'''

TODO: move this to README.md 



VERSION 2.0

The new version of Das Harmonie is intended to simplify an overly complicated program but simulataneously increase its functionality. 

The objective is straightforward:
1) Accept an input file, in one of a variety of formats. (That is, anything that can be parsed by music21.)
2) Validations
	a) Valid arguments
		i) Invalid arguments --> fault; exit 
	b) Recognizable format
		i) Unable to parse --> fault; exit
	c) One melody line required.
		i) Multiple melody lines --> ask user to choose one of them
		ii) No melody line --> fault; exit
	d) Time signature must be valid.
		i) invalid time signature (per music21) --> fault; exit
		ii) no time signature --> fault; exit
		iii) no time signature at measure 1 --> fault; exit
	e) Key signature must be within 7 flats or 7 sharps
		i) Greater than 7 flats or sharps --> fault; exit
3) Either choose the key signature given, or analyze the melody to determine an appropriate one.
	a) Completely diatonic (either one key or multiple) --> choose diatonic chord set
	b) Non-diatonic --> break down by measure (this is the tough part)
4) Develop chord progressions. Choose locations for cadences. This is the most difficult part to implement.
5) Build the score using music21 objects. Options for accompaniment style include block chords and arpeggio.


Additional features:
1) To allow for user configuration during use, the main harmonization tools will reside in harmony.py.
Users will be able to configure items such as defaults for style, key signature analysis, strength of chord tendencies, etc. from
the config.py file.
2) Thus, das-harmonie will be able to run standalone:
		>>> python das-harmonie FILENAME -b --pdf
   Or as an interactive element.
   		$ python
   		Python 2.7.....
   		>>> from das-harmonie import *
   		>>> config.setOutputFormat('pdf')
   		>>> harmony.harmonize('melody1.xml')
   		Amazing things happen....
3) Debug will be fully implemented. --debug. Will actually generate print statements.
4) Info will be implemented to allow users to see how the program is working.
5) Better system of constants. This is to be determined....


Version 2.1
New functionality for 'genres' of accompaniment (classical, jazz).
Implement bestTimeSignature for scores without time signatures. V2.0 currently rejects them.
Implement smart checking of command-line arguments.


Version 2.2
Add new accompaniment forms (string quartet, guitar, cello).


'''


#-----------------------------------------------------------
# Here, Das-Harmonie is being run standalone.

# parse arguments


