from LinkedList import LinkedList, HashListNode


class HashTable:
    """
    Hash table class, utilizes linked list for resolving collisions with separate chaining
    """
    def __init__(self, tableSize=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.tableSize = tableSize
        self.numItems = 0
        self.table = [LinkedList() for i in range(self.tableSize)]

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.tableSize != other.tableSize:
            return False
        for i in range(self.tableSize):
            if self.table[i] != other.table[i]:
                return False
        return True

    def hash_function(self, x):
        """
        DO NOT EDIT
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.tableSize


    # ------------------------------------------
    # ---------- DO NOT MODIFY ABOVE -----------
    # ------------------------------------------
    # -------------- MODIFY BELOW --------------


    def __repr__(self):
        """
        Defines string representation of a hash table
        :return: string representing hash table
        """
        hashstring = ""
        number = 0
        #number is used to keep track of which "bucket(linked list)" contains which key-value pairs
        for i in self.table:
            hashstring = hashstring + "[" + str(number) + "]: "
            if repr(i) is not None:
                hashstring = hashstring + repr(i) + '\n'
            number = number + 1
        return hashstring

    def insert(self, key, value):
        """
        precondition: key-value pair
        postcondition: inserts key-value pair into hash table
        """
        if key != "" and key is not None:
            j = self.hash_function(key)
            self._bucket_setitem(j, key, value) #inserts key-value using linked list "bucket"
            if self.numItems > self.tableSize // 1.25: # keep load factor <= 0.8
                self.double()

    def _bucket_setitem(self, j, key, value):
        """
        precondition: hash value and the key-value pair it represents
        postcondition: inserts key and value into "bucket" using hash value
        """
        if self.table[j] is None:
            self.table[j] = LinkedList()  # bucket is new to the table
        old_size = self.table[j].size()
        self.table[j].append(key,value) #inserts into linked list with linked list method
        if self.table[j].size() > old_size:  #if key was new to the table (i.e. size increased)
           self.numItems += 1  # increase size

    def find(self, key):
        """
        precondition: key to find
        postcondition: returns node with key, or false if not found
        """
        for i in self.table:
            node = i.find(key)
            if node:
                return node
        return False

    def lookup(self, key):
        """
        precondition: key of node to find
        postcondition: returns value corresponding to the given key, or false if not found
        """
        node = self.find(key)
        if node == False:
            return False
        if node is None:
            raise KeyError('Key Error: ' + repr(key))        # no match found
        return node.value                      # may raise KeyError

    def delete(self, key):
        """
        precondition: key of hash to delete
        postcondition: deletes hashlistnode of given key
        """
        j = self.hash_function(key)
        self.bucket_delitem(j, key)  # may raise KeyError
        self.numItems -= 1

    def bucket_delitem(self, j, key):
        """
        precondition: hash value and its key
        postcondition: removes hash value from linked list
        """
        bucket = self.table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(key))  # no match found
        bucket.remove(self.find(key))

    def double(self):
        """
        precondition: none
        postcondition: doubles size of hash table and rehashes
        """
        self.tableSize = 2 * self.tableSize
        self.rehash()

    def rehash(self):
        """
        precondition: none
        postcondition: rehashes hashtable
        """
        old = self.table #record old hashtable
        self.numItems = 0 #reset items counter
        self.table = [LinkedList() for i in range(self.tableSize)] #create new hashtable
        for bucket in old: #insert old key-values into new hashtable
            node = bucket.head
            while node is not None:
                self.insert(node.key,node.value)
                node = node.next

def FindWords(phrase, k):
    """
    precondition: string phrase and number k
    postcondition: returns set of all substrings > 1 that occur in the phrase k times
    """
    hash_table = HashTable()
    count_set = set()
    length = len(phrase)
    for i in range(length):
        for j in range(i+1,length+1):
            #uses two loops to find all of the substrings in phrase
            substring = phrase[i:j]
            count = hash_table.lookup(substring)#notes if substring is already in hashtable
            #if substring in hashtable, update it's count to be one greater, otherwise put into
            #hashtable with a count of 1
            if count and len(substring)>1:
                hash_table.insert(substring.lower(),count+1)
            elif len(substring)>1:
                hash_table.insert(substring.lower(),1)
    for i in range(length):
        for j in range(i+1,length+1):
            #get all substrings again, but now check to see what their final count is
            substring = phrase[i:j]
            count = hash_table.lookup(substring)
            #if final count is equal to k, add to set of substrings
            if count == k:
                count_set.add(substring)
    return count_set