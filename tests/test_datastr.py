from src.datastr import Node, Stack


def test_node_init():
    node = Node(10)
    assert node.data == 10
    assert node.next_node is None

def test_node_next_node():
    node1 = Node(5)
    node2 = Node('a', node1)
    assert node1.data == 5
    assert node2.next_node is node1

def test_stack_init():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    assert stack.top.data == 'data3'
    assert stack.top.next_node.data == 'data2'
    assert stack.top.next_node.next_node.data == 'data1'
