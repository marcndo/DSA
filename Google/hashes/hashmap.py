class MyHashMap:

    def __init__(self):
        self.map_ = []
#needs to fix the put function to avoid duplicate values in line 12 through 16
    def put(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        if len(self.map_) == 0:
            self.map_.append([key, value])
        else:
            for item in self.map_:
                if item[0] == key:
                    item[1] = value
                elif [self.key, self.value] not in self.map_:
                    self.map_.append([self.key, self.value])

    def get(self, key: int) -> int:
        return self.key

    def remove(self, key: int) -> None:
        for item in self.map_:
            if self.key == item[0]:
                self.map_.remove(item)
            else:
                key = -1
                return key


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
myHashMap.put(2, 8)
print(myHashMap.map_)