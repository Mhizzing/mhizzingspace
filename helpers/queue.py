class Queue:
    def __init__(self):
        self.queue = []
        self.maxlen = 10

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    def __str__(self):
        queue_str = ''
        if self.queue:
            for item in self.queue:
                queue_str +=  str(item) + '\n'
            return queue_str[:-1]
        else:
            return '0 items in queue.'

test = Queue()
test.push(1)
test.push(2)
test.push(3)
print(test)