class Queue:
    def __init__(self, balance):
        self.queue = []
        self.balance = 5000

    def enqueue_deposit(self, data):
        self.queue.append(data)
        print(self.balance)
        deposit = int(input("enter the amount to deposit:"))
        self.balance += deposit
        print(self.balance)

    def enqueue_withdraw(self, data):
        self.queue.append(data)
        withdraw = int(input("enter the amount to withdraw:"))
        if self.balance >= withdraw:
            self.balance -= withdraw
        else:
            print("insuffient balance")

    def dequeue(self):
        self.queue.pop(0)

    def display(self):
        print(self.balance)

    def size(self):
        s = len(self.queue)
        if s == 0:
            print("queue is empty")
        else:
            print("queue length is", s)


queue1 = Queue('100')
queue1.enqueue_withdraw('a')
queue1.enqueue_deposit('b')
queue1.dequeue()
queue1.enqueue_withdraw('c')
queue1.dequeue()
queue1.enqueue_deposit('d')
queue1.dequeue()
queue1.dequeue()
queue1.size()