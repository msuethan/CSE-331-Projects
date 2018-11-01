########################################
# PROJECT 6 - BinarySearchTree
# Author: Ethan Lee
# PID: A48941153
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Describes equality comparison for nodes ('==')
        :param other: node being compare to
        :return: True if equal, False if not equal
        """
        return type(other) is type(self) and self.value == other.value

    def __repr__(self):
        """
        Defines string representation of a node (str())
        :return: string representing node
        """
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        :return nothing
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result


    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        precondition: value to insert into BST
        postcondition: puts value in a node and adds to BST if value not in BST
        """
        #case 1: empty BST/inserting the root
        if self.size == 0:
            self.root = Node(value)
            self.size = self.size + 1
        else:
            #uses the search function to find what the parent node of the value should be
            search_dummy = self.search(value, self.root)
            #case 2: inserts node to right based on relative value
            if search_dummy.value < value:
                search_dummy.right = Node(value)
                search_dummy.right.parent = search_dummy
                self.size = self.size + 1
            #case 3: inserts node to left based on relative value
            elif search_dummy.value > value:
                search_dummy.left = Node(value)
                search_dummy.left.parent = search_dummy
                self.size = self.size + 1

    def remove(self, value):
        """
        precondition: value to remove from BST
        postcondition: remove value from BST if possible, and update BST accordingly
        """
        #first search for the node with the offending value
        search_dummy = self.search(value, self.root)
        #if value is not in the BST, do nothing
        if search_dummy.value == value:
            left = search_dummy.left
            right = search_dummy.right
            parent = search_dummy.parent
            #case 1: remove node has both a left and right child
            if left and right:
                #calculate the replacement node: the smallest node that is bigger than the remove node
                replacement = search_dummy.right
                while replacement.left:
                    replacement = replacement.left
                #case 1.1: remove node is root (special b/c it does not have a parent)
                if search_dummy.value == self.root.value:
                    #case 1.11: the replacement node is just the right child (special case b/c of parent handling)
                    #procedure: make right subtree the BST and "add" the left subtree as the new root's left child
                    if replacement.value == self.root.right:
                        holder = self.root.left
                        self.root = self.root.right
                        self.root.parent = None
                        self.root.left = holder
                    #case 1.12: replacement node has a right subchild (there is no case where replacement has left child)
                    #procedure: change the root's value and update replacement's child as new child of replacement's parent
                    elif replacement.right:
                        self.root.value = replacement.value
                        if replacement.parent.right.value == replacement.value:
                            replacement.parent.right = replacement.right
                        if replacement.parent.left.value == replacement.value:
                            replacement.parent.left = replacement.right
                    #case 1.13: replacement node has no children
                    #procedure: change root's value and update replacement's parent to no child
                    else:
                        self.root.value = replacement.value
                        replacement.parent.left = None
                #case 1.2: remove node is NOT the root (it does have a parent)
                else:
                    #case 1.21: replacement node is the right child (special b/c parent handling)
                    #procedure: replace with right subtree and update info/add left subtree
                    if replacement.value == right.value:
                        if parent.value < search_dummy.value:
                            parent.right = right
                        if parent.value > search_dummy.value:
                            parent.left = right
                        right.left = left
                        right.parent = parent
                    #case 1.22: replacement node has right child
                    #procedure: update remove node's value and make replacement's child the new child of replacement's parent
                    elif replacement.right:
                        search_dummy.value = replacement.value
                        if replacement.parent.right.value == replacement.value:
                            replacement.parent.right = replacement.right
                        if replacement.parent.left.value == replacement.value:
                            replacement.parent.left = replacement.right
                    #case 1.23: replacement node is leaf
                    #procedure: change remove node's value and update replacement node's parent to none
                    else:
                        search_dummy.value = replacement.value
                        replacement.parent.left = None
            #case 2: remove node has only a left child
            elif left:
                #case 2.1: remove node is root (not a child)
                #procedure: update root to be the left child
                if search_dummy.value == self.root.value:
                    self.root = self.root.left
                    self.root.parent = None
                #case 2.2: remove node is a left child
                #procedure: update remove node's child to be the left child of remove node's parent
                elif search_dummy.value < parent.value:
                    parent.left = left
                    left.parent = parent
                #case 2.3: remove node is a right child
                #procedure: update remove node's child to be the right child of remove node's parent
                elif search_dummy.value > parent.value:
                    parent.right = left
                    left.parent = parent
            #case 3: remove node has only a right child
            elif right:
                #case 3.1: remove node is root (not a child)
                #procedure: update right child to be root
                if search_dummy.value == self.root.value:
                    self.root = self.root.right
                    self.root.parent = None
                #case 3.2: remove node is a left child
                #procedure: update remove node's child to be the left child of remove node's parent
                elif search_dummy.value < parent.value:
                    parent.left = right
                    right.parent = parent
                #case 3.3: remove node is a right child
                #procedure: update remove node's child to be the right child of remove node's parent
                elif search_dummy.value > parent.value:
                    parent.right = right
                    right.parent = parent
            #case 4: remove node has no child
            else:
                #case 4.1: remove node is root
                #procedure: root is now none
                if search_dummy.value == self.root.value:
                    self.root = None
                #case 4.2: remove node is left child
                #procedure: set remove node's parent's left child to none
                elif search_dummy.value < parent.value:
                    parent.left = None
                #case 4.3: remove node is right child
                #procedure: set remove node's parent's right child to none
                elif search_dummy.value > parent.value:
                    parent.right = None
            self.size = self.size - 1

    def search(self, value, node):
        """
        precondition: value to search for and node to start the search from
        postcondition: returns node with value if possible, otherwise returns the parent node of where the value would be
        """
        #case for empty BST
        if self.size == 0:
            return None
        #case for if the value is the value of the starting node
        if node.value == value:
            return node
        #if the value is more than starting node, recursively search the right subtree
        elif node.value < value:
            if node.right:
                return self.search(value,node.right)
            else:
                return node
        #if the value is less than starting node, recursively search the left subtree
        elif node.value > value:
            if node.left:
                return self.search(value,node.left)
            else:
                return node

    def inorder(self, node, inorder_list=list()):
        """
        precondition: node to start from, list to store elements
        postcondition: performs in-order traversal and stores elements in the list as they are visited
                     : returns list
        """
        if self.size == 0:
            return inorder_list
        if node.left: #first traverse left (recursively)
            self.inorder(node.left,inorder_list)
        inorder_list.append(node.value)#then node
        if node.right:#then right (recursively
            self.inorder(node.right,inorder_list)
        return inorder_list

    def preorder(self, node, preorder_list=list()):
        """
        precondition: node to start from, list to store elements
        postcondition: performs pre-order traversal and stores elements in list as they are visited
                     : returns list
        """
        if self.size == 0:
            return preorder_list
        preorder_list.append(node.value)#first append starting node
        if node.left:#then go left and use recursion
            self.preorder(node.left,preorder_list)
        if node.right:#finally go right and use recursion
            self.preorder(node.right,preorder_list)
        return preorder_list

    def postorder(self, node, postorder_list=list()):
        """
        precondition: node to start from, list to store elements
        postcondition: performs post-order traversal and stores elements in list as they are visited
                     : returns list
        """
        if self.size == 0:
            return postorder_list
        if node.left:#first go left (from bottom) and get nodes recursively
            self.postorder(node.left,postorder_list)
        if node.right:#then go right and get nodes recursively
            self.postorder(node.right,postorder_list)
        postorder_list.append(node.value)#finally append original (top-most) node
        return postorder_list

    def depth(self, value):
        """
        precondition: value to find the depth of
        postcondition: returns depth of the node containing the value
        """
        if self.size == 0:
            return -1
        #search for the value to get the node so it's position can be found
        search_dummy = self.search(value,self.root)
        #if value is not in the BST return -1
        if search_dummy.value != value:
            return -1
        #if value is the root it has 0 depth
        if search_dummy.value == self.root.value:
            return 0
        #values deeper than root have depth of their parent +1, so recursively find total depth
        else:
            return 1 + self.depth(search_dummy.parent.value)

    def height(self, node):
        """
        precondition: node to find height of
        postcondition: returns height of node
        """
        #empty BST has height -1 (root is ground level i.e. height 0)
        if node == None:
            return -1
        #total height is height of child + 1, so use recursion
        else:
            return max(self.height(node.left), self.height(node.right))+1

    def min(self, node):
        """
        precondition: starting node for minimum value search
        postcondition: returns node with minimum value
        """
        #if BST empty there is no min node
        if self.size == 0:
            return None
        #moves left (where smaller nodes are kept) recursively
        else:
            if node.left:
                return self.min(node.left)
            else:
                return node

    def max(self, node):
        """
        precondition: node to start maximum search from
        postcondition: returns node with maximum value
        """
        #if empty BST, no maximum
        if self.size == 0:
            return None
        #moves right (where bigger nodes are kept) recursively
        else:
            if node.right:
                return self.max(node.right)
            else:
                return node

    def get_size(self):
        """
        precondition: none
        postcondition: returns size of BST
        """
        return self.size