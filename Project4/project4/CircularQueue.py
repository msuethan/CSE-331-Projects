class CircularQueue(object):
    def __init__(self, capacity=2):
        """
        Initialize the queue to be empty with a fixed capacity
        :param capacity: Initial size of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.list = [0] * self.capacity
        self.sum = 0
        self.read = 0
        self.write = 0

    def __eq__(self, other):
        return self.capacity == other.capacity \
               and self.size == other.size \
               and self.read == other.read \
               and self.write == other.write

    # ----------------------- MODIFY BELOW THIS LINE ---------------------------
    def __str__(self):
        '''
        Returns elements in circular queue as a string
        :param none:
        :return: string of elements (comma separated)
        '''
        if self.size == 0:
            return "Queue is empty"

        content = ""
        ##  INSERT STRING OUTPUT CODE HERE!
        for i in range(self.read,self.capacity):
            if self.list[i] != None:
                content = content + str(self.list[i]) + ", "
            #add all elements from the start of the filled queue to the end of the queue container
        if ((self.read != 0) and (self.list[0] != None)): #if the queue has circle back:
            #add all elements from the beginning of the queue container to the start of the filled queue
            #this grabs all the elements that have circle back
            for i in range(0,self.read):
                if self.list[i] != None:
                    content = content + str(self.list[i]) + ", "
        content = content[:-2]
        return f"Contents: {content}"


    # DO NOT MODIFY or DELETE this line
    __repr__ = __str__

    def enqueue(self, number):
        '''
        Adds number to back (write) of queue
        :param number:  number that is added to back
        :return: none
        '''
        if self.size == len(self.list):
            self.resize() #resize if too big
        #mod version of queue(saving for posterity): avail = (self.read+self.size)%self.capacity
        if (self.read != 0 and self.write == self.capacity):
            self.write = 0 #used to "circle back" if space at beginning
        self.list[self.write] = number
        self.write = self.write + 1
        self.size = self.size + 1
        self.sum = self.sum + number

    def dequeue(self):
        '''
        Removes element from front (read) of queue if queue is not empty
        :param none
        :return: none
        '''
        if self.size == 0:
            return(None)
        else:
            self.sum = self.sum - self.list[self.read]
            self.list[self.read] = None
            self.read = (self.read + 1)%self.capacity
            #use modulo so read is set correctly even when circling back
            self.size = self.size - 1

    def resize(self):
        '''
        Double the queue's capacity and move the first-most element to the front if possible
        :param none
        :return: none
        '''
        old = self.list
        self.capacity = 2 * self.capacity
        self.list = [None] * self.capacity #create new queue
        front = self.read
        for i in range(self.size): #copy old queue over, moved to start
            self.list[i] = old[front]
            front = (1 + front)%len(old)
        self.read = 0 #set beginning to 0
        self.write = len(old) #set end to lenth of old queue (end)

    def get_average(self):
        '''
        Calculate average of elements in the queue
        :param none:
        :return: number that is average of queue elements
        '''
        if self.size == 0:
            return 0
        return self.sum/self.size