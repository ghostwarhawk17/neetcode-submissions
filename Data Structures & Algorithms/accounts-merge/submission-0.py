class disjoint:
    def __init__(self, n):
        self.parent = [0] * n
        self.size = [1] * n
        self.rank = [0] * n

        for i in range(n):
            self.parent[i] = i

    def finduparent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.finduparent(self.parent[node])
        return self.parent[node]

    def unionset(self, u, v):
        ult_u = self.finduparent(u)
        ult_v = self.finduparent(v)

        if ult_u == ult_v:
            return

        if self.size[ult_u] > self.size[ult_v]:
            self.parent[ult_v] = ult_u
            self.size[ult_u] += self.size[ult_v]

        elif self.size[ult_v] > self.size[ult_u]:
            self.parent[ult_u] = ult_v
            self.size[ult_v] += self.size[ult_u]

        else:
            self.parent[ult_u] = ult_v
            self.size[ult_v] += self.size[ult_u]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ds = disjoint(len(accounts))
        hashmap = {}
        for i, arr in enumerate(accounts):
            for email in arr[1:]:
                if email not in hashmap:
                    hashmap[email] = i
                else:
                    ds.unionset(i, hashmap[email])

   
        merged = defaultdict(list)

        for email, value in hashmap.items():
            ult_p = ds.finduparent(value)
            merged[ult_p].append(email)

        ans = []
        for parent, emails in merged.items():
            emails.sort()
            ans.append([accounts[parent][0]] + emails)

        return ans

