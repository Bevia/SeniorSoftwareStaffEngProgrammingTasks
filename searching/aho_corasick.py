from collections import deque, defaultdict

# The Aho-Corasick algorithm is a powerful string-matching algorithm used
# to search for multiple “patterns” or “keywords” in a single scan of a
# given “text.” It is especially efficient when searching for many
# patterns within the same text. It builds a finite state machine
# (trie with failure links) based on the patterns,
# allowing quick matching across patterns
class AhoCorasick:
    def __init__(self, patterns):
        self.trie = {}
        self.output = defaultdict(list)
        self.fail_links = {}
        self._build_trie(patterns)
        self._build_failure_links()

    def _build_trie(self, patterns):
        # Step 1: Build the trie
        for pattern in patterns:
            node = self.trie
            for char in pattern:
                node = node.setdefault(char, {})
            # Mark the end of a pattern with a list of patterns that end here
            self.output[id(node)].append(pattern)

    def _build_failure_links(self):
        # Step 2: Build failure links
        queue = deque()
        # Initialize root failure links and enqueue direct children of root
        for char, node in self.trie.items():
            self.fail_links[id(node)] = self.trie
            queue.append(node)

        while queue:
            current_node = queue.popleft()
            for char, next_node in current_node.items():
                # Set failure link for next_node
                fail_state = self.fail_links[id(current_node)]
                while fail_state is not None and char not in fail_state:
                    fail_state = self.fail_links.get(id(fail_state), None)
                self.fail_links[id(next_node)] = fail_state[char] if fail_state else self.trie

                # Append output patterns of the failure state to the current state
                if fail_state:
                    self.output[id(next_node)].extend(self.output[id(fail_state[char])])
                queue.append(next_node)

    def search(self, text):
        # Step 3: Search through the text
        node = self.trie
        matches = []

        for i, char in enumerate(text):
            while node is not None and char not in node:
                node = self.fail_links.get(id(node), None)
            if node is None:
                node = self.trie
                continue

            node = node[char]
            # Check for matches at this node
            for pattern in self.output[id(node)]:
                matches.append((pattern, i - len(pattern) + 1, i))

        return matches

# Example usage
patterns = ["he", "she", "his", "hers"]
text = "ushers"
aho_corasick = AhoCorasick(patterns)
matches = aho_corasick.search(text)
print("Matches found:", matches)