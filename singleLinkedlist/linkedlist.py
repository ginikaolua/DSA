class Node:
    def __innit__(self, data = None, next = None):
        self.data = data
        self.next = next

class linkedList:
    def __innit__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.next = newNode
        self.length = 1

    def insert_at_end(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length +=1
    def get(self, index):
       if(index < 0 or index >= self.length):
            print('out of bounds')
            return
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp


    def set(self,index,value):
        node = set.get(index)
        node.data = value
        return self

    def insert(self,index,value):
        node = self.get(index)
        node.data = value
        return self

    def remove(self, index):



        
        
        

        