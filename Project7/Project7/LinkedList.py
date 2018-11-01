class HashListNode:
    def __init__(self, key, val = None):
        """
        DO NOT EDIT
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.value = val
        self.key = key
        self.next = None

    def __str__(self):
        '''
        DO NOT EDIT
        String representation of a linked list node

        :return: String representation
        '''
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        '''
        DO NOT EDIT
        Equality operator
        :return: True if equal, false if not
        '''

        if self and other:
            return self.value == other.value and self.next == other.next \
                   and self.key == other.key
        elif not self and not other:
            return True

        return False

class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None
        self.tail = None

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """

        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next
                temp_other = temp_other.next
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True


    # -------------------------------
    # ----- DO NOT MODIFY ABOVE -----
    # ----- MODIFY BELOW ------------
    # -------------------------------


    def __repr__(self):
        """
        Defines string representation of a linked list
        :return: string representing linked list
        """
        temp_node = self.head
        if temp_node is None:
            return "" #return nothing if empty list
        printed = ""  #otherwise prints list as node1->node2->etc.
        while temp_node is not None:
            if temp_node is not self.head:
                printed = printed + " -> "
            printed = printed +  str(temp_node.key) + ":" + str(temp_node.value)
            temp_node = temp_node.next
        return printed

    __str__ = __repr__


    def append(self, key, value):
        """
        precondition: key & its corresponding value
        postcondition: appends key & value pair to linked list (at the end)
        """
        #case1: if empty linked list, append as the head
        if self.head is None:
            self.head = HashListNode(key,value)
            self.tail = self.head
        #case2: append key & value as a node to end of list
        else:
            itr_node = self.head
            updated = False
            while itr_node is not None:
                #if key is already in list, update value instead
                if itr_node.key == key:
                    itr_node.value = value
                    updated = True
                itr_node = itr_node.next
            if updated is False:
                new_node = HashListNode(key,value)
                dummy_node = self.tail
                dummy_node.next = new_node
                self.tail = new_node

    def remove(self, key):
        """
        precondition: key of node to remove
        postcondition: remove node with corresponding key, do nothing if not there
        """
        node = self.find(key)
        #if node is only node, update head and tail
        if self.head == node:
            self.head = None
            self.tail = None
        elif node:
            parent = self.head
            while parent.next != node:
                parent = parent.next
            parent.next = node.next #update parent and child node to "go around" removed node
            if node == self.tail:
                self.tail = parent

    def find(self, key):
        """
        precondition: key of node to find
        postcondition: returns node with corresponding key, or False if node is not found
        """
        node = self.head
        while node:
            if node.key == key:
                return node
            node = node.next
        return False

    def size(self):
        """
        precondition: none
        postcondition: returns size of linked list
        """
        size = 0
        node = self.head
        while node:
            size = size + 1
            node = node.next
        return size