class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def deleteNode(head,key):
    if head and head.data==key:
        return head.next
    
    curr=head
    while curr and curr.next:
        if curr.next.data==key:
            curr.next=curr.next.next
            break
        curr=curr.next
    return head

def insertatpos(head,key,data): #insert after key
    curr=head
    while curr:
        if curr.data==key:
            nNode=Node(data)
            nNode.next=curr.next
            curr.next=nNode
            break
        curr=curr.next
    return head

def traversal(head):
    curr=head
    while curr:
        print(curr.data, end="->")
        curr=curr.next

head=Node(1)
head.next=Node(3)
head.next.next=Node(2)
head.next.next.next=Node(10)
head.next.next.next.next=Node(100)

head=deleteNode(head,999)
head=insertatpos(head,2,55)

traversal(head)