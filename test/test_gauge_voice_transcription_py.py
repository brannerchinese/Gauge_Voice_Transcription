# test_gauge_voice_transcription_py2.py
# David Prager Branner
# 20140130

import pytest
import gauge_voice_transcription_py2 as G

s1 = 'abc'

def simple01():
    s2 = 'abc'
    assert (1.0, 1.0, 1.0) == G.percent_matching(s1, s2)

def simple02():
    s2 = 'abc '
    assert (0.8571428571428571, 1.0, 1.0) == G.percent_matching(s1, s2)
