class MyCalendar:
    def __init__(self):
        self.calen = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.calen:
            if startTime < e and s <endTime :      
                return False
        self.calen.append([startTime, endTime])
        return True