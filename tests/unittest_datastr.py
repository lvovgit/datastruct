import unittest
from src.datastr import Node, Stack
from src.custom_gueue import Queue
from src.linked_list import LinkedList


class TestNode(unittest.TestCase):
    """Тест класса Node"""

    def test_node_init(self):
        node = Node(10)
        assert node.data == 10
        assert node.next_node is None

    def test_node_next_node(self):
        node1 = Node(5)
        node2 = Node('a', node1)
        assert node1.data == 5
        assert node2.next_node is node1

class TestStack(unittest.TestCase):
    """Тест класса Stack"""

    def test_stack_init(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        assert stack.top.data == 'data3'
        assert stack.top.next_node.data == 'data2'
        assert stack.top.next_node.next_node.data == 'data1'

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        assert stack.top.data == 'data1'
        assert data == 'data2'

class TestQueue(unittest.TestCase):
    """Тест класса Queue"""
    def test_enqueue(self):
        queue1 = Queue()
        queue1.enqueue('data1')
        queue1.enqueue('data2')
        queue1.enqueue('data3')
        assert queue1.head.data == 'data1'
        assert queue1.head.next_node.data == 'data2'
        assert queue1.tail.data == 'data3'
        assert queue1.tail.next_node is None

    def test_dequeue(self):
        queue1 = Queue()
        queue1.enqueue('data1')
        queue1.enqueue('data2')
        queue1.enqueue('data3')
        assert queue1.dequeue() == 'data1'
        assert queue1.dequeue() == 'data2'
        assert queue1.dequeue() == 'data3'
        assert queue1.dequeue() is None


class TestLinkedList(unittest.TestCase):
    """Тест класса LinkedList"""
    def test_linkedlist(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        assert ll.print_ll() == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"