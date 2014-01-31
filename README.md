## Gauge_Voice_Transcription

Calculate various quantitative gauges of the accuracy of voice transcription.

This project is in mid-process.

---

### To run

 Note that this software is designed for use only with Python 2, at or above version 2.6. Running in other environments will fail by design, since the NLTK dependency requires Python 2.
 
 The required arguments of the `main` function are the original string and a string containing its transcription. Output is a rounded-off value showing the percentage of the original string found intact, within some tolerance, in the transcription:

    In [1]: import gauge_voice_transcription_py2 as G
    In [2]: G.main('This is right.', 'this is almost right')
    By character:       0.8
    By word:            0.9
    By normalized word: 0.9

Guide to the output:

   * **By character** compares the strings character by character, with punctuation stripped and case differences eliminated. Comparing the strings by character not a good principle when well-formed whole English words are expected to be in the second string, which is usually the case with voice transcription output.
   * **By word** compares arrays of whole words, with punctuation stripped and case differences eliminated.
   * **By normalized word** is like "by word", but with additional normalization of nouns and verbs to their "lemma" (morphologically neutral dictionary-headword) forms, and with most contractions expanded (_can't_ => _cannot_, _won't_ => _will not_, etc.). 

"By normalized word" is the most useful option if one wants to ignore minor differences in grammar:

    In [3]: G.main('This is right.', 'this be almost right')
    By character:       0.7
    By word:            0.6
    By normalized word: 0.9

By default, results are rounded to a single decimal place. For other precision, use a third argument `places`:

    In [4]: G.main('This is right.', 'this be almost right', places=2)
    By character:       0.73
    By word:            0.57
    By normalized word: 0.86

The unrounded results are returned by the `percent_matching` function:

    In [5]: G.percent_matching('This is right.', 'this be almost right')
    Out[6]: (0.7272727272727273, 0.5714285714285714, 0.8571428571428571)

### Testing

There is a rudimentary test suite in `test`, intended for use with `pytest`. To run:

    $ pip install pytest
    $ py.test test

### Algorithm

The algorithm used was described as ["the gestalt approach"](http://www.drdobbs.com/database/pattern-matching-the-gestalt-approach/database/pattern-matching-the-gestalt-approach/184407970?pgno=5) to pattern matching in the 1988 article introducing it, in an assembly-language implementation. Known as the Ratcliff/Obershelp pattern matching algorithm, it is implemented as `difflib.SequenceMatcher` in the Python standard library, with cubic worst-case time complexity.

The original algorithm is designed for comparing two strings of characters. Here, since I am interested in comparing not fine-grained strings but arrays of well-formed standard English words (the usual output of voice-transcription software), I have introduced a hack to adapt `difflib.SequenceMatcher` to compare arrays, whole element by whole element.
 
Discussion forthcoming.

[end]
