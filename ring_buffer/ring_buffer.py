# solution using an array as storage

# class RingBuffer:
#     def __init__(self, capacity):

#         self.capacity = capacity

#         self.size = 0

#         self.storage = []

#         self.counter = 0
               

#     def append(self, item):

#         if self.size < self.capacity:

#             self.storage.append(item)

#             self.size += 1

#         else:

#             self.storage[self.counter] = item

#             if self.counter < self.capacity -1:

#                 self.counter  += 1

#             else:

#                 self.counter = 0


#     def get(self):
        
#         return [item for item in self.storage if item != None]


# solution using a DoublyLinkedList

from doubly_linked_list import DoublyLinkedList



class RingBuffer:
    def __init__(self, capacity):

        self.capacity = capacity

        self.current = None

        self.storage = DoublyLinkedList()

        
            
    def append(self, item):

        if self.storage.length < self.capacity:

            self.storage.add_to_tail(item)

            self.current = self.storage.head


        else:

            self.current.value = item

            if self.current.next == None:

                self.current = self.storage.head

            else:

                self.current = self.current.next
           
    def get(self):

        values = []

        current = self.storage.head

        while current:

            values.append(current.value)

            current = current.next

        return [value for value in values if value != None]
        
        
