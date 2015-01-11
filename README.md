Das-Harmonie
===========

A Python attempt at _supervised_, automatic melodic harmonization.

**Demonstration available here:** https://www.youtube.com/watch?v=fq1XNULCcSw

In order to take advantage of the full power of Das-Harmonie, you should download the following software:

1. Music21 (https://code.google.com/p/music21/downloads/list)

2. LilyPond (http://www.lilypond.org)

3. Finale NotePad (available free at http://www.finalemusic.com/products/finale-notepad/resources)


**INSTRUCTIONS FOR INSTALLATION**

1. Parts of this program depend on the open-source Music21 library for converting files. Download and install Music21 at https://code.google.com/p/music21/downloads/list. Follow the instructions to properly configure the library. Music21 should be installed globally.

2. Get the files for das-harmonie from GitHub (git clone).

3. You should now have a folder titled "das-harmonie." Move into the parent directory ("cd ..").

4. Run the program with code like this!
```
>>> python das-harmonie inputfile.xml -B --mus
```

**Options**
-----------


**Arguments**

1. das-harmonie
2. _name_ of file containing melody
3. _style_ of accompaniment
4. _format_ of output score



**Accepted file types**

1. 'xml'
2. 'mxl'
3. 'abc' --> only used in music21 corpus: http://web.mit.edu/music21/doc/systemReference/referenceCorpus.html




Code          | Style of accompaniment
------------- | ----------------------
-B            | Block chords
-A            | Arppegiated chords




Code       | Possible output formats
-----------| -------------------------------------
--mus      | Returned as a score in Finale NotePad
--pdf      | PDF Document (requires LilyPond - see above)
--lily.pdf | PDF Document (same functionality as --pdf)
--lily     | PNG file (also requires LilyPond)
--text     | Prints the output to the terminal in music21 notation
--debug    | Can be used to turn on debug functionality. Will _not_ print a score.





VERSIONS
========

Version 1.0
Created as a final project for Harvard's CS51 course.


Version 2.0
Intended to simplify an overly complicated program but simulataneously increase its functionality. 

_ENTIRELY_ restructured codebase, algorithms, and use methods.

However, simplicity is emphasized. To keep it simple, maintainable, and Pythonic, I strive to avoid redundant or
trivial functionality.


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
