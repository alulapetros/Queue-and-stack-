"""
A list stores data in a contiguous memory in such a way that it can be accessed by their index staring from zero and
go through all the way to the length of the list.Whereas dictionaries store data in association with another value which
is commonly called a key.Therefore, to access a data from a list we can use their index while in dictionaries we use
the key to get the value associated with it.
"""
class HashMap:
        def __init__(self):
                self.size = 10
                self.map = [None] * self.size

        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.size

        def add(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]

                if self.map[key_hash] is None:
                        self.map[key_hash] = [key_value]
                        return True
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True

        def get(self, key):
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None

        def delete(self, key):
                key_hash = self._get_hash(key)

                if self.map[key_hash] is None:
                        return False
                for i in range (len(self.map[key_hash])):
                        if self.map[key_hash][i][0] == key:
                                self.map[key_hash].pop(i)
                                return True
                return False

        def keys(self):
                arr = []
                for i in range(len(self.map)):
                        if self.map[i]:
                                arr.append(self.map[i][0])
                return arr

        def print(self):
                print('---PHONEBOOK----')
                for item in self.map:
                        if item is not None:
                                print(str(item))

h = HashMap()
h.add('Bob', '567-8888')
h.add('Jhon', '293-6753')
h.add('Jhon', '333-8233')
h.add('Marry', '293-8625')
h.add('Yani', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Yani', '777-8888')
h.print()
h.delete('Bob')
h.print()
print('Jhon: ' + h.get('Jhon'))
print(h.keys())