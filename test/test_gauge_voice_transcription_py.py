# test_gauge_voice_transcription_py2.py
# David Prager Branner
# 20140130

import sys
import os
sys.path.append(os.path.join('..'))
import gauge_voice_transcription_py2 as G


def test_short01():
    s1 = 'abc'
    s2 = 'abc'
    assert (1.0, 1.0, 1.0) == G.percent_matching(s1, s2)

def test_short02():
    s1 = 'abc'
    s2 = 'abc '
    assert (0.8571428571428571, 1.0, 1.0) == G.percent_matching(s1, s2)

# Begin long-string tests.

def test_long01():
    s1 = """The declines were fueled by concerns that efforts by emerging-market central banks to tighten monetary policy won't be enough to protect their economies against an exit of investor money. Although higher rates are supposed to entice investors to continue investing in emerging-market currencies, analysts said the toll the higher interest rates may take on the economic growth of those nations may be too high."""
    s2 = """The Decline 4 Fuel by concerns that efforts by emerging markets central banks to tighten monetary policy won't be enough to protect their economies against an exit of invest your money. Although higher. Rates are supposed to entice investors to continue investing in emerging markets times. These, analysts at the total. The higher interest rates may take on the economic growth of those nations. Maybe too high."""
    assert (0.9529702970297029, 
            0.8091603053435115, 
            0.8421052631578947) == G.percent_matching(s1, s2)
