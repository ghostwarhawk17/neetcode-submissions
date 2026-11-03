class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in  range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(node,par):
            if node in visited:
                return False
            visited.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei,node):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n
        
        
