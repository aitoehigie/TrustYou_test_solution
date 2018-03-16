#!/usr/bin/env python3

#########################################
# Author: Ehigie Pascal Aito
# Email: aitoehigie@gmail.com
# Date: 03/16/2018
# Title: Refactored TrustYou test solution
##########################################

import re
import unittest

# Class based rewrite


class NamedEntityRecognizer:
    FIRST_SENT_TOKEN_RE = re.compile(r"([a-z]+)\s*(.*)$", re.I)
    CAPITALIZED_TOKEN_RE = re.compile(r"[A-Z][a-z]*$")

    def __init__(self, text):
        # Removed global variable and used a 
        # local buffer to store current named entity. 
        self.named_entity_buffer = []
        self.remaining_text = text

    def update_buffer(self, entity_token):
        if self.CAPITALIZED_TOKEN_RE.match(entity_token):
            self.named_entity_buffer.append(entity_token)
        else:
            self.named_entity_buffer = []

    def pop_token(self):
        entity_match = self.FIRST_SENT_TOKEN_RE.match(self.remaining_text)
        entity_token = None

        if entity_match:
            entity_token = entity_match.group(1)
            self.remaining_text = entity_match.group(2)
            self.update_buffer(entity_token)
        return True if entity_token else False


    def consume_named_entity_buffer(self):
        if len(self.named_entity_buffer) >= 2:
            named_entity = " ".join(self.named_entity_buffer)
            self.named_entity_buffer = []
            return named_entity
        else:
            return None

    def extract_named_entities(self):
        entities = set()

        while self.pop_token():
            entity = self.consume_named_entity_buffer()
            if entity:
                entities.add(entity)

        return entities


class NamedEntityTestCase(unittest.TestCase):
    def test_ner_extraction(self):

        text = "When we went to Los Angeles last year we visited the Hollywood Sign"

        ner = NamedEntityRecognizer(text)
        entities = ner.extract_named_entities()

        self.assertEqual(set(["Los Angeles", "Hollywood Sign"]), entities)


if __name__ == "__main__":
    unittest.main()
