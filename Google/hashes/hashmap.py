class MyHashMap:
    def __init__(self):
        self.map_ = []

    @staticmethod
    def hash_function(key):
        return hash(key)

    def put(self, key, value):
        index = self.hash_function(key)
        print(index)
        for pair in self.map_:
            if pair[0] == key:
                pair[1] = value
        else:
            self.map_.append([key, value])

    def get(self, key):
        for pair in self.map_:
            if self.hash_function(key) == pair[0]:
                return pair[1]
            else:
                return -1

    def remove(self):
        pass


myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.map_)
print(myHashMap.get(3))



