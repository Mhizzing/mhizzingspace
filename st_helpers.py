import inspect

class Queue:
    def __init__(self):
        self.queue = []
        self.maxlen = 10

    def push(self, item):
        self.queue.append(item)

    def serve(self):
        if self.queue:
            print(f"I just popped out {self.queue[0]}")
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

def menu_gen(a_class):
    class_functions = inspect.getmembers(a_class, predicate=inspect.isfunction)
    outstr = ''
    for i, item in enumerate(class_functions):
        if item[0][0] != '_':
            outstr += f'{i}. ' + item[0] + '\n'
    return(outstr)
    
def main():
    test = Queue()
    test.push(1)
    test.push(2)
    test.push(3)
    print(test)

if __name__ == "__main__":
    main()