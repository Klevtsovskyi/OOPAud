class ProtectedDictInt:

    def __init__(self):
        self.dict = {}

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError(f"{key} has to be int type")
        return self.dict[key]

    def __setitem__(self, key, value):  # self[key] = value
        if not isinstance(key, int):
            raise TypeError(f"{key} has to be int type")
        if key in self.dict:
            raise KeyError(f"{key} is already in dict")
        self.dict[key] = value

    def __contains__(self, key):  # key in self
        return key in self.dict

    def __len__(self):  # len(self)
        return len(self.dict)

    def __str__(self):
        return str(self.dict)

    def __add__(self, other):  # self + other
        if isinstance(other, tuple) and len(other) == 2:
            key = other[0]
            value = other[1]
            self[key] = value
        elif isinstance(other, ProtectedDictInt):
            for key, value in other.dict.items():
                self[key] = value
        else:
            raise TypeError(f"{other} has to be tuple or ProtectedDictInt")
        return self

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"{other} has to be int type")
        if other in self:
            del self.dict[other]
        return self

    def __iter__(self):
        return ProtectedDictIntIterator(self.dict)


class ProtectedDictIntIterator:

    def __init__(self, dct: dict):
        self.collection = sorted(dct.keys())
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i == len(self.collection):
            raise StopIteration
        return self.collection[self.i]


if __name__ == '__main__':
    dct = ProtectedDictInt()
    dct + (100, 5) + (6, 32) + (54, 3) + (9, 65) + (23, 34) + (73, 53)
    for x in dct:
        print(x, end=" ")
    print()
    for x in dct:
        print(x, end=" ")
