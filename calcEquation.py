"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations or len(equations) != len(values):
            return []
        if not queries:
            return []
        
        def add_connection(n1, n2, val):
            if n1 in graph:
                graph[n1].append((n2, val))
            else:
                graph[n1] = [(n2, val)]
        
        
        graph = {}
        
        i = 0 
        while i < len(values):
            n1, n2 = equations[i]
            val = values[i]
            add_connection(n1, n2, val)
            add_connection(n2, n1, 1/val)
            i += 1
        
        def calc_query(query):
            n1, n2 = query
            if n1 not in graph or n2 not in graph:
                return -1.0
            
            q = collections.deque([(n1, 1.0)])
            seen = set()
            while q:
                n, val = q.popleft()
                seen.add(n)
                if n == n2:
                    return val
                for neighbor, neighbor_val in graph[n]:
                    if neighbor not in seen:
                        q.append((neighbor, neighbor_val * val))
                        if n != n1:
                            graph[n1].append((neighbor, neighbor_val * val))
            
            return -1.0
        
        
        return [calc_query(query) for query in queries]
            