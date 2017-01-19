class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


def add(anode, bnode):
  if anode == None and bnode = None:
    return None

  resultHead, resultTail = None
  carry = 0
  isFirstNode = True

  while anode != None or bnode !=None:
    sum = 0
    if anode != None:
      sum += anode.data
      anode = anode.next

    if bnode != None:
      sum += bnode.data
      bnode = bnode.next

    carry = sum/10
    val = sum %10
    newNode = Node(val)
    if isFirstNode:
      resultHead, resultTail = newNode
      isFirstNode = False
    else:
      resultTail.next = newNode

  if carry > 0:
    newNode = Node(carry)
    resultTail.next = newNode

  return resultHead






