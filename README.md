dasharmonie
===========

A Python attempt at automatic melodic harmonization.


**INSTRUCTIONS FOR INSTALLATION**

1. Parts of this program depend on the open-source Music21 library for converting files. Download and install Music21 at https://code.google.com/p/music21/downloads/list. Follow the instructions to properly configure the library. Music21 should be installed globally.
2. Get the files for das-harmonie from GitHub (git clone).
3. You should now have a folder titled "das-harmonie." Move into the parent directory ("cd ..").
4. Run the program with code like this!
```
>>> python das-harmonie inputfile.xml -B --mus
```

**OPTIONS**

Code          | Style of accompaniment
------------- | ----------------------
-B            | Block chords
-A            | Arppegiated chords
