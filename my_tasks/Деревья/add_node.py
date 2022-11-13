LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root, key):
    if key < root.value:
        if root.left is None:
            root.left = Node(value=key)
            return root
        else:
            insert(root.left, key)
    if key >= root.value:
        if root.right is None:
            root.right = Node(value=key)
            return root
        else:
            insert(root.right, key)


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()
