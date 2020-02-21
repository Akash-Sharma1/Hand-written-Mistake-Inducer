# Spelling Error Generator

This Program takes an sentence as an Input and Outputs a line with one or more spelling mistakes.

Usage
% pip install -r requirements.txt
% python Main.py

Spelling mistakes are introduced via following operations:

0. removing punctuations randomly
1. changing digits randomly
2. swapping letters randomly
3. repeating an letter randomly
4. deleting multiple occuring letters
5.a Generating a word based on how close it sounds to the actual word.
5.b returning a word sound similar to another and other is also an actual word.

Any of the operation is randomly applied on a random word from a given sentence, and the resulting word can be placed back in its correct place.

This program relies on phonetics and jellybean python librarie.
Sound codes are generated via Soundex, Demetaphone algorithms which are provided by "phonectincs" library
https://pypi.org/project/phonetics/
distance between the words is calculated via jaro wrinkler algorithm which is provided by "jellybean" library
https://jellyfish.readthedocs.io/en/latest/
