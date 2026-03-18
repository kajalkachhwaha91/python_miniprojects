class Queue:
    def __init__(self):
        self.queue = []
        self.stack = []

    def qqueue(self, element):
        self.queue.append(element)

    def reverse_k_ele(self, k):

        if k > len(self.queue):
            return "k greater than queue size"

        # Step 1: push first k elements to stack
        for i in range(k):
            self.stack.append(self.queue.pop(0))

        # Step 2: add stack elements back
        while self.stack:
            self.queue.append(self.stack.pop())

        # Step 3: move remaining elements
        for i in range(len(self.queue) - k):
            self.queue.append(self.queue.pop(0))


ob = Queue()

ob.qqueue("a")
ob.qqueue("b")
ob.qqueue("c")

print("Original queue:", ob.queue)

ob.reverse_k_ele(2)

print("After reversing first 2 elements:", ob.queue)