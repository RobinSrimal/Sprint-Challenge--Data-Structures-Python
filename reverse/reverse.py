class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        

        if node == None:

            return 

        # save next node for later
        next_node = node.get_next()

        # set next of node to the previous node
        node.set_next(prev)

        # update previous node to current node
        prev = node

        # if there is no next node we reached the end of the linked list
        # therefore the head of the linked list is the current node
        if not next_node:

            self.head = node

        # otherwise we call reverse_ list where next_node == node.next and 
        # prev == node
        else: 
            self.reverse_list(next_node, prev)




