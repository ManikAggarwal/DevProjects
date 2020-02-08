from typing import List

class Node:
    def __init__(self, key):
        self.left = None
        self.val = key
        self.right = None

    def __repr__(self):
        return f'<Node {self.val}>'

class BinaryTree:
    def __init__(self, node: Node = None):
        self.head = node

    def add(self, node: Node) -> None:
        current_head = self.head
        while current_head:
            if node.val == current_head.val:
                raise ValueError(f'Node with value {node.val} already exists.')
            elif node.val < current_head.val:
                if not current_head.left:
                    current_head.left = node
                    return
                else:
                    current_head = current_head.left
            elif node.val > current_head.val:
                if not current_head.right:
                    current_head.right = node
                    return
                else:
                    current_head = current_head.right
        self.head = node

    def inorder(self) -> List[Node]:
        vals_list = list()
        self._inorder_traverse(self.head, vals_list)
        return vals_list

    def _inorder_traverse(self, current_head, vals_list):
        if not current_head:
            return
        self._inorder_traverse(current_head.left, vals_list)
        vals_list.append(current_head.val)
        self._inorder_traverse(current_head.right, vals_list)

    def preorder(self) -> List[Node]:
        vals_list = list()
        self._preorder_traverse(self.head, vals_list)
        return vals_list

    def _preorder_traverse(self, current_head, vals_list):
        if not current_head:
            return
        vals_list.append(current_head.val)
        self._preorder_traverse(current_head.left, vals_list)
        self._preorder_traverse(current_head.right, vals_list)

    def postorder(self) -> List[Node]:
        vals_list = list()
        self._postorder_traverse(self.head, vals_list)
        return vals_list

    def _postorder_traverse(self, current_head, vals_list):
        if not current_head:
            return
        self._postorder_traverse(current_head.left, vals_list)
        self._postorder_traverse(current_head.right, vals_list)
        vals_list.append(current_head.val)

    def find(self, val: int) -> Node:
        current_node = self.head

        while current_node:
            if current_node.val == val:
                return current_node
            elif val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right


    def find_parent(self, node: Node) -> Node:
        current_node = self.head

        if node.val == current_node.val:
            return current_node

        while current_node:
            if (current_node.left and current_node.left.val == node.val) or\
                    (current_node.right and current_node.right.val == node.val):
                return current_node
            elif node.val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def rightmost_node(self, node: Node) -> Node:
        while node:
            rightnode = node
            node = node.right
        return rightnode


    def delete(self, value: int) -> None:
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(to_delete)

        if to_delete.left and to_delete.right: # Both childs present
            rightmost_node = self.rightmost_node(to_delete.left)
            rightmost_parent = self.find_parent(rightmost_node)

            if rightmost_parent != to_delete:
                rightmost_parent.right = rightmost_node.left
                rightmost_node.left = to_delete.left
            rightmost_node.right = to_delete.right

            if to_delete_parent.left == to_delete:
                to_delete_parent.left = rightmost_node
            elif to_delete_parent.right == to_delete:
                to_delete_parent.right = rightmost_node
            else:
                self.head = rightmost_node

        elif to_delete.left or to_delete.right: # One child is present, could be right one or left one
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.left or to_delete.right
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.left or to_delete.right
            else:
                self.head = to_delete.left or to_delete.right

        else: # No children
            if  to_delete_parent.left == to_delete:
                to_delete_parent.left = None
            elif to_delete_parent.right == to_delete:
                to_delete_parent.right = None
            else:
                self.head = None




if __name__ == '__main__':
    # b = BinaryTree(Node(50))
    b = BinaryTree()
    c = tuple(map(int, input('Enter the nodes to be added to binary tree -> ').split()))

    for key in c:
        b.add(Node(key))

    delete_node_value = int(input('Enter node to delete -> '))
    b.delete(delete_node_value)
    print(b.preorder())