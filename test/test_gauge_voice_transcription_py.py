#!/usr/bin/python
# -*- coding: utf-8 -*-

# test_gauge_voice_transcription_py2.py
# David Prager Branner
# 20140131, works

import sys
import os
sys.path.append(os.path.join('..'))
import gauge_voice_transcription_py2 as G
import re


def test_short01():
    s1 = 'abc'
    s2 = 'abc'
    assert G.percent_matching(s1, s2) == (1.0, 1.0, 1.0)

def test_short02():
    s1 = 'abc'
    s2 = 'abc '
    assert G.percent_matching(s1, s2) == (0.8571428571428571, 1.0, 1.0)

# Begin long-string tests.

def test_long01():
    s1 = u"""The declines were fueled by concerns that efforts by emerging-market central banks to tighten monetary policy won't be enough to protect their economies against an exit of investor money. Although higher rates are supposed to entice investors to continue investing in emerging-market currencies, analysts said the toll the higher interest rates may take on the economic growth of those nations may be too high."""
    s2 = u"""The Decline 4 Fuel by concerns that efforts by emerging markets central banks to tighten monetary policy won't be enough to protect their economies against an exit of invest your money. Although higher. Rates are supposed to entice investors to continue investing in emerging markets times. These, analysts at the total. The higher interest rates may take on the economic growth of those nations. Maybe too high."""
    assert G.percent_matching(s1, s2) == (
            0.9529702970297029, 0.8091603053435115, 0.8421052631578947)

def test_long02():
    s1 = u"""'''Vladimir Iosifovich Levenshtein''' ({{lang-ru|Владимир Иосифович Левенште́йн}} born [[1935]]) is a [[Russia]]n scientist who did research in [[information theory]] and [[error-correcting code]]s. Among other contributions, he is known for the [[Levenshtein distance]] algorithm, which he developed in 1965."""
    s2 = u"""'''Vladimir Iosifovich Levenshtein''' ({{lang-ru|Влади́мир Ио́сифович Левенште́йн}}; born 1935) is a [[Russia]]n scientist who has done research in [[information theory]], [[error-correcting code]]s, and [[combinatorial design]]. Among other contributions, he is known for the [[Levenshtein distance]] and a Levenshtein algorithm, which he developed in 1965."""
    assert G.percent_matching(s1, s2) == (
            0.8939393939393939, 0.868421052631579, 0.8947368421052632)

def test_long03():
    s1 = u"""The '''Great Dinky Robbery''' was a prank perpetrated by four [[Princeton University]] students on Friday, May 3, 1963.<ref>{{cite news |first=J. D. |last=Reed |title=The Little Engine That Can |url=http://query.nytimes.com/gst/fullpage.html?res=9900E1D9103BF932A05750C0A9649C8B63&sec=&spon=&pagewanted=4 |work=New York Times |date=March 31, 2002 |accessdate=2007-12-12 }}</ref> The Dinky referred to is the Princeton Branch service operated at the time by the [[Pennsylvania Railroad]], usually a one-car train. At the time, Princeton was an all-male school, so the Dinky was the primary means of transportation for women coming to the campus to meet their dates."""
    s2 = u"""The '''Great Dinky Robbery''' was a prank perpetrated by four [[Princeton University]] students on Friday, May 3, 1963.<ref>{{cite news |first=J. D. |last=Reed |title=The Little Engine That Can |url=http://query.nytimes.com/gst/fullpage.html?res=9900E1D9103BF932A05750C0A9649C8B63&sec=&spon=&pagewanted=4 |work=New York Times |date=March 31, 2002 |accessdate=2007-12-12 }}</ref> At the time, Princeton was an all-male school and the Dinky was the primary means of transportation for women coming to the campus to meet their dates. In the "Robbery", four students on horseback [[ambush]]ed the train as it was arriving in the [[Princeton Junction (NJT station)|Princeton Junction station]]. A convertible was parked across the track forcing the Dinky to come to an abrupt halt. At that point, the ersatz cowboys rode up to the Dinky, and, led by George Bunn '63 who was armed with a pistol loaded with blanks, boarded and seized four girls selected on the spot. The riders and their newly found dates rode off on the horses, the convertible was moved off the tracks, and the Dinky arrived safely, albeit a few minutes late. Although the University administrators were aware of the event and knew who was involved, they took no official action against them."""
    assert G.percent_matching(s1, s2) == (
            0.5297787861599547, 0.45925925925925926, 0.45925925925925926)
