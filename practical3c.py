# WAP to scan a polynomial using linked list and add two polynomial.


class Node: 
    

    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
        
    def display(self):
        print(self.element)


class LinkedList:
    
        
    def __init__(self):
        self.head = None
        self.size = 0
        
    def _len_(self):
        return self.size
    
    def get_head(self):
        return self.head
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size ==0:
            print("no element")
        first = self.head
        print(first.element.element)
        first = first.next
        while first:
            print(first.element)
            first = first.next
            
    def add_head(self,e):
        temp = self.head 
        self.head = Node(e)
        self.head.next = temp
        self.size += 1 
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
        
    def remove_head(self):
        if self.is_empty():
            print("Empty Singly linked list")
        else:
            print("Removing")
            self.head = self.head.next
            self.size -= 1
            
    def add_tail(self,e):
        new_value = Node(e)
        self.get_tail().next = new_value
        self.size += 1
        
    def find_second_last_element(self):
        if self.size >= 2:
            first = self.head 
            temp_counter = self.size -2
            while temp_counter > 0:
                first = first.next 
                temp_counter -= 1 
            return first  
        else:
            print("Size not sufficient")      
        return None

    def remove_tail(self):
        if self.is_empty():
            print("Empty Singly linked list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else: 
            Node = self.find_second_last_element()
            if Node:
                Node.next = None
                self.size -= 1
                
    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index == 0:
            return element_node.element
        if index > self.size-1:
            print("index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter +=1
        return element_node
                  
    def remove_between_list(self,position):
        if position > self.size - 1:
            print("index out of bound")
        elif position == self.size-1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(position - 1)
            next_node = self.get_node_at(position + 1)
            prev_node.next = next_node
            self.size -= 1
            
    def add_between_list(self,position,element):
        if position > self.size:
            print("index out of bound")
        elif position == self.size:
            self.add_tail(element)
        elif position ==0:
            self.add_head(element)
        else:
            prev_node = self.get_node_at(position - 1)
            current_node = self.get_node_at(position)
            prev_node.next = element
            element.next = current_node
            self.size -= 1
        
    def search(self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            if value.element == search_value:
                return value.element
            index += 1
        print("Not Found")
        return False
    
    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size - 1)
            last_node.next = linkedlist_value.head
            self.size = self.size + linkedlist_value.size
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size
            

order = 3

list1 = LinkedList()
print("Polynomial 1:")

list1.add_head(Node(int(input(f"coefficient for power {order} : "))))
for i in reversed(range(order)):
    list1.add_tail(int(input(f"coefficient for power {i} : ")))
    
list2 = LinkedList()
print("Polynomial 2")

list2.add_head(Node(int(input(f"coefficient for power {order} : "))))
for i in reversed(range(order)):
    list2.add_tail(int(input(f"coefficient for power {i} : ")))

print("Adding cooeficients of polynomial 1 and 2 ")
print(list1.get_node_at(0).element + list2.get_node_at(0).element, "x^3 + " , 
         list1.get_node_at(1).element + list2.get_node_at(1).element, "x^2 + ",
         list1.get_node_at(2).element + list2.get_node_at(2).element, "x + ",
         list1.get_node_at(3).element + list2.get_node_at(3).element)




