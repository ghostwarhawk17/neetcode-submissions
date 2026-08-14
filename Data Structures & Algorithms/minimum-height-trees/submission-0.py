class Solution:
    def bfs(self,node,adj):
        height = 0
        visited = set()
        q = deque()
        q.append((node,0))
        visited.add(node)

        while q:
            node,h = q.popleft()
            height = max(height , h)
            for nodes in adj[node]:
                if nodes not in visited:
                    visited.add(nodes)
                    q.append((nodes,h + 1))
        
        return height 

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        min_height = [] * len(adj)

        for parent,child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        heights = [self.bfs(i, adj) for i in range(n)] 
        mini = min(heights)

        min_h = min(heights)
        return [i for i, h in enumerate(heights) if h == min_h]

        
