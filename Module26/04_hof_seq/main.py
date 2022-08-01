from collections.abc import Iterator


def qhofstadter(qlist: list) -> Iterator[int]:
    if qlist != [1, 1]:
        qlist = []
    while True:
        try:
            qnext = qlist[- qlist[- 1]] + qlist[- qlist[- 2]]
            qlist.append(qnext)
            yield qnext
        except IndexError:
            print('list index out of range')
            break


i = 1
for elem in qhofstadter([1, 1]):
    if i > 15:
        break
    else:
        print(elem, end=' ')
        i += 1


class QHofstadter:
    def __init__(self, qlist) -> None:
        self.qlist = qlist[:]

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self):
        try:
            new = self.qlist[- self.qlist[-1]] + self.qlist[- self.qlist[-2]]
            self.qlist.append(new)
            return new
        except IndexError:
            print('list index out of range')
            raise StopIteration

    def current_state(self):
        return self.qlist


iteratorQ = QHofstadter([1, 1])
print()
print([next(iteratorQ) for _ in range(25)])
print(iteratorQ.current_state())
