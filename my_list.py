class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None #next의 초기 value는 아무것도 가리키지 않음
head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)


#iterative
def printNodes(node:ListNode):
  crnt_node = node
  while crnt_node is not None: #crnt_node가 존재할때
    print(crnt_node.val, end=' ')
    crnt_node = crnt_node.next #마지막노드 None을 가리키며 종료

printNodes(head_node)

#recursive
def printNodesRecur(node:ListNode):
  print(node.val, end=' ')
  if node.next is not None:
    printNodesRecur(node.next)

printNodesRecur(head_node)

class SLinkedList:
  def __init__(self):
    self.head = None

  def addAtHead(self, val): #O(1)
    node = ListNode(val)
    node.next = self.head #새로만들어진 node의 next에 head가 가리키고 있던 곳을 넣어줌
    self.head = node #head는 새롭게 만들어진 node를 가리킴

  def addBack(self, val): #O(n)
    node = ListNode(val)
    crnt_node = self.head
    while crnt_node.next:
      crnt_node = crnt_node.next
    crnt_node.next = node

  def findNode(self, val): #O(n)
    crnt_node = self.head
    while crnt_node is not None:
      if crnt_node.val == val:
        return crnt_node
      crnt_node = crnt_node.next
    raise RuntimeError('Node not found')

  def addAfter(self, node, val): #O(1)
    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node

  def deleteAfter(self, prev_node): #O(1)
    if prev_node.next is not None:
      prev_node.next = prev_node.next.next

  def recursive(self, node:ListNode) -> ListNode:
    if not node:
      return None
    next_node = self.recursive(node.next)
    if node.val == self.__val:
      return next_node
    else:
      node.next = next_node
      return node

slist = SLinkedList()
slist.addAtHead(1)
slist.addAtHead(2)
slist.addBack(3)


node1 = slist.findNode(1)
slist.addAfter(node1, 4)

printNodes(slist.head)
