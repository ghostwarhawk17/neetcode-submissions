class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, par):
            if node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == par: continue       
                if dfs(nei, node):
                    return True
            return False

        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            visited = set()
            if dfs(u, -1):
                return [u, v]
        return []