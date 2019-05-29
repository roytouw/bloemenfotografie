class Queue:

    def __init__(self, limit=5):
        self.limit = limit
        self.counter = 0
        self.data = []

    def put(self, val):
        if self.counter == self.limit:
            del self.data[0]
        else:
            self.counter += 1
        self.data.append(val)

    def pop(self):
        if self.counter == 0:
            raise IndexError('Queue is empty!')
        val = self.data.pop(0)
        self.counter -= 1
        return val

    def get_all(self):
        return self.data


if __name__ == "__main__":
    q = Queue(5)
    for i in range(5):
        q.put(i)
    for i in range(5, 10):
        q.put(i)
        print(q.get_all())






