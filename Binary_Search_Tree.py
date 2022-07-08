
class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.node_value = value
      self.left_child = None
      self.right_child = None
      self.height = None

  def __init__(self):
    self.__root = None
    self.__leaf_value = None

  def __height(self, t):
    if t.left_child and t.right_child:
        if t.left_child.height > t.right_child.height:
          return t.left_child.height +1
        else:
          return t.right_child.height+1
    elif t.left_child:
      return t.left_child.height+1
    elif t.right_child:
      return t.right_child.height + 1
    else:
      return 1

  def __balance_value(self, t):
    #finds the balance of a given node
    if t and t.right_child:
        if t.left_child:
            balance = t.right_child.height -  t.left_child.height
        else:
            balance = t.right_child.height
    elif t and t.left_child:
        balance = -t.left_child.height
    else:
        balance = 0
    return balance

  def __balance(self, t):
    if abs(self.__balance_value(t)) != 2: #the node is balanced
       return t
       
    if self.__balance_value(t) == -2:                   #the node has a heavy left child
      if self.__balance_value(t.left_child) > 0:        #the left child's children are skewed to the right (need straightening)
        t.left_child = self.__right_balance(t.left_child)
        t = self.__left_balance(t)
        return t 
      else:                                             #the left child's children are skewed to the left
        t = self.__left_balance(t)
        t.height = self.__height(t)
        return t 
    else:                                                  #the node has a heavy right child
      if self.__balance_value(t.right_child) < 0:          #the right child's children are skewed to the left (need straightening)
        t.right_child = self.__left_balance(t.right_child)
        t = self.__right_balance(t)
        return t 
      else:                                                #the right child's children are skewed to the right
        t = self.__right_balance(t)
        t.height = self.__height(t)
      return t

  def __left_balance(self, t):
    temp = t.left_child
    t.left_child = temp.right_child
    temp.right_child = t
    #height
    temp.right_child.height = self.__height(temp.right_child)
    temp.height = self.__height(temp)
    return temp

  def __right_balance(self, t):
    temp = t.right_child
    t.right_child = temp.left_child
    temp.left_child = t
    #height
    temp.left_child.height = self.__height(temp.left_child)
    temp.height = self.__height(temp)
    return temp


  def insert_element(self, value):
    # "less is left; greater is right"
    #If the value is already contained in the tree, raise a ValueError. 
    self.__root = self.__recursive_insert(value, self.__root)
    self.__root = self.__balance(self.__root)

  def __recursive_insert(self, value, t):
    if t is None:
      new_node = self.__BST_Node(value)
      new_node.height = 1
      return new_node

    if value > t.node_value:
      t.right_child = self.__recursive_insert(value, t.right_child)
      t = self.__balance(t)
      t.height = self.__height(t)
      return self.__balance(t)
    elif value < t.node_value:
      t.left_child = self.__recursive_insert(value, t.left_child)
      t = self.__balance(t)
      t.height = self.__height(t)
      return self.__balance(t)

    else:
      raise ValueError
    


  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement.
    self.__root = self.__recursive_removal(value, self.__root)
    self.__root = self.__balance(self.__root)

  def __recursive_removal(self, value, t):
    #value not found in whole tree
    if not t:
      raise ValueError

    #value located, deals with value's children
    elif t.node_value == value:
      if t.right_child and not t.left_child:
        return t.right_child
      elif t.left_child and not t.right_child:
        return t.left_child
    #If the value has two children then the...
    #right child's left-most leaf replaces the node being removed
      elif t.left_child and t.right_child:
        t.right_child = self.__double_child_recursion(t.right_child)
        t.node_value = self.__leaf_value 
        t.height = self.__height(t)
        return t

    #still searching for value
    elif value > t.node_value:
      t.right_child = self.__recursive_removal(value, t.right_child)
      t.height = self.__height(t)
      return t
    elif value < t.node_value:
      t.left_child = self.__recursive_removal(value, t.left_child)
      t.height = self.__height(t)
      return t

  def __double_child_recursion(self, t):
      if t.left_child:
        t.left_child = self.__double_child_recursion(t.left_child)
        t.height = self.__height(t)
        return t
      else:
        self.__leaf_value = t.node_value 
        return t.right_child

    

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    if self.__root is None:
      return '[ ]'
    self.__concatenation = '[ '
    self.__recursive_in_order(self.__root)
    self.__concatenation = self.__concatenation[0:len(self.__concatenation)-2]
    return self.__concatenation + ' ]'
  def __recursive_in_order(self, t):
    if t:
      self.__recursive_in_order(t.left_child)
      self.__concatenation += str(t.node_value) +', '
      self.__recursive_in_order(t.right_child)
    return
    
  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    if self.__root is None:
      return '[ ]'
    self.__concatenation = '[ '
    self.__recursive_pre_order(self.__root)
    self.__concatenation = self.__concatenation[0:len(self.__concatenation)-2]
    return self.__concatenation + ' ]'
  def __recursive_pre_order(self, t):
    if t:
      self.__concatenation += str(t.node_value) +', '
      self.__recursive_pre_order(t.left_child)
      self.__recursive_pre_order(t.right_child)

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    if self.__root is None:
      return '[ ]'
    self.__concatenation = '[ '
    self.__recursive_post_order(self.__root)
    self.__concatenation = self.__concatenation[0:len(self.__concatenation)-2]
    return self.__concatenation + ' ]'
  def __recursive_post_order(self, t):
    if t:
      self.__recursive_post_order(t.left_child)
      self.__recursive_post_order(t.right_child)
      self.__concatenation += str(t.node_value) +', '

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root:
      return self.__root.height
    else:
      return 0

  def __str__(self):
    return self.in_order()

  def to_list(self):
    self.__tree_list = []
    self.__recursive_to_list(self.__root)
    return self.__tree_list
  def __recursive_to_list(self, t):
    if t:
      self.__recursive_to_list(t.left_child)
      self.__tree_list.append(t.node_value)
      self.__recursive_to_list(t.right_child)



if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
  