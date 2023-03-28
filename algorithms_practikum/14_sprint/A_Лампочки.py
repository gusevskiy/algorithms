LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def solution(root) -> int:
    value = root.value

    def _sub(links, value):

        if links.left is not None:
            value = (links.value if value < links.value else value)
            value = _sub(links.left, value)
        if links.right is not None:
            value = (links.value if value < links.value else value)
            value = _sub(links.right, value)
        if value < links.value:
            return links.value
        else:
            return value
    value = _sub(root, value)
    return value


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3

if __name__ == '__main__':
    test()