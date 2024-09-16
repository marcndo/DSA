class MyHashSet:
    def __init__(self):
        self.item = []

    def _hash_function(self, key):
        return hash(key)

    def add(self, key: int) -> None:
        self.key = key
        if self._hash_function(key) in self.item:
            self.key = self._hash_function(key)
        else:
            self.item.append(self._hash_function(key))

    def remove(self, key: int) -> None:
        self.item.remove(self._hash_function(key))

    def contains(self, key: int) -> bool:
        if self._hash_function(key) in self.item:
            return True
        else:
            return False


object1 = MyHashSet()

object1.add(1)
object1.add(2)
print(object1.contains(1))
print(object1.contains(3))
object1.add(2)
print(object1.item)
print(object1.contains(2))
print(object1.remove(2))
print(object1.contains(2))

