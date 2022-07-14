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
        if node is None:
            return False
        #If the value is in the tree return true
        if node.data == data:
            return True
        #Else Keep looking
        else:
            if data < node.data:
                return self._contains(data, node.left)
            elif data > node.data:
                return self._contains(data, node.right)

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