class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr_node = self.head.next
        cnt = 0
        while (curr_node != None):
            if (cnt == index):
                return curr_node.val
            cnt += 1
            curr_node = curr_node.next
        return -1

    def insertHead(self, val: int) -> None:
        insert_node = Node(val)
        insert_node.next = self.head.next
        self.head.next = insert_node
        
        if insert_node.next == None:
            self.tail = insert_node

    def insertTail(self, val: int) -> None:
        insert_node = Node(val)
        self.tail.next = insert_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr_node = self.head
        cnt = 0
        while cnt < index and curr_node != None:
            cnt += 1
            curr_node = curr_node.next
    
        # curr_node -> node right before index
        if curr_node != None and curr_node.next != None:
            if curr_node.next == self.tail:
                self.tail = curr_node
            curr_node.next = curr_node.next.next
            return True
        return False    

    def getValues(self) -> List[int]:
        curr_node = self.head.next
        values = []
        while (curr_node != None):
            values.append(curr_node.val)
            curr_node = curr_node.next
        return values
