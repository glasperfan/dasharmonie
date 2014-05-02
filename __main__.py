#__main__.py
# This is the main module for analysis. It is executed directly.

import sys
import subprocess
import os
import music21
import libraries.tools as T
import libraries.harmony as H
from libraries.constants import *

'''

Necessary arguments:
sys.argv[1] ---> MusicXML file containing a melody
	Options: all musicXML files 
sys.argv[2] ---> Style of accompaniment
	Options: -B, -A
sys.argv[3] ---> Format of output
	Options: --mus, --pdf, --xml, --midi, --lily, --text, --debug
	Note: --debug turns debug mode on for the current session.

Requirements
1) File must be of MusicXML format.
2) The parsed score must contain a melody line.
3) The parsed score must contain a time signature.
4) The time signature must be a recognized one (either 3/4 or 4/4).
5) The parsed score must be entirely diatonic. 
6) The specified style must be a valid one.

'''

# Works from music21 corpus can be files of any of these types.
# User files should all be .xml format.
accepted_extensions = ['.xml', '.mxl', '.abc']
 
# Currently, only melodies with these time signatures function correctly.
accepted_timeSignatures = ['3/4', '4/4', '2/2', '6/8', '2/4']

# Currently accepted styles of accompaniment. 
#'-B' = block chords, '-A' = arppegiated
accepted_styles = ['-B', '-A']

# Accepted methods of output.
# Note: these will all display once the program has run.
accepted_output_methods = ['--pdf', '--mus', '--xml', '--lily', '--text', '--debug']

def basicVerify():
	if len(sys.argv) == 4:
  		return True
	else:
  		raise Exception ("Error (0): there are missing arguments.")

def verifyFile():
	try:
		f = sys.argv[1]
		fileName, fileExtension = os.path.splitext(f)
	except:
		raise Exception ("Error (1): cannot verify input file extension.")
	try:
		l = os.listdir("das-harmonie/melodies")
		x = l.index(f)
	except:
		res = music21.corpus.getWork(fileName)
		if len(res) > 0:
			s = music21.corpus.parse(res)
			print "File verified."
			#s.show('lily.pdf')
			return s
		else:
			raise Exception ("Error (3): cannot parse file.")
	try:
		s = music21.converter.parse("das-harmonie/melodies/" + f)
		print "File verified."
		#s.show('lily.pdf')
		return s
	except:
		raise Exception ("Error (3): cannot parse file.")

def verifyScore(s):
	# verify time signature
	try:
		time = s.flat.getElementsByClass(music21.meter.TimeSignature)[0]
		accepted_timeSignatures.index(time.ratioString)
		return True
	except:
		raise Exception ("Error (4): time signature not recognized.")
	# verify score is diatonic
	try:
		ms = H.getMeasures(s)
		ns = [] 
		for m in ms:
			ns.extend(H.getPitches(m))
		note_set = T.listScale(T.toPitchClasses(T.listSet(ns)))
		if len(note_set.scale) > 7:
			raise Exception ("Error (5): melody is not recognized as diatonic.")
		print "Score verified."
		return True
	except:
		raise Exception ("Error (6): unable to access notes.")

def verifyStyle():
	#verify style (specified via command-line)
	try:
		style = sys.argv[2]
		x = accepted_styles.index(style)
		print "Style verfied."
		return True
	except:
		raise Exception ("Error (7): invalid style specified.")

def verifyOutputMethod():
	try:
		om = sys.argv[3]
		x = accepted_output_methods.index(om)
		print "Output method verified."
		return True
	except:
		raise Exception ("Error (8): invalid output method.")

def verify():
	print "Verifying..."
	basic = basicVerify()
	s = verifyFile()
	allGood = basic and verifyScore(s) and verifyStyle() and verifyOutputMethod()
	if allGood:
		return s

def runDasHarmonie():
	sys.tracebacklimit = 0 # hides traceback stdout 
	DEBUG = False
	om = sys.argv[3]
	if om == '--debug':
		DEBUG = True
	s = verify()
	res = T.keyAndTonic(s)
	print res
	chords = H.runAnalysis(s)
	output = s #GENERATE ACCOMPANIMENT
	if om == '--mus':
		output.show()
	elif om == '--pdf':
		output.show('lily.pdf')
	elif om == '--xml':
		output.show('musicxml')
	elif om == '--lily':
		output.show('lily')
	elif om == '--text':
		output.show('text')
	elif om == '--debug':
		assert DEBUG == True
	else:
		# default
		output.show('lily.pdf')

def run():
	runDasHarmonie()


run()