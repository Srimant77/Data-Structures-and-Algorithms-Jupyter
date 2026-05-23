class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        iterator = self.head
        while iterator:
            print(iterator.value)
            iterator = iterator.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def pop(self):
        # Case1 - There is no element
        if not self.head:
            return None
        
        
        # Case 2 - There is one element
        elif self.head == self.tail:
            temp = self.head # we will return temp

            self.head = None
            self.tail = None
            self.length -= 1

            return temp.value
        
        # Case 3 - There is a full list
        else:
            pointer = self.head
            while pointer.next is not self.tail:
                pointer = pointer.next

            temp = self.tail # we will return temp
            self.tail = pointer
            self.tail.next = None
            self.length -= 1

            return temp.value
        
    def prepend(self, value):

        new_node = Node(value)
        
        # Case 1 - There is nothing in the list
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        # Case 2 - There are elements in the list
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True

    def pop_first(self):
        # Case 1 - There are no elements
        if self.length == 0:
            return None

        # Case 2 - There is one element
        elif self.length == 1:
            
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        # Case 3 - There are many elements
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp
        
    def get(self, index):
        # Edge case - There is nothing in the list or the index is more than the length of the list - 1
        if (self.head != None) and (index >= (self.length)):
            return None
        
        # Edge case 2 - A negative number is passed as index
        elif (index < 0):
            return None
        
        elif self.head == None:
            return None
        
        else:
            iterator = self.head
            iterator_index = 0
            while iterator_index != index:
                iterator = iterator.next
                iterator_index += 1
            return iterator
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        temp = self.get(index-1)

        new_node = Node(value)
        
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index-1)
        next_node = temp.next
        
        temp.next = next_node.next
        next_node.next = None
        self.length -= 1
        return next_node
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        if self.length == 0:
            return None
        else:       
            slow = self.head
            fast = self.head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow.value
        
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False
    
    def find_kth_from_end(self,k):
        # Setup - Get a gap of k between the slow and fast pointer
        # Assumption is that you cannot use self.length
        # Aim is to return a pointer to the kth from end node

        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is not None:
                fast = fast.next
            else:
                return None
        
        # At this stage we have created the requisite gap between fast and slow
        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow
    
    def remove_duplicates(self):
        # Remove the second instance to remove duplicates. The first instance stays
        
        list_of_keys = {}
        if self.length <= 1:
            return self
        
        temp = self.head
        after_temp = self.head.next

        # Edge case - after_temp and temp are duplicates in a list of size 2
        if (after_temp.value == temp.value) and self.length == 2:
            temp.next = None
            return self

        list_of_keys[temp.value] = True

        while after_temp is not None:
            if after_temp.value not in list_of_keys:
                list_of_keys[after_temp.value] = True
                temp = temp.next
                after_temp = after_temp.next
            else:
                duplicate_node = after_temp
                temp.next = temp.next.next
                after_temp = after_temp.next
                duplicate_node.next = None
                self.length -= 1

                if temp.next is None:
                    self.tail = temp
        
        return self

        
        






                                    



my_ll = LinkedList(1)

my_ll.append(2)

my_ll.append(3)

my_ll.append(6)

my_ll.print_list()

# print("------------------")

# print(my_ll.pop())

# print("------------------")

# print(my_ll.pop())

# print("------------------")

# print(my_ll.pop())

# print("------------------")

# my_ll.prepend(4)

# my_ll.print_list()

# print("------------------")

# print("Item removed was: ",my_ll.pop_first())

# my_ll.print_list()

# print("The get method returned:", my_ll.get(2), "for index 2")


# print("The set method returned:", my_ll.set_value(1,4), "for index 1")

# my_ll.reverse()

# print("Find middle node returned", my_ll.find_middle_node())

print("------------------")

print(my_ll.has_loop())

# ===========================================================================
# ===========================================================================
# ===========================================================================

print("Test 1: Scattered Duplicates")
ll_1 = LinkedList(1)
for val in [2, 1, 3, 2, 4]:
    ll_1.append(val)
print("Before: ", end="")
ll_1.print_list()
ll_1.remove_duplicates()
print("After:  ", end="")
ll_1.print_list()
print("-" * 30)

print("Test 2: Consecutive Duplicates (and removing the tail)")
ll_2 = LinkedList(5)
for val in [5, 5, 5]:
    ll_2.append(val)
print("Before: ", end="")
ll_2.print_list()
ll_2.remove_duplicates()
print("After:  ", end="")
ll_2.print_list()
print("-" * 30)

print("Test 3: No Duplicates")
ll_3 = LinkedList(7)
for val in [8, 9]:
    ll_3.append(val)
print("Before: ", end="")
ll_3.print_list()
ll_3.remove_duplicates()
print("After:  ", end="")
ll_3.print_list()
print("-" * 30)

print("Test 4: List of Size 2 with Duplicate (Your original edge case)")
ll_4 = LinkedList(10)
ll_4.append(10)
print("Before: ", end="")
ll_4.print_list()
ll_4.remove_duplicates()
print("After:  ", end="")
ll_4.print_list()