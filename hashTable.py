

class hashTable:
  def __init__(self): 
    self.length  = 1700
    self.size= 0
    self.myArray = [None]* self.length  
  
  def insert(self, key, value):
    # 1. Increment size
    self.size += 1
    # 2. Compute index of key
    index = self.hash(key)
    # Go to the node corresponding to the hash
    node = self.myArray[index]
    # 3. If bucket is empty:
    if node is None:
      # Create node, add it, return
      self.myArray[index] = Node(key, value)
      return
    # 4. Collision! Iterate to the end of the linked list at provided index
    prev = node
    while node is not None:
      prev = node
      node = node.next
    # Add a new node at the end of the list with provided key/value

    prev.next = Node(key, value)

  def find(self, key):
    # 1. Compute hash
    index = self.hash(key)
    # 2. Go to first node in list at myarray
    node = self.myArray[index]
    # 3. Traverse the linked list at this node
    while node is not None and node.key != key:
      node = node.next
    # 4. Now, node is the requested key/value pair or None
    if node is None:
      # Not found
      return None
    else:
      # Found - return the data value
      return node.value

  def hash(self, key):
    hashSum=0
    hashSum = int(key) %(self.length)
    return hashSum



class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None





vaccineTable = hashTable()
# Create some data to be stored

user_one = ["Marina Amorim", "21","Moderna", "06/17/2000"]
# Insert our data under the key "phoneDirectory"

vaccineTable.insert("0001", user_one)
# Do whatever we need with the phone_numbers variable

user_one = None
... # Later on...

user_two = ["test", "21","Moderna", "06/17/2000"]
# Insert our data under the key "phoneDirectory"

vaccineTable.insert("2000", user_two)
# Do whatever we need with the phone_numbers variable

user_two = None
... # Later on...

# Retrieve the data we stored in the HashTable

user_one = vaccineTable.find("0001")
user_two = vaccineTable.find("2000")
# find() retrieved our list object

# phone_numbers is now equal to ["555-555-5555", "444-444-4444"]


