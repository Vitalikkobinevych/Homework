class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def __eq__(self, other):
        return self.data == other

    def __int__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def append(self, new_node):
        if self.head:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next

            temp_node.next = new_node
        else:
            self.head = new_node

    def remove_duplicates(self):

        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head

        # Pick elements one by one
        while (ptr1 != None and ptr1.next != None):

            ptr2 = ptr1

            # Compare the picked element with rest
            # of the elements
            while (ptr2.next != None):

                # If duplicate then delete it
                if (ptr1.data == ptr2.next.data):

                    # Sequence of steps is important here
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next

            ptr1 = ptr1.next

    def display(self):
        temp_node = self.head
        if temp_node:
            while temp_node is not None:
                print(temp_node.data, end=" ")
                temp_node = temp_node.next
        else:
            print("Empty list")

    def is_empty(self):
        return self.head is None

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        pos = 0
        current = self.head
        if self.__len__() <= index:
            print('not such index')
            return None
        while pos is not index:
            current = current.next
            pos += 1
        return current.data

    def insert_at_end(self, item):
        if self.is_empty():
            self.append(item)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(item,None)

    def insert(self, item, position):
        position = position-1
        if position > self.__len__() or position < 0:
            print('Enter pos correctly')
            return None
        if position == 0:
            self.head = Node(item, self.head)
        elif position == self.__len__():
            self.insert_at_end(item)
        else:
            i = 0
            current = self.head
            while current.next:
                if i == position - 1:
                    current.next = Node(item, current.next)
                current = current.next
                i += 1

    def delete(self, position):
        position = position - 1
        if position > self.__len__() or position < 0:
            print('Enter pos correctly')
            return None

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def clear(self):
        temp = self.head
        if temp is None:
            raise IndexError('Empty list')
        while temp:
            self.head = temp.next
            temp = self.head


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

