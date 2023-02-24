class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """Добавляет данные в стек"""
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        remove = self.top
        self.top = self.top.next_node
        return remove.data

# node1 = Node('data1')
#
#
# stack = Stack(node1)
# stack.push({'id': 1})
#
# node2 = Node({'id': 2})
# node1.next_node = node2
# print(node1.data)