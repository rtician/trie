class Trie(object):
    def __init__(self):
        self.children = {}
        self.end_word = False

    def add(self, char):
        self.children[char] = Trie()

    def insert(self, word):
        node = self
        for char in word.lower():
            if char not in node.children:
                node.add(char)
            node = node.children[char]
        node.end_word = True

    def find_words(self, prefix):
        results = []
        if self.end_word:
            results.append(prefix)
        for char, node in self.children.items():
            results.extend(node.find_words(prefix + char))
        return results

    def autocomplete(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.find_words(prefix)

