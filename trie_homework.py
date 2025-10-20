class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.words = []

    def put(self, word, value=None):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        self.words.append(word)


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        """Підраховує кількість слів, що закінчуються заданим суфіксом"""
        if not isinstance(pattern, str):
            return 0
        return sum(1 for word in self.words if word.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        """Перевіряє, чи є слова з певним префіксом"""
        if not isinstance(prefix, str):
            return False
        return any(word.startswith(prefix) for word in self.words)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    print("🔍 Перевірка Trie-функцій:\n")
    print("Суфікси:")
    for suffix in ["e", "ion", "a", "at"]:
        print(f"{suffix}: {trie.count_words_with_suffix(suffix)}")

    print("\nПрефікси:")
    for prefix in ["app", "bat", "ban", "ca"]:
        print(f"{prefix}: {trie.has_prefix(prefix)}")