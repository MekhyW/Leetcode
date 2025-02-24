class MyHashSet:

    def __init__(self):
        self.vals = {}

    def add(self, key: int) -> None:
        self.vals[key] = 1

    def remove(self, key: int) -> None:
        if key in self.vals:
            del self.vals[key]

    def contains(self, key: int) -> bool:
        return key in self.vals


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)