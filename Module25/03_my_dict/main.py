

class MyDict(dict):

    def __init__(self, dict):
        super().__init__(dict)
        self.dict = dict

    def __str__(self):
        return f'{self.dict}'

    def get(self, key, default=None):
        return super().get(key, 0)


dic = MyDict({1: 'a', 2: 'B'})
print(dic)

print(dic.get('2'))
print(dic.get(1))

