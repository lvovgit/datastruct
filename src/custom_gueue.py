class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        dequeue_element = self.head
        self.head = self.head.next_node
        return dequeue_element.data

        #new_node = Node(data)
        #self.head == None
        # new_node.next_node = self.tail
        # self.head = new_node

# queue1 = Queue()
# queue1.enqueue('data1')
# queue1.enqueue('data2')
# queue1.enqueue('data3')
#
# print(queue.head.data)
