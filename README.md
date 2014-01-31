## Gauge_Voice_Transcription

**Calculate various quantitative gauges of the accuracy of voice transcription.**

---

**Note** that this software is designed for use only with Python 2, at or above version 2.6. Running in other environments will fail by design, since the NLTK dependency requires Python 2.

### To run

The required arguments of the `main` function are the original string and a string containing its transcription. Output is a rounded-off value showing the percentage of the original string found intact, within some tolerance, in the transcription:

    In [1]: import gauge_voice_transcription_py2 as G
    In [2]: G.main('This is right.', 'this is almost right')
    By character:       0.8
    By word:            0.9
    By normalized word: 0.9

Guide to the output:

   * **By character** compares the strings character by character, with punctuation stripped and upper- and lower-case differences eliminated. Comparing the strings by character not a good principle when well-formed whole English words are expected to be in the second string, which is usually the case with voice transcription output.
   * **By word** compares arrays of whole words, with punctuation stripped and upper- and lower-case differences eliminated.
   * **By normalized word** is just like "by word", but with additional normalization of most nouns and verbs to their "lemma" (morphologically neutral dictionary-headword) forms, and with most contractions expanded (_can't_ => _cannot_, _won't_ => _will not_, etc.). 

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

The algorithm used was described as ["the gestalt approach"](http://www.drdobbs.com/database/pattern-matching-the-gestalt-approach/database/pattern-matching-the-gestalt-approach/184407970?pgno=5) to pattern matching in the 1988 article introducing it, in an assembly-language implementation. Dating to 1983, it was intended for use in educational software, for automating the checking of student responses on exams. Known as the Ratcliff/Obershelp pattern matching algorithm, it is implemented as `difflib.SequenceMatcher` in the Python standard library, with cubic worst-case time complexity.

The original algorithm is designed for comparing two strings of characters. Here, I am interested in comparison not of strings but of arrays, and want to measure not single-character differences but the matching of whole, well-formed words in standard English (the usual output of voice-transcription software). So I have introduced a hack to adapt `difflib.SequenceMatcher` to compare arrays, whole element by whole element.
 
The hack is as follows:

 1. given two arrays of words as input,
 1. construct a set of all words occurring in either array;
 1. construct a dictionary: pair each unique word in the set to a unique but arbitrary character: `{word: character}`;
 1. convert each source array to a string of single characters, one word to one character, based on the contents of the dictionary.

This hack allows `difflib.SequenceMatcher` to operate on arrays of indivisible elements.

---

This project is in mid-process.

Still to do: 

 1. Convert phone calls to MP3.
 2. Decide about inclusion of tolerance information.
 1. Prepare slides for presentation.

[end]
