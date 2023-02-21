
# Write a program to create a function that takes two sorted linked lists in ascending order as input and returns a sorted linked list in ascending order. 



# Input:

#       list1= 2->1->3

#       list2=4->6->5



# Output :  sortedlist = 1->2->3->4->5->6


class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

def merge_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.value < list2.value:
        merged_head = list1
        list1 = list1.next
    else:
        merged_head = list2
        list2 = list2.next

    merged_tail = merged_head

    while list1 and list2:
        if list1.value < list2.value:
            merged_tail.next = list1
            list1 = list1.next
        else:
            merged_tail.next = list2
            list2 = list2.next
        merged_tail = merged_tail.next

    if list1:
        merged_tail.next = list1
    else:
        merged_tail.next = list2

    return merged_head

def print_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()

# Example usage:
list1 = Node(2)
list1.next = Node(1)
list1.next.next = Node(3)

list2 = Node(4)
list2.next = Node(6)
list2.next.next = Node(5)

sorted_list = merge_lists(list1, list2)
print("Sorted list:")
print_list(sorted_list)