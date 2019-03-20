"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True
        
        q = collections.deque()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        n = len(board)
        m = len(board[0])
        word_l = list(word)[::-1]
        seen =set()
        for i in range(n):
            for j in range(m):
                if word_l and board[i][j] == word_l[-1]:
                    q.append((i,j))
                    seen.add((i,j))
                    word_l.pop()
                while q:
                    # print(q)
                    row, col = q.popleft()
                    next_q = []
                    for d in dirs:
                        r = row + d[0]
                        c = col + d[1]
                        if r < 0 or c < 0 or r >= n or c >= m or (r,c) in seen:
                            continue
                        if word_l and board[r][c] == word_l[-1]:
                            next_q.append((r,c))
                            seen.add((r,c))
                    # print(next_q)
                    if word_l:
                        word_l.pop()
                    q = collections.deque(next_q)
                    if not word_l and q:
                        return True
                    
                if not q and word_l:
                    word_l = list(word)[::-1]

        return False
        