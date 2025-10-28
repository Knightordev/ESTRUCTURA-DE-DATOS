from abc import ABC, abstractmethod

class Order:
    def __init__(self, qty, customer):
        self.qty = qty
        self.customer = customer
    
    def print(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qty}")
        print("     ------------")
    
    def getQty(self):
        return self.qty
    
    def getCustomer(self):
        return self.customer


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, next_node):
        self.next = next_node


class QueueInterface(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def front(self):
        pass

    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass


class Queue(QueueInterface):
    def __init__(self):
        self.frontNode = None
        self.rearNode = None
        self.count = 0

    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def front(self):
        if not self.isEmpty():
            return self.frontNode.getData()
        else:
            return None
        
    def enqueue(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.frontNode = newNode
            self.rearNode = newNode
        else:
            self.rearNode.setNext(newNode)
            self.rearNode = newNode
        self.count += 1

    def dequeue(self):
        if not self.isEmpty():
            item = self.frontNode.getData()
            self.frontNode = self.frontNode.getNext()
            self.count -= 1
            if self.isEmpty():
                self.rearNode = None
            return item
        else:
            return None
    
    def printInfo(self):
        print("********* QUEUE DUMP *********")
        print("   Size:", self.size())
        current = self.frontNode
        i = 1
        while current is not None:
            print(f"   ** Element {i}")
            current.getData().print()
            current = current.getNext()
            i += 1
        print("******************************")


def main():
    order1 = Order(20, "cost1")
    order2 = Order(30, "cost2")
    order3 = Order(40, "cost3")
    order4 = Order(50, "cost4")

    queue = Queue()
    queue.enqueue(order1)
    queue.enqueue(order2)
    queue.enqueue(order3)
    queue.enqueue(order4)

    print(f"Size of queue: {queue.size()}")
    print("Front of queue:")
    queue.front().print()

    print("\nQueue content:")
    queue.printInfo()

if __name__ == "__main__":
    main()