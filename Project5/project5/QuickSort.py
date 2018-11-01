from Queue import LinkedQueue, Node


def insertion_sort(queue):
    """
    precondition: queue to be sorted
    postcondition: sorts the nodes in a queue in ascending order using the insertion sort algorithm
    """
    after = queue.left() #make node designated for after current
    queue.enqueue(after.val) #enqueue the first node to the back, for easier sorting (see dummy)
    dummy = after
    after = after.next
    dummy.next = None #turn first node into dummy node with smallest value, for easy sorting
    dummy.val = smallest(queue) #set dummy value low so everything is sorted larger than dummy
    while after:
        curr = after
        after = after.next
        swapper = dummy
        while swapper.next != None and swapper.next < curr:
        #move thru queue to find element to swap with
            swapper = swapper.next
        curr.next= swapper.next #commence swapping
        swapper.next= curr
    queue.dequeue() #remove the dummy node from the queue

def pick_pivot(queue):
    """
    precondition: queue that needs a pivot picked
    postcondition: returns median pivot value between first, middle, and last node values
    """
    left = queue.left()
    right = queue.right()
    center = queue.get_middle()
    #^make nodes for each of the node positions
    #below: comparisons for determining which has median value
    if((left <= center) and (center <= right)):
        return center.val
    if((right <= center) and (center <= left)):
        return center.val
    if((center <= left) and (left <= right)):
        return left.val
    if((right <= left) and (left <= center)):
        return left.val
    return right.val

def quick_sort(queue):
    """
    precondition: queue to be sorted
    postcondition: sorts the nodes in a queue in ascending order using the quick sort algorithm
    """
    #code mostly from D2L slide example
    if len(queue) <= 10:
        insertion_sort(queue) #use insertion sort for queues smaller than 11
    else:
        pivot = Node(pick_pivot(queue),None) #pick pivot point and make pivot node for comparison
        L = LinkedQueue() #create queues for less than pivot, equal to, and greater than
        E = LinkedQueue()
        G = LinkedQueue()
        while not queue.is_empty(): #sort elements into respective queues
            if queue.left() < pivot:
                L.enqueue(queue.dequeue())
            elif pivot < queue.left():
                G.enqueue(queue.dequeue())
            else:
                E.enqueue(queue.dequeue())
        quick_sort(L) #recursively run quicksort to sort less than and greater than queues
        quick_sort(G)
        while not L.is_empty():#combine sorted queues for complete sorted queue
            queue.enqueue(L.dequeue())
        while not E.is_empty():
            queue.enqueue(E.dequeue())
        while not G.is_empty():
            queue.enqueue(G.dequeue())

def smallest(queue):
    """
    precondition: queue to find smallest value in
    postcondition: returns smallest value in queue, default as -1
    """
    smallest_val = -1 #-1 is less than 0.0 and 'a', the most likely lowest node values
    make_small = queue.left()
    while make_small != None and type(make_small.val) is not str:
        if make_small.val < smallest_val:
            smallest_val = make_small.val - 1
        make_small = make_small.next
    return smallest_val