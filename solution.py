#!/usr/bin/env python3

################################
# Author: Ehigie Pascal Aito
# Email: aitoehigie@gmail.com
# Date: 03/16/2018
################################



"""
NamedEntityRecognizer is responsible for recognizing all the entities in a text
"""


class NamedEntityRecognizer:
    # Regular expression for matching a token at the beginning of a sentence
    FIRST_SENT_TOKEN_RE = re.compile(r"([a-z]+)\s*(.*)$", re.I)

    # Regular expression to recognize an uppercase token
    CAPITALIZED_TOKEN_RE = re.compile(r"[A-Z][a-z]*$")

    def __init__(self, text):
        # Buffer to store current named entity
        self.named_entity_buffer = []
        # keeps track of the text to be processed
        self.remaining_text = text

    def update_buffer(self, entity_token):
        """
        Updates named entity buffer if its a capitalized word
        """
        if self.CAPITALIZED_TOKEN_RE.match(entity_token):
            self.named_entity_buffer.append(entity_token)
        else:
            self.named_entity_buffer = []

    def chop_token_to_buffer(self):
        """
        Take the first token off the beginning of text. If its first letter is
        capitalized, remember it in word buffer - we may have a named entity on our
        hands!!

        @return: token, token is None in case text is empty
        """

        entity_match = self.FIRST_SENT_TOKEN_RE.match(self.remaining_text)
        entity_token = None

        if entity_match:
            entity_token = entity_match.group(1)
            self.remaining_text = entity_match.group(2)
            self.update_buffer(entity_token)
        return True if entity_token else False


    def consume_namedentity_buffer(self):
        """
        Return a named entity, if we have assembled one in the current buffer.
        Returns None if we have to keep searching.

        @return named entity string if buffer has enough tokens otherwise None
        """
        if len(self.named_entity_buffer) >= 2:
            named_entity = " ".join(self.named_entity_buffer)
            # Clears buffer after finding named entity
            self.named_entity_buffer = []
            return named_entity
        else:
            return None

    def get_named_entities(self):
        """
        Returns set of  named entities in a text
        @return set
        """
        entities = set()

        while self.chop_token_to_buffer():
            entity = self.consume_namedentity_buffer()
            if entity:
                entities.add(entity)

        return entities


class NamedEntityTestCase(unittest.TestCase):
    def test_ner_extraction(self):
        # Remember to change this Unit test as well to follow the interface
        # changes you propose above

        text = "When we went to Los Angeles last year we visited the Hollywood Sign"

        ner = NamedEntityRecognizer(text)
        entities = ner.get_named_entities()

        self.assertEqual(set(["Los Angeles", "Hollywood Sign"]), entities)


if __name__ == "__main__":
    unittest.main()

import re
import unittest


class NamedEntityRecognizer:
    # Regular expression for matching a token at the beginning of a sentence
    FIRST_SENT_TOKEN_RE = re.compile(r"([a-z]+)\s*(.*)$", re.I)

    # Regular expression to recognize an uppercase token
    CAPITALIZED_TOKEN_RE = re.compile(r"[A-Z][a-z]*$")

    def __init__(self, text):
        # Buffer to store current named entity
        self.named_entity_buffer = []
        # keeps track of the text to be processed
        self.remaining_text = text

    def update_buffer(self, entity_token):
        """
        Updates named entity buffer if its a capitalized word
        """
        if self.CAPITALIZED_TOKEN_RE.match(entity_token):
            self.named_entity_buffer.append(entity_token)
        else:
            self.named_entity_buffer = []

    def chop_token_to_buffer(self):
        """
        Take the first token off the beginning of text. If its first letter is
        capitalized, remember it in word buffer - we may have a named entity on our
        hands!!

        @return: token, token is None in case text is empty
        """

        entity_match = self.FIRST_SENT_TOKEN_RE.match(self.remaining_text)
        entity_token = None

        if entity_match:
            entity_token = entity_match.group(1)
            self.remaining_text = entity_match.group(2)
            self.update_buffer(entity_token)
        return True if entity_token else False


    def consume_namedentity_buffer(self):
        """
        Return a named entity, if we have assembled one in the current buffer.
        Returns None if we have to keep searching.

        @return named entity string if buffer has enough tokens otherwise None
        """
        if len(self.named_entity_buffer) >= 2:
            named_entity = " ".join(self.named_entity_buffer)
            # Clears buffer after finding named entity
            self.named_entity_buffer = []
            return named_entity
        else:
            return None

    def get_named_entities(self):
        """
        Returns set of  named entities in a text
        @return set
        """
        entities = set()

        while self.chop_token_to_buffer():
            entity = self.consume_namedentity_buffer()
            if entity:
                entities.add(entity)

        return entities


class NamedEntityTestCase(unittest.TestCase):
    def test_ner_extraction(self):
        # Remember to change this Unit test as well to follow the interface
        # changes you propose above

        text = "When we went to Los Angeles last year we visited the Hollywood Sign"

        ner = NamedEntityRecognizer(text)
        entities = ner.get_named_entities()

        self.assertEqual(set(["Los Angeles", "Hollywood Sign"]), entities)


if __name__ == "__main__":
    unittest.main()
