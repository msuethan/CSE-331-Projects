###################################
# PROJECT 3 - STACK
# Author: Ethan Lee
# PID: A48941153
###################################
class Stack:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, capacity=2):
        """
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack.
        """
        self._capacity = capacity
        self._data = [0] * self._capacity
        self._size = 0

    def __str__(self):
        """
        Prints the elements in the stack from bottom of the stack to top,
        followed by the capacity.
        :return: string
        """
        if self._size == 0:
            return "Empty Stack"

        output = []
        for i in range(self._size):
            output.append(str(self._data[i]))
        return "{} Capacity: {}".format(output, str(self._capacity))

    ###### COMPLETE THE FUNCTIONS BELOW ######

    # --------------------Accessor Functions---------------------------------
    def get_size(self):
        '''
        Gets the number of elements in the stack
        :param none
        :return: int of the size (number of elements) in the stack
        '''
        return self._size

    def is_empty(self):
        '''
        Determines if the stack has elements in it
        :param none
        :return: bool, True if stack is empty, False if not
        '''
        if self._size == 0:
            return True
        return False

    def top(self):
        '''
        Returns the most recently added element (the top) in the stack
        :param none
        :return: the last element pushed on the stack
        '''
        if self._size == 0:
            return None
        return self._data[self._size-1]

    # ---------------------------Mutator Functions------------------------------

    def push(self, addition):
        '''
        Calls the grow function to increase the stack size if necessary, then puts a new element
        into the first empty space of the stack
        :param addition: the element to push on to the stack
        :return: none
        '''
        self.grow()
        self._data[self._size] = addition
        self._size = self._size + 1

    def pop(self):
        '''
        Deletes and returns the top of the stack
        :param none
        :return: the top of the stack, or none if the stack is empty
        '''
        if self._size == 0:
            return None
        top_value = self._data[self._size-1]
        self._size = self._size - 1
        self.shrink()
        return top_value

    def grow(self):
        '''
        If the stack capacity is equal to its size, creates a list with double the capacity and copies the stack over
        :param none
        :return: none
        '''
        if self._size == self._capacity:
            self._capacity = 2*self._capacity
            B = [0] * self._capacity
            for i in range(0,self._size):
                B[i] = self._data[i]
            self._data = B

    def shrink(self):
        '''
        If the stack size is less than or equal to half its capacity, creates a list with half the capacity and copies
        the stack over
        :param none
        :return: none
        '''
        if self._capacity//2 < 2:
            pass
        elif self._size <= self._capacity//2:
            self._capacity = self._capacity//2
            B = [0] * self._capacity
            for i in range(0,self._size):
                B[i] = self._data[i]
            self._data = B



def Palindrome(phrase):
    '''
    Determines if a given phrase is a palindrome (same forwards as backwards) using the stack class
    :param phrase: string whose palindrome status is in question
    :return: bool, True if palindrome, False if not
    '''
    import string
    phrase = "".join(char.lower() for char in phrase if (char in string.ascii_letters or char in string.digits))
    #removes all punctuation and spaces from the phrase string and changes uppercase letters to lowercase
    #imports and uses the string method function for ascii letters and digits
    phrasestack = Stack()
    for i in phrase:
        phrasestack.push(i)
    for i in phrase:
        if i != phrasestack.pop():
            return False
    return True