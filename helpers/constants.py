# constants.py

###################################
### TO DEFINE PROGRAM CONSTANTS ###
###################################

## DEBUG SWITCH ##
DEBUG = True


# Some functions operate on the knowledge of diatonic or not.
# For know we are assuming that is true.
#DIATONIC = True

DEFAULT_TIME_SIGNATURE = 4

# The smallest length of segements in the harmonic analysis.
# 1 represents a full measure, 0.5 a half measure, 
# 2 is 2 measures, etc. 
SEGMENT_LENGTH = 1

# maximum number of beats (in quarter-lengths)
MAX_DURATION = 8


### PITCH PROGRESSIONS ###

# In order of descending strength:
# The float in parentheses corresponds to the
# "strength" of the progression. The higher the
# rating, the more confidence there is that this
# scale is indeed the appropriate one. 

# Essentially certain #
# All 1,1	All 7,1		All 2,1
# All 5,1	All 4,3
# For example, "'B', 'A', 'G'" (3,2,1) will always return G major
PPC_PROBABILITY = 0.5

# High #
pitch_progression_high = [[1,2,3],[1,1,3],[1,3,5],[5,1,3],[4,2,3]]
PPH_PROBABILITY = 0.4

# Medium #
pitch_progression_medium = [[3,4,5],[1,1,5],[5,6,5],[2,5,3],[3,5,3],[6,5,3]]
PPM_PROBABILITY = 0.3

# Low #
# Also includes all progression with last == 1 and second != 1,2,5,7
pitch_progression_low = [[5,2,3],[7,1,5],[1,6,5]]
PPL_PROBABILITY = 0.2

# Not Found (0.1) #
PPN_PROBABILITY = 0.1





