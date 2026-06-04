class TimeMap:
    """
    the result should be like {"alice":{1:"happy",2:"sad"}}

    so initialization creates a set
    set(key, value, time) add a new key, or add a new value to list
    get(key, time), returns "" if key not exists 
    elif time>lenth-1 return index of length - 1 else time as index
    """

    def __init__(self):
        self.TimeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.TimeMap:
            values = self.TimeMap[key] #[[1:'happy'],[]]
            l, r = 0, len(values) - 1
            while l <= r:
                mid = (l + r) // 2
                if values[mid][0] == timestamp:
                    return values[mid][1]
                elif values[mid][0] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
            return values[r][1] if r >= 0 else ""
        return ""
        
            
        
        
