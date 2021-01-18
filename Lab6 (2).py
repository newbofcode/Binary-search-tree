# Yong He
# 500570639

# LAB INSTRUCTIONS

# Add your name and student number in the comments above
# Complete the code for the following Binary Search Tree class
# You must complete the following methods:
# - insert: Add an element to the BST and maintain the BST characteristic
# - delete: Delete an element from the BST and maintain the BST characteristic
#           Must be able to handle 3 cases:
#               - Node deleted has no children
#               - Node deleted has one child
#               - Node deleted has two children
# - getMinimum: Return the minimum value in the tree
# - getMaximum: Return the maximum value in the tree
# - getHeight: Return the height of the tree
# - __str__: Returns a string representation of the nodes of the tree in order. Should not contain any new lines. Values should be seperated by a ", "

# You may add helper methods if needed.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # YOUR CODE STARTS HERE
    def insert(self, value):
        if value == self.value:
            return
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                 return self.left
            lastvalue = self.right.getMinimum()
            self.value = lastvalue
            self.right = self.right.delete(lastvalue)
        return self
    def getMinimum(self):
        if self.left is None:
            return self.value
        return self.left.getMinimum()
    def getMaximum(self):
        if self.right is None:
            return self.value
        return self.right.getMaximum()
    def getHeight(self):
        if self.left and self.right:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        elif self.left:
            return 1 + self.left.getHeight()
        elif self.right:
            return 1 + self.right.getHeight()
        else:
            return 1
    def __str__(self):
        str1 = ""
        if self.left:
            str1+=str(self.left.__str__())
        str1+= str(self.value) +", "
        if self.right:
            str1+=str(self.right.__str__())
        return str1
    # YOUR CODE ENDS HERE

    

# DO NOT CHANGE THE FOLLOWING CODE
# Tests
tree = BST(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
print(tree) # Expected output: "1, 2, 3, 4, 5, "

tree = BST(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(7)
print(tree) # Expected output: "1, 2, 3, 4, 5, 6, 7 "
print(tree.left) # Expected output: "1, 2, 3, "
print(tree.right) # Expected output: "5, 6, 7, "

print(tree.getMinimum()) # Expected output: "1"
print(tree.getMaximum()) # Expected output: "7"
print(tree.getHeight()) # Expected output: "3"

tree.delete(7)
print(tree) # Expected output: "1, 2, 3, 4, 5, 6, "
tree.delete(6)
print(tree) # Expected output: "1, 2, 3, 4, 5, "
tree.delete(2)
print(tree) # Expected output: "1, 3, 4, 5, "

