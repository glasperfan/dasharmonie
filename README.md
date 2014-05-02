Das-Harmonie
===========

A Python attempt at _supervised_, automatic melodic harmonization.

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

**OPTIONS**

Argument 1: das-harmonie
Argument 2: _name_ of file containing melody
Argument 3: _style_ of accompaniment
Argument 4: _format_ of output score

Accepted file types:
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
