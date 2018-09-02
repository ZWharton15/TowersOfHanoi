#basic data structures library

class Node():
    
    def __init__(self, value, linked_node=None):
        self.value = value
        self.linked_node = linked_node
    
    def set_next_node(self, linked_node):
        self.linked_node = linked_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.linked_node

class Stack:
    def __init__(self, name=None, limit=99):
        self.top_item = None
        self.size = 0
        self.limit = limit
        self.name = name
  
    def push(self, value):
        if self.has_space():
          item = Node(value)
          item.set_next_node(self.top_item)
          self.top_item = item
          self.size += 1
        else:
          print("Stack limit reached")

    def pop(self):
        if not self.is_empty():
          item_to_remove = self.top_item
          self.top_item = item_to_remove.get_next_node()
          self.size -= 1
          return item_to_remove.get_value()
        else:
          print("No items on stack")
  
    def peek(self):
        if not self.is_empty():
        	    return self.top_item.get_value()
        else:
          print("No items on stack")
      
    def has_space(self):
        return self.limit > self.size
  
    def is_empty(self):
        return self.size == 0
    
    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    
    def get_all_items(self):
        pointer = self.top_item
        item_list = []
        while pointer:
            item_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        item_list.reverse()
        return item_list