# Implement Linked List. Include options for insertion, deletion and search of a
# number, reverse the list and concatenate two linked lists

# singly linkedlist
class Node1: 

    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
        
    def display(self):
        print(self.element)

class LinkedList:
        
    def __init__(self):
        self.head = None
        self.size = 0
        
        
    def __len__(self):
        return self.size
    
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
#         return "Displaying list"
        if self.size ==0:
            print("no element")
            
        first = self.head
        print(first.element)
        first = first.next
        while first:
            
            print(first.element)
            first = first.next
    
    
    def add_head(self,e):
        temp = self.head 
        self.head = Node1(e) 
        self.head.next = temp
        self.size += 1
        
    
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None ):
            last_object = last_object.next
        return last_object
    
        
    def remove_head(self):
        if self.is_empty():
            print("empty")
        else:
            print("removing head")
            self.head =  self.head.next
            self.size -=1
            
    def add_tail(self, e):
        new_value = Node1(e)
        self.get_tail().next = new_value
        self.size += 1
        
    def find_second_last_el(self):
        #second_last_el = None
        
        if self.size >= 2:
            first = self.head
            temp_counter = self.size - 1
            while temp_counter > 1:
                first = first.next
                temp_counter -= 1
            return first
                
        else:
            print("size not sufficient")
        return None

        
    def remove_tail(self):
        if self.is_empty():
            print("empty singly linked list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else:
            Node1 = self.find_second_last_el()
            if Node1:
                Node1.next = None
                self.size -= 1
                
    def get_Node1_at(self, index):
        el_Node1 = self.head
        counter = 0
        if index > self.size-1:
            print("index out of bound")
            return None
        while(counter < index):
            el_Node1 = el_Node1.next
            counter +=1
        return el_Node1
    
    def remove_between_list(self, position):
        if position > self.size - 1:
            print("index out of bound")
        elif position == self.size-1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_Node1 = self.get_Node1_at(position - 1)
            next_Node1 = self.get_Node1_at(position + 1)
            prev_Node1.next = next_Node1
            self.size -= 1
            
            
    def add_between_list(self,position, element):
        if position > self.size:
            print("index out of bound")
        elif position == self.size:
            self.add_tail(element)
        elif position ==0:
            self.add_head(element)
        else:
            prev_Node1 = self.get_Node1_at(position - 1)
            current_Node1 = self.get_Node1_at(position)
            prev_Node1.next = element
            element.next = current_Node1
            self.size -= 1
            
            
    def search(self, search_value):
        index = 0
        while(index < self.size):
            value = self.get_Node1_at(index)
            print("searching at "+ str(index)+ " and val is "+str(value.element))
            if value.element == search_value:
                print("found")
                return True
            index +=1
        print("not found")
        return False
        
        
        
    def merge(self, linkedlist_value):
        if self.size > 0:
            last_Node1 = self.get_Node1_at(self.size - 1)
            last_Node1.next = linkedlist_value.head
            self.size = self.size + linkedlist_value.size
        else:
            
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size

print("Linked List\n")
     
print("\n1 .  Singly linked list\n")
sy = LinkedList()
print("adding elements\n")
sy.add_head(6)
sy.add_head(5)
sy.add_head(4)
sy.add_tail(3)
sy.add_tail(2)
sy.add_tail(1)
print("final list\n")
sy.display()


sy.remove_head()
print("\nfinal list\n")
sy.display()

sy.remove_tail()
print("\nremoving tail : final list\n")
sy.display()

print("\nget node at 1 \n")
sy.get_Node1_at(1).display()

print("\nremove between list :1 \n")
sy.remove_between_list(0)
print("\nfinal list\n")
sy.display()

print("\nsearching 3 in list\n")
sy.search(3)

print("\nadding elements in list2\n")
fy = LinkedList()
fy.add_head(22)
fy.add_head(55)
fy.add_tail(11)
print("\nfinal list\n")
fy.display()

sy.merge(fy)
print("merging 2 lists\n")
sy.display()



# doubly linkedlist


class Node:
    
    
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
        
        
class DoublyLinkedList:
    
    
    def __init__(self):
        self.head = None
           
    def add_head(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            print("node inserted")
            return
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def add_tail(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            new_node = Node(data)
            n.next = new_node
            new_node.prev = n
            new_node.next = None
        
    def traverse_list(self):      # same as display() function
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.item)
                n = n.next
                
    def remove_head(self):
        if self.head is None:
            print("List is empty")
            return 
        elif self.head.next is None:
            self.head = None
            return
        else:
            self.head = self.head.next
        
        
    def remove_tail(self):
        if self.head is None:
            print("List is empty")
            return 
        elif self.head.next is None:
            self.head = None
            return
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prev.next = None
        
        
    def reverse_linked_list(self):     
        if self.head is None:
            print("List is empty")
            return 
        else:
            p = self.head
            q = p.next
            p.next = None
            p.prev = q
            while q is not None:
                q.prev = q.next
                q.next = p
                p = q
                q = q.prev
            self.head = p

    
            
print("\n2.  Doubly linked list\n")
print("\nadding elements\n")
l1 = DoublyLinkedList()

l1.add_head('b')

l1.add_head('c')

l1.add_tail('d')
print("\nfinal list\n")

l1.traverse_list()

print("\nremoving head: final list\n")
l1.remove_head()

l1.traverse_list()

print("\nremoving tail : final list\n")
l1.remove_tail()

l1.traverse_list()

print("\nadding elements\n")
l1.add_head('c')
l1.add_head('e')
l1.add_tail('f')
print("\nfinal list\n")
l1.traverse_list()

print("\nreversed list\n")
l1.reverse_linked_list()

l1.traverse_list()






