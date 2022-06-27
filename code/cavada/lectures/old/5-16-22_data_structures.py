"""store numberous pieces of """

"""list"""

"""tuples"""

"""dictionarys"""
# objects
# hashtable
# 

"""set"""

# removes duplicates
letters_in_mississippi = set('mississippi')
letters_in_mississippi = list(letters_in_mississippi)
print(letters_in_mississippi)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stock.pop()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
  
    def dequeue(self):
        return self.queue.pop(0)     

class Tree:
    def __init__(self, data, children=None,parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent

    def add_child(self, data):
        child = True(data, parent=self)
        self.children.append(child)



"""Graph"""

from collections import defaultdict
def Tree():
    return defaultdict(Tree)

                        #                        1
tree = Tree()           #                      / | \  
tree[1][2][5][6]        #                    2   3   4  
tree[1][3] = Tree(7)    #                    |   |    /\
tree[1][4][8]           #                    5   7   8  9
tree[1][4][9][10]       #                    |          |
                        #                    6          10


import json
print(json.dumps(tree))

"""
| Type  | Length? | Ordered? | Lookup? | Mutable? |
|-------|---------|----------|---------|----------|
| List  | Yes     | Yes      | No      | Yes      |
| Tuple | Yes     | Yes      | No      | No       |
| Dict  | Yes     | No       | Yes     | Yes      |
| Set   | No      | No       | No      | Yes      |
"""