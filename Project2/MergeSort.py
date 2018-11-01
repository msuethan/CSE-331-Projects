
class LinkedListNode:
    def __init__(self, val = None):
        """
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.val = val
        self.next = None

    def __le__(self, other):
        '''
        :param other: Linked list node
        :return: boolean value of less than equal to other
        '''
        if isinstance(other, LinkedListNode):
            return self.val <= other.val





class LinkedList:
    def __init__(self):
        """
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None

    def __repr__(self):
        '''
        :param: none
        :return: string representation of linked list
        '''
        result = []
        current = self.head

        while current:
            result.append(str(current.val))
            current = current.next

        return " -> ".join(result)

    __str__ = __repr__


    def push_back(self, data):
        '''
        :param data:  val for new node to be added to Linked list
        :return: None
        '''
        node = LinkedListNode(data)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = node

        else:
            self.head = node




'''
ANYTHING BEFORE THIS COMMENT SHOULDN'T BE MODIFIED IN ANYWAY!
'''
# --------- START MODIFYING HERE ---------
def Partition(head):
    '''
    Goes through linked list to find the middle-most node
    :param head:  first node in a linked list
    :return: middle node of the linked list
    '''
    midpt = head                #the current midpoint in the linked list
    endpt = head.next           #the current endpoint in the linked list

    while endpt != None and endpt.next != None:
        endpt = endpt.next
        endpt = endpt.next      #endpoint "moves" twice as fast as midpoint so when it reaches the end of the list,
        midpt = midpt.next      #midpoint will be in the middle

    return midpt

def Merge(list1, list2):
    '''
    Merges two linked list into a single linked list
    :param list1:  the first node of a linked list
    :param list2:  the first node of a separate linked list
    :return: Merged linked list
    '''
    if list1 == None:           #if either list is empty, returns the non-empty list, which will already be sorted
        return list2
    if list2 == None:
        return list1

    if list1.val < list2.val:   #compares the value of the current node of each list and transfers the lower value to
        mergedlist = list1      #the merged list
        mergedlist.next = Merge(list1.next, list2)
    else:
        mergedlist = list2
        mergedlist.next = Merge(list1, list2.next)

    return mergedlist

def MergeSort(head):
    '''
    Sorts a linked list in ascending order using a Merge Sort Algorithm
    :param head:  the first node of the unsorted linked list
    :return: the first node of the new sorted linked list
    '''
    if head == None:
        return head
    if head.next == None:
        return head

    midpt = Partition(head)     #finds middle node of linked list
    head2 = midpt.next          #sets middle node as head of new linked list
    midpt.next = None           #completes partitioning by deleting connection to 2nd half of the original linked list

    head = MergeSort(head)      #recursive merge sort
    head2 = MergeSort(head2)
    head = Merge(head, head2)   #puts lists back together
    return head