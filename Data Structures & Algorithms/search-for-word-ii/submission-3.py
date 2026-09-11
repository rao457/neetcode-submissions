class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node.children:
                return

            nxt = node.children[ch]

            # Complete word found
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None       # prevent duplicates

            # Mark visited
            board[r][c] = '#'

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols
                    and board[nr][nc] != '#'
                    and board[nr][nc] in nxt.children
                ):
                    dfs(nr, nc, nxt)

            # Restore
            board[r][c] = ch

            # ⭐ Pruning
            if not nxt.children and nxt.word is None:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result