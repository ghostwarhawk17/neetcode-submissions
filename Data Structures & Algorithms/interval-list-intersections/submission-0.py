class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []
        res = []
        firstList.sort(key = lambda x:x[0])
        secondList.sort(key = lambda x:x[0])

        i = j = 0

        while i < len(firstList) and j < len(secondList):
            start_a,end_a = firstList[i]
            start_b,end_b = secondList[j]

            new_start = max(start_a,start_b)
            new_end = min(end_a,end_b)
            if new_start <= new_end:
                res.append([new_start,new_end])

            if end_a < end_b:
                i+=1
            else:
                j+=1

        return res

