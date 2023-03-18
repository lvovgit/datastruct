from typing import Any

class Node:
    """Класс узла, содержащий данные и ссылку на следующий узел"""
    def __init__(self, data: Any, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node('data'={self.data}, 'next_node'={self.next_node})"