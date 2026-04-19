class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.word = False


class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.word

    def starts_with(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True

    # Added method to solve this exercise:
    def fuzzy_search(self, word: str, fuzz_char: str = '.'):
        candidates = [self.root]

        for c in word:
            if not candidates:
                return False
            # Matching a fuzzy char - take every node at the current depth and add it to the queue
            if c == fuzz_char:
                queue_len = len(candidates)
                for _ in range(0, queue_len):
                    candidate = candidates.pop(0)

                    for val in candidate.children.values():
                        candidates.append(val)
                continue

            queue_len = len(candidates)
            for _ in range(0, queue_len):
                candidate = candidates.pop(0)

                if c in candidate.children:
                    candidates.append(candidate.children[c])

        for entry in candidates:
            if entry.word:
                return True

        return False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.fuzzy_search(word)

