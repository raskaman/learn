class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    Singly linked list
    """    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Return the number of nodes in the list
        Takes 0(n) liner time
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node

        return count
              
    def add(self, data):
        """
        Adds a new node containing data at the head of the list
        Takes 0(1) contant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the fisrt node containing data that matches the key
        Return the node or 'None' if not found

        Takes 0(n) time, linear time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes 0(1) constant time but finding the node at the
        insertion point takes 0(n) linear time

        Takes 0(n) linear time
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -=1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def removeAtIndex(self, index):
        current = self.head
        
        if index == 0 and current is self.head:
            self.head = current.next_node
            return current
        
        if index > 0:
            position = index
            while position > 1:
                position -=1
                current = current.next_node

            prev_node = current
            remove_node = current.next_node
            next_node = current.next_node.next_node

            prev_node.next_node = next_node
        
        return remove_node

    def __repr__(self):
        """
        Return a string representation of the list
        Takes 0(n) time, linera time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> ' .join(nodes)

"""
l = LinkedList()
l.add(10)
l.add(20)
l.add(30)
l.add(40)
l.add(50)
l.removeAtIndex(1)
"""