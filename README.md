## Gauge Voice Transcription

**Calculate various quantitative gauges of the accuracy of voice transcription.**

---

### [Slides](http://htmlpreview.github.io/?https://github.com/brannerchinese/Gauge_Voice_Transcription/blob/master/SLIDES/branner_interfering_with_STT_slides_20140214.html) of Hack and Tell presentation

These slides may not display correctly on GitHub.com; if not, clone this repository to a regular file system and open the `html` file from there.

---

**Note** that this software is designed for use only with Python 2, at or above version 2.6. Running in other environments will fail by design, since the NLTK dependency requires Python 2.

### To run

The required arguments of the `main` function are the original string and a string containing its transcription. Output is a rounded-off value showing the percentage of the original string found intact, within some tolerance, in the transcription:

    In [1]: import gauge_voice_transcription_py2 as G
    In [2]: G.main('I would like a banana, too.', 'i would likes, the bananas chew')
    By character:       0.8
    By word:            0.3
    By normalized word: 0.7

Guide to the output:

   * **By character** compares the strings character by character, with punctuation stripped and upper- and lower-case differences eliminated. Comparing the strings by character not a good principle when well-formed whole English words are expected to be in the second string, which is usually the case with voice transcription output.
   * **By word** compares arrays of whole words, with punctuation stripped and upper- and lower-case differences eliminated.
   * **By normalized word** is just like "by word", but with additional normalization of most nouns and verbs to their "lemma" (morphologically neutral dictionary-headword) forms, and with most contractions expanded (_can't_ => _cannot_, _won't_ => _will not_, etc.). 

"By normalized word" is the most useful option if one wants to ignore minor differences in morphology, such as _likes_ for _like_ and _bananas_ for _banana_.

By default, results are rounded to a single decimal place. For other precision, use a third argument `places`:

    In [4]: G.main('I would like a banana, too.', 'i would likes, the bananas chew', places=2)
    By character:       0.76
    By word:            0.33
    By normalized word: 0.67

The unrounded results are returned by the `percent_matching` function:

    In [5]: G.percent_matching('I would like a banana, too.', 'i would likes, the bananas chew')
    Out[6]: (0.7636363636363637, 0.3333333333333333, 0.6666666666666666)

### Testing

There is a rudimentary test suite in `test`, intended for use with `pytest`. To run:

    $ pip install pytest
    $ py.test test

### Algorithm

The algorithm used was described as ["the gestalt approach"](http://www.drdobbs.com/database/pattern-matching-the-gestalt-approach/database/pattern-matching-the-gestalt-approach/184407970?pgno=5) to pattern-matching in the 1988 article introducing it, in an assembly-language implementation. Dating to 1983, it was intended for use in educational software, for automating the checking of student responses on exams; it was also used in early spell-checkers. Known as the Ratcliff/Obershelp pattern-matching algorithm, it is implemented as `difflib.SequenceMatcher` in the Python standard library, with cubic worst-case time complexity.

The original algorithm is designed for comparing two strings of characters. Here, I am interested in comparison not of strings but of arrays, and want to measure not single-character differences but the matching of whole, well-formed words in standard English (the usual output of voice-transcription software). But `difflib.SequenceMatcher` is able to operate on arrays of indivisible elements.

---

### Still to be done

 * Times of day (08:30, e.g.) occasionally appear in Google Voice transcriptions and need to be handled. This will require adding the numbers 11 to 59 to `digit2word`.

[end]
