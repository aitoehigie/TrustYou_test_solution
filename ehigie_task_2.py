import re
import unittest

# Buffer to store current named entity
WORD_BUFFER = []
# Regular expression for matching a token at the beginning of a sentence
TOKEN_RE = re.compile(r"([a-z]+)\s*(.*)$", re.I)
# Regular expression to recognize an uppercase token
UPPERCASE_RE = re.compile(r"[A-Z][a-z]*$")

def pop_token(text):
    """
    Take the first token off the beginning of text. If its first letter is
    capitalized, remember it in word buffer - we may have a named entity on our
    hands!!

    @return: Tuple (token, remaining_text). Token is None in case text is empty
    """
    global WORD_BUFFER
    token_match = TOKEN_RE.match(text)
    if token_match:
        token = token_match.group(1)
        if UPPERCASE_RE.match(token):
            WORD_BUFFER.append(token)
        else:
            WORD_BUFFER = []
        return token, token_match.group(2)
    return None, text

def extract_named_entity():
    """
    Return a named entity, if we have assembled one in the current buffer.
    Returns None if we have to keep searching.
    """
    global WORD_BUFFER
    if len(WORD_BUFFER) >= 2:
        named_entity = " ".join(WORD_BUFFER)
        WORD_BUFFER = []
        return named_entity

class NamedEntityTestCase(unittest.TestCase):

    def test_ner_extraction(self):

        # Remember to change this Unit test as well to follow the interface
        # changes you propose above
        
        text = "When we went to Los Angeles last year we visited the Hollywood Sign"

        entities = set()
        while True:
            token, text = pop_token(text)
            if not token:
                entity = extract_named_entity()
                if entity:
                    entities.add(entity)
                break

            entity = extract_named_entity()
            if entity:
                entities.add(entity)

        self.assertEqual(set(["Los Angeles", "Hollywood Sign"]), entities)

if __name__ == "__main__":
    
    import sys
    
    # Test case names are passed in via sys.stdin, for scoring by remoteinterview.io
    
    for line in sys.stdin:
        test_name = line.rstrip()
        test_case = NamedEntityTestCase(test_name)
        runner = unittest.TextTestRunner()
        if runner.run(test_case).wasSuccessful():
            print("OK")
        else:
            print("Test {} failed!".format(test_name))
