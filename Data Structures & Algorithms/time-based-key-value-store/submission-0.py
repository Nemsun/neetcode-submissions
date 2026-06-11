class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map:
            return ""
        
        L, R = 0, len(self.time_map[key]) - 1
        res = ""

        while L <= R:
            M = L + (R - L) // 2

            if self.time_map[key][M][1] <= timestamp:
                res = self.time_map[key][M][0]
                L = M + 1
            else:
                R = M - 1
        
        return res

        
        
        

