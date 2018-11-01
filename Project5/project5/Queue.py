class Node:
  """Lightweight, nonpublic class for storing a singly linked node.
    should only be called within the LinkedQueue class definition """

  __slots__ = 'val', 'next'         # streamline memory usage

  def __init__(self, val, next):
    self.val = val
    self.next = next

  def __lt__(self, other):
    ''' assumes other is of same type, invoked with "<" '''
    return self.val <= other.val

  def __le__(self, other):
    ''' assumes other is of same type, invoked with "<=" '''
    return self.val <= other.val



class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  def __init__(self):
    """Create an empty queue."""
    self.head = None
    self.tail = None
    self.size = 0


  def __str__(self):
    ''' string implementation of current elements in queue '''
    head = self.head
    values = list()
    while head:
      values.append(str(head.val))
      head = head.next

    return ", ".join(values)

  __repr__ = __str__


################## start modifying below this line ######################
  def __len__(self):
    """
    Gets the number of nodes of the linked list
    :return: size of list
    """
    return self.size

  def is_empty(self):
    """
    precondition: none
    postcondition: returns a boolean type True if queue is empty, false if it isn't
    """
    if self.size == 0:
      return True
    return False

  def dequeue(self):
    """
    precondition: none
    postcondition: deletes front node and returns the value it was holding
    """
    old_head = self.head #temporarily stores node to be deleted
    if old_head.next:
        self.head = old_head.next #if there is another node, update front of queue
    self.size = self.size - 1
    if self.size == 0:
      self.head = None
      self.tail = None
    return old_head.val #return value


  def enqueue(self, element):
    """
    precondition: value that new node will store
    postcondition: adds a new node to the end of the queue, holding element as its value
    """
    new_node = Node(element,None)
    if self.head == None: #if this is the first node, set head and tail to be node
        self.head = new_node
        self.tail = new_node
    else: #otherwise set tail to be node
        node = self.tail
        node.next = new_node
    self.tail = new_node
    self.size = self.size + 1

  def get_middle(self):
    """
    precondition: none
    postcondition: returns the middle-most node in the queue (closer to first when even number of nodes)
    """
    mid_pos = (self.size-1)//2 #this is given
    node = self.head
    for i in range(0,mid_pos):#returns node that is at position given by said equation
        node = node.next
    return node

  def left(self):
    """
    precondition: none
    postcondition: returns the first node in the queue
    """
    return self.head

  def right(self):
    """
    precondition: none
    postcondition: returns the last node in the queue
    """
    return self.tail