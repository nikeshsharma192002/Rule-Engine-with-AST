# node.py

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operand" or "operator"
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Operator or operand value

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"
