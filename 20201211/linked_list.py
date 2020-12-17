class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        temp_head = self.head
        current = 0
        while temp_head:
            if current == index:
                return temp_head.val
            temp_head = temp_head.next
            current += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head = ListNode(val=val, next=self.head)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = ListNode(val=val)
        if not self.head:
            self.head = node
        temp_head = self.head
        while temp_head:
            if not temp_head.next:
                temp_head.next = node
                break
            temp_head = temp_head.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = ListNode(val=val)
        if index == 0:
            node.next = self.head
            self.head = node
        current = 0
        temp_head = self.head
        while temp_head:
            if current == index - 1:
                node.next = temp_head.next
                temp_head.next = node
                break
            temp_head = temp_head.next
            current += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
        current = 0
        temp_head = self.head
        while temp_head:
            if current == index - 1:
                if temp_head.next:
                    temp_head.next = temp_head.next.next
                break
            temp_head = temp_head.next
            current += 1
