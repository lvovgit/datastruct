import unittest
from src.datastr import Node, Stack


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