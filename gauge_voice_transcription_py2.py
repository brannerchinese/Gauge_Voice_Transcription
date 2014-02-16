# gauge_voice_transcription_py2.py
# 20140215, working.
# David Prager Branner

"""Return quantitative gauges of the accuracy of voice transcription."""

import sys
# Ensure Python version 2.6 or above, because of NTLK.
if sys.version_info[0] != 2 or sys.version_info[1] < 6:
    print("This program requires Python 2, versions 2.6 or above.")
    sys.exit(1)
import re
import difflib
import nltk


def main(orig, transcr, places=1):
    if not (orig or transcr):
        print 'Cannot run with empty input strings. Exiting.'
        sys.exit(1)
    gauge_raw, gauge_word, gauge_lemma = percent_matching(orig, transcr)
    print ('''By character:       {}\nBy word:            {}'''
            '''\nBy normalized word: {}'''.format(
            round(gauge_raw, places), 
            round(gauge_word, places), 
            round(gauge_lemma, places)))

# Global variables.
# Treebank and WordNet POS need correspondences specified in order for the
# NLTK lemmatizer to work correctly on the tagged output. Only the following
# five have application, however.
TB2WN = {
    'J': nltk.wordnet.wordnet.ADJ,
    'R': nltk.wordnet.wordnet.ADV,
    'N': nltk.wordnet.wordnet.NOUN,
    'V': nltk.wordnet.wordnet.VERB,
    'S': nltk.wordnet.wordnet.ADJ_SAT
    }
WNL = nltk.stem.WordNetLemmatizer()
# Replace numerals with equivalent words.
# Attested: 3rd; 25 for 'too high', must mean 'two five'.
# Unknown whether we will actually encounter 11, 12th, 0th.
digit2word = { '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '0th': 'zeroth',
        '1st': 'first',
        '2nd': 'second',
        '3rd': 'third',
        '4th': 'fourth',
        '5th': 'fifth',
        '6th': 'sixth',
        '7th': 'seventh',
        '8th': 'eighth',
        '9th': 'ninth',
        '10th': 'tenth',
        }


def percent_matching(orig, transcr):
    """Compare the likeness of two input strings."""
    #
    # Case 1. Simple case: strings are compared character by character.
    #
    # Strip punctuation and lower-case all words
    orig_cleaned = re.sub(r'[^\w\s]', '', orig.lower())
    transcr_cleaned = re.sub(r'[^\w\s]', '', transcr.lower())
    #
    # Instantiate a SequenceMatcher and compute the ratio of common content.
    gauge_raw = difflib.SequenceMatcher(
            None, orig_cleaned, transcr_cleaned, autojunk=False).ratio()
    #
    # Case 2. Case of whole words rather than characters.
    #
    orig_words = orig_cleaned.split()
    transcr_words = transcr_cleaned.split()
    #
    # Instantiate a SequenceMatcher and compute the ratio of common content.
    gauge_word = difflib.SequenceMatcher(
            None, orig_words, transcr_words, autojunk=False).ratio()
    #
    # Case 3. Case of normalized whole words.
    #
    # Normalize each word via NLTK and create additional pair of strings.
    orig_norm = clean_and_normalize(orig)
    transcr_norm = clean_and_normalize(transcr)
    #
    # Instantiate a SequenceMatcher and compute the ratio of common content.
    gauge_lemma = difflib.SequenceMatcher(
            None, orig_norm, transcr_norm, autojunk=False).ratio()
    #
    return (gauge_raw, gauge_word, gauge_lemma)

def clean_and_normalize(the_str):
    """Return all-downcase, unpunctuated, lemmatized list of words in string."""
    # Annoyingly, nltk.word_tokenize does not handle contractions well.
    # The substitutions below are best guesses; some will occasionally be wrong.
    # In particular, 's is not handled at all here, since it includes
    # possessive and the contraction of is and has: "Tom's" could be "belonging
    # to Tom", "Tom is", or "Tom has".
    the_str = the_str.lower()
    the_str = re.sub(r"won't", 'will not', the_str)
    the_str = re.sub(r"can't", 'cannot', the_str)
    the_str = re.sub(r"it's", 'it is', the_str)
    substitutions = {r"'ll": ' will',
            r"n't": ' not',
            r"'m": ' am',
            r"'d": ' would',
            r"'ve": ' have',
            r"'re": ' are',
            r"'ve": ' have',
            r"wanna": 'want to',
            r"anymore": 'any more',
            r"gonna": 'going to',
            }
    for s in substitutions:
        the_str = re.sub(s, substitutions[s], the_str)
    # Remove all other punctuation and normalize.
    the_str = re.sub(r'[^\w\s]', '', the_str)
    tokenized = nltk.word_tokenize(the_str)
    tagged = nltk.pos_tag(tokenized)
    lemmata = [WNL.lemmatize(item[0], TB2WN[item[1][0]])
            if item[1][0] in TB2WN else item[0] for item in tagged]
    for i, word in enumerate(lemmata):
        if word in digit2word:
            lemmata[i] = digit2word[word]
    return lemmata

if __name__ == '__main__':
    main('', '')
