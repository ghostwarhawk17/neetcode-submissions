class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        ans = []
        time = 0

        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

        maxheap = [(-cnt, ch) for ch, cnt in count.items()]
        heapq.heapify(maxheap)

        q = deque()

        while maxheap or q:
            time += 1

            if maxheap:
                cnt, char = heapq.heappop(maxheap)
                cnt += 1
                ans.append(char)

                if cnt:
                    q.append((cnt, char, time + 1))

            if q and q[0][2] == time:
                cnt, char, _ = q.popleft()
                heapq.heappush(maxheap, (cnt, char))

            if not maxheap and q and q[0][2] > time:
                return ""

        return "".join(ans)