"""
GooglereseTranslator class for the Speaking in Tongues problem
for Google Code Jam 2012
Qualification

Link to problem description:
http://code.google.com/codejam/contest/1460488/dashboard#s=p0

author: 
Christos Nitsas
(chrisn654)

language:
Python 3.2.1

date:
April, 2012
"""


from string import ascii_lowercase


class CantGuessMapFromExamplesError(Exception):
    def __init__(self):
        self.value = "Not enough examples! (missing more than one letter)"
    def __str__(self):
        return repr(self.value)


def guess_map_from_examples(examples):
    """
    Guess a letter-mapping-dictionary from the given examples.
    
    Assumptions:
    - the mapping is one-to-one and onto
    - the examples only contain lowercase ascii letters and spaces
    - the examples are valid (no contradictions)
    """
    result = {}
    for googlerese_string, english_string in examples.items():
        result.update(zip(googlerese_string, english_string))
    # make sure that space maps to space
    result[' '] = ' '
    missing_letters = set(ascii_lowercase + " ") - set(result.keys())
    if len(missing_letters) > 1:
        raise(CantGuessMapFromExamplesError)
    elif len(missing_letters) == 1:
        # one letter is missing but, since the mapping is one-to-one and 
        # onto, we can guess its mapping
        missing_letter = missing_letters.pop()
        missing_mappings = set(ascii_lowercase + " ") - set(result.values())
        result[missing_letter] = missing_mappings.pop()
    return result


class GooglereseTranslator:
    """
    A Googlerese-to-English translator.
    
    Tries to guess the letter-mapping-dictionary from the examples.
    """
    
    def __init__(self, examples=None):
        if examples is not None:
            self.letter_map_gtoe = guess_map_from_examples(examples)
        else:
            self.letter_map_gtoe = guess_map_from_examples(self.examples)
        self.translation_table_gtoe = str.maketrans(self.letter_map_gtoe)
    
    def to_english(self, message):
        return message.translate(self.translation_table_gtoe)
    
    examples = {"y qee":"a zoo", 
                "ejp mysljylc kd kxveddknmc re jsicpdrysi":"our language is impossible to understand", 
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd":"there are twenty six factorial possibilities", 
                "de kr kd eoya kw aej tysr re ujdr lkgc jv":"so it is okay if you want to just give up"}

