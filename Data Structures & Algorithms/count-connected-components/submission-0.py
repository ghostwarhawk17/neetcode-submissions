class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()
        q = deque()
        components = 0
        for parent,child in edges:
            adj[parent].append(child)
            adj[child].append(parent)

        for node in range(n):
            if node in visited:
                continue
            visited.add(node)
            components +=1
            if not q:
                q.append(node)

            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
        
        return components

        

