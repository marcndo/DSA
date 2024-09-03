class MyHashMap:

    def __init__(self, ):
        self.map_ = []

    def put(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        for item in self.map_:
            if self.key == item[0]:
                item[1] = self.value
            else:
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
print(myHashMap.map_)