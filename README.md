Das-Harmonie
===========

A Python attempt at _supervised_, automatic melodic harmonization.

**Demonstration available here:** https://www.youtube.com/watch?v=fq1XNULCcSw


**VERSION 2.0 CURRENTLY IN DEVELOPMENT**...stay tuned! :)

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
