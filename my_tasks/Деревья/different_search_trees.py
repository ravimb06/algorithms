LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def solution(root) -> bool:
    right_edge = True
    left_edge = True
    if root and root.left:
        if root.left.value >= root.value:
            return False
        elif root.left.right and root.left.right.value >= root.value:
            return False
        else:
            left_edge = solution(root.left)
    if root and root.right:
        if root.right.value <= root.value:
            return False
        elif root.right.left and root.right.left.value <= root.value:
            return False
        else:
            right_edge = solution(root.right)
    return right_edge and left_edge


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
