
import Node 

n1 = Node.Node("hat")
n2 = Node.Node("scarf")
n3 = Node.Node("gloves")
n4 = Node.Node("thermals")
n5 = Node.Node("socks")

# Set and get next values. Have the nodes reference each other. 
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n5)
# n1 is head 
# n1 -> n2 -> n3 -> n4 -> n5 -> None
print("\nGet data and pointers off our nodes:")
print(n1.get_data()) # hat 
print(n5.get_data()) # socks 
print(n1.get_next()) # scarf
print(n5.get_next()) # None (hit end of list)

# Write a loop that walks through a list of nodes
# 1. Iterate over a list of your nodes
print("\nIterate over the list:")
nodes = [n1,n2,n3,n4,n5]
for node in nodes:
    print(node)

# 2. Use the "head"
print("\nPrinting starting at the head:")
node = n1
while node: 
    print(node.get_data())
    # debug statement
    # print("{0} -> {1}".format(node.get_data(), node.get_next()))
    node = node.get_next() # This works because the last node points to Next 
