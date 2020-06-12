class RingBuffer:
    def __init__(self, capacity):

        self.capacity = capacity

        self.size = 0

        self.storage = []

        self.counter = 0
               

    def append(self, item):

        if self.size < self.capacity:

            self.storage.append(item)

            self.size += 1

        else:

            self.storage[self.counter] = item

            if self.counter < self.capacity -1:

                self.counter  += 1

            else:

                self.counter = 0


    def get(self):
        
        return [item for item in self.storage if item != None]
