# test_gauge_voice_transcription_py2.py
# David Prager Branner
# 20140130

import pytest
import gauge_voice_transcription_py2 as G

def simple01():
    s1 = 'abc'
    s2 = 'abc'
    assert 1.0, 1.0, 1.0 == G.percent_matching(s1, s2)


