"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        
        def add_vertices(w):
            for c in w:
                if c not in graph:
                    graph[c] = set()
        
        def add_words_to_graph(w1, w2):
            add_vertices(w1)
            add_vertices(w2)
            l = min(len(w1), len(w2))
            done = False
            for i in range(l):
                if w1[i] != w2[i]:
                    graph[w1[i]].add(w2[i])
                    done = True
                    break
            if not done and len(w1) > len(w2):
                return False
            return True
        
        def topo_dfs(x, g, visited, visiting, st): # Return True if there is a cycle
            visited.add(x)
            visiting.add(x)
            for nbr in g[x]:
                if nbr in visiting: # Back-Edge!
                    return True
                if nbr not in visited:
                    if topo_dfs(nbr, g, visited, visiting, st):
                        return True
            visiting.remove(x)
            st.append(x)
            return False

        
        for i in range(len(words) - 1):
            if not add_words_to_graph(words[i], words[i+1]):
                return ''
        add_vertices(words[-1])
        
        visited, visiting, st = set(), set(), []
        for k in graph.keys():
            if k not in visited:
                if topo_dfs(k, graph, visited, visiting, st):
                    return ""
        st.reverse()
        return "".join(st)