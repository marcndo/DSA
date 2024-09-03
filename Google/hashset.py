class MyHashSet:

    def __init__(self):
        self.item = []

    def add(self, key: int) -> None:
        self.key = key
        if self.key in self.item:
            pass
        else:
            return self.item.append(self.key)

    def remove(self, key: int) -> None:
        self.item.remove(self.key)

    def contains(self, key: int) -> bool:
        if self.key in self.item:
            return True
        else:
            return False


object1 = MyHashSet()

object1.add(1)
object1.add(2)
print(object1.contains(1))
print(object1.item)
print(object1.remove(2))
print(object1.item)
print(object1.contains(3))
