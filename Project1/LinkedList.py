########################################
# PROJECT 1 - Linked List
# Author: Ethan Lee
# PID: A48941153
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)


class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None  # Node
        self.tail = None  # Node
        self.size = 0     # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    ###### COMPLETE THE FUNCTIONS BELOW #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        Gets the number of nodes of the linked list
        :return: size of list
        """
        size = 0
        node = self.head
        while node:
            node = node.next_node
            size = size +1
        return size
        pass

    def is_empty(self):
        """
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        """
        node = self.head
        if node.next_node == self.tail:
            return True
        else:
            return False
        pass

    def front_value(self):
        """
        Gets the first value of the list
        :return: value of the list head
        """
        node = self.head
        return node.value
        pass

    def back_value(self):
        """
        Gets the last value of the list
        :return: value of the list tail
        """
        node = self.tail
        return node.value
        pass

    def count(self, val):
        """
        Counts the number of times a value 'val' occurs in the list
        :param val: value to find and count
        :return: number of time 'val' occurs
        """
        node = self.head
        count = 0
        while node:
            if node.value == val:
                count = count +1
            node = node.next_node
        return count
        pass

    def find(self, val):
        """
        Searches for and returns the first node with the value 'val'
        :param val: value to search for
        :return: True if value is in list, False if value is not found
        """
        node = self.head
        while node:
            if node.value == val:
                return True
            node = node.next_node
        return False
        pass

    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        Adds a node to the front of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        new_node = Node(val)
        if self.head == None:
            self.tail = new_node
        new_node.next_node = self.head
        self.head = new_node

        pass

    def push_back(self, val):
        """
        Adds a node to the back of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node != None:
                node = node.next_node
            node.next_node = new_node
        self.tail = new_node
        pass

    def pop_front(self):
        """
        Removes a node from the front of the list
        :return: the value of the removed node
        """
        trash_node = self.head
        self.head = trash_node.next_node
        return trash_node.value
        pass

    def pop_back(self):
        """
        Removes a node from the back of the list
        :return: the value of the removed node
        """
        node = self.head
        while node.next_node != self.tail:
            node = node.next_node
        trash_node = node.next_node
        node.next_node = None;
        self.tail = node
        return trash_node.value
        pass
