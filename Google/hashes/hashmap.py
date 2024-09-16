class MyHashMap:
    def __init__(self):
        self.map_ = []

    # @staticmethod
    # def hash_function(key):
    #     return hash(key)

    def put(self, key, value):
        for pair in self.map_:
            if pair[0] == key:
                pair[1] = value
                return
        self.map_.append([key, value])

    def get(self, key):
        for pair in self.map_:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        for i, pair in enumerate(self.map_):
            if pair[0] == key:
                del self.map_[i]


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
# myHashMap.put(3, 3)
print(myHashMap.get(1))
print(myHashMap.get(3))
myHashMap.put(2, 1)
print(myHashMap.get(2))
print(myHashMap.remove(2))
print(myHashMap.get(2))
print(myHashMap.map_)