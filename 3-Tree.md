# Tree
Trees are a powerful type of list in coding. They are very similar to a link list however in a tree there can be multiple connections between nodes. We will only be dealing with 
**Binary Trees** where the max connection between nodes are two. 

## Structure of Binary Tree
The top of the tree is called the root. That is where the tree will start to branch off like a pyramid. In the picture below this would be the **A** value. Leafs are the nodes that have nothing connecting to them. Leafs in the pictures would be **D** and **E**. Then Binary Trees have a parent and a child node. A child is connected to a parent. And a parent is a node connected to another node. For example **B** is the parent while **D** and **E** are the child. 

![BST](Picture/Tree.jpg)

## Tree in Python
Most operations involving trees uses recursion. This being said functions are needed to preform the operations. Recursion makes the process easier because it identify and issue and makes that issue smaller. 

### 1. Inserting
The first operation is inserting into a tree. The insert function will take your value and determine if it is higher or lower than the current node it is looking at then go through each node with the same process until it finds and empty spot. A well balance tree will have a performance of O(log n) because every time it determine if the value is higher or lower it no longer has to look through that section of the list. 

### 2. Remove
The remove operation will search through the tree until it finds that specific value then remove said value. Once the item is removed from the list the function also need to adjust the tree to make sure there is no holes in the tree. The remove function can be done in O(log n) similarly to the insert performance. 

### 3. Contains
The contain function will search through the tree using recursion. The function determines if the value is higher or lower then follows that path of the subtree until it finds the data. This can be down in O(log n).

### 4. Transverse 
There are two types of transverse functions. The first being transverse forward which will go through and display the tree from smallest to largest. Or the other function being transverse backwards which will display the tree from largest to smallest. Because the transverse functions go through every item in the list this has a performance of O(n).

### 5. Height
The height function will search through the left and right subtree and determine which height is bigger. Then it will return the bigger value plus one to account for the root. This can be done in O(n) performance. 

### 6. Size and Empty
The size and if the tree is empty is all contain within the BST class. If the size is zero then we know the tree is empty. This can be done in O(1) performance. 

## Issues
Trees can be used for powerful performance with adding and removing in O(log n) time. However this is only true if you have a balance tree. You know if the tree is balance where the height from the root to the leaf of each subtree is the same. If several values are inserted that make the tree unbalance needs to be reconstructed so the tree is balance to keep that performance. 

## Example
As mention up above to do this basic functions for trees recursion is necessary. Here is an example on how to use recursion to insert a value into a tree.
```python
def insert(self, data):
    # Check to see if the BST is empty and if it
    # is then sets the value as the root. If it is
    # not empty we use recursion to find the location 
    # to place the data
    if self.root is None:
        self.root = BST.Node(data)
    else:
       self._insert(data, self.root)  # Start at the root

def _insert(self, data, node):
    if data < node.data:
        # The data belongs on the left side.
        if node.left is None:
            # We found an empty spot
            node.left = BST.Node(data)
        else:
            # Need to keep looking.  Call _insert
            # recursively on the left sub-tree.
            self._insert(data, node.left)
    else:
        #The data is equal stop looking for a spot
        if node.data == data:
            return
        # The data belongs on the right side.
        if node.right is None:
            # We found an empty spot
            node.right = BST.Node(data)
        else:
           # Need to keep looking.  Call _insert
            # recursively on the right sub-tree.
            self._insert(data, node.right)

tree = BST()
tree.insert(5) #This will insert the number 5 into the tree
```

## Problem to Solve
Trees are very fast when it comes to looking up if a value is in a tree. I am going to give you some starting code. This code will contain the BST class with a few basic functions. I need you to create a function that will find a value in a tree. Down below is the base of the program. I need you to fill in the `_contains()` function.
```python
class BST:

    class Node:

        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):      
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            #The data is equal stop looking for a spot
            if node.data == data:
                return
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    
    def __contains__(self, data):
        # This function is the "in" operation example: for i in tree:
        # Whenever the "in" operator is called it will use this function
        
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
       
        #If the value does not exist return false
        
        #If the value is in the tree return true
        
        #Else Keep looking
        pass

    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        

#Test Solution
tree = BST()
tree.insert(10)
tree.insert(8)
tree.insert(5)
tree.insert(6)
tree.insert(14)
print(8 in tree) 
print(14 in tree)   
print(75 in tree)
#EXPECTED RESULT: True True False
```

## Solution 
[Tree Solution](Python/tree_prove.py)


