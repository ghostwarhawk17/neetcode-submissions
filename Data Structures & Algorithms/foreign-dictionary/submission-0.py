class Solution:

    def dfs(self, node, visited, pathVisited, adj, stack):

        visited[node] = 1
        pathVisited[node] = 1
        for it in adj[node]:
            if not visited[it]:
                if self.dfs(it, visited, pathVisited, adj, stack):
                    return True
            elif pathVisited[it]:
                return True
        pathVisited[node] = 0
        stack.append(node)
        return False

    def foreignDictionary(self, words):
        adj = {}

        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch] = []

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            # Invalid case
            if len(first) > len(second) and first.startswith(second):
                return ""
            length = min(len(first), len(second))
            for j in range(length):
                if first[j] != second[j]:
                    adj[first[j]].append(second[j])
                    break
        visited = {ch: 0 for ch in adj}
        pathVisited = {ch: 0 for ch in adj}
        stack = []
        for ch in adj:
            if not visited[ch]:
                if self.dfs(ch, visited, pathVisited, adj, stack):
                    return ""
        stack.reverse()
        return "".join(stack)