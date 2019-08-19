import random
import string
import unittest

from autocomplete import Trie


def random_string(length=10, possible_characters=(string.ascii_lowercase + string.digits)):
    return ''.join(random.choice(possible_characters) for _ in range(length))


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = [random_string() for _ in range(4)]

    def test_insert(self):
        self.assertFalse(self.trie.children)

        for word in self.words:
            self.trie.insert(word)
            self.assertTrue(self.trie.children)
            self.assertEqual(self.trie.autocomplete(word), [word])

        # Test ignore case on node build
        word = random_string()
        trie = Trie()
        trie.insert(word.upper())
        self.assertTrue(trie.autocomplete(word), word)

    def test_find_words(self):
        for word in self.words:
            node = self.trie
            self.trie.insert(word)
            for char in word:
                node = node.children[char]
            self.assertTrue(node.find_words(word), [word])

    def test_autocomplete(self):
        for word in self.words:
            self.trie.insert(word)

        prefix = random.choice(self.words)
        self.assertEqual(self.trie.autocomplete(prefix), [prefix])
        self.assertEqual(self.trie.autocomplete(random_string()), [])

