import Stack 

# Make a stack object 
s = Stack.Stack() 
print(s.is_empty()) # We just created it, its empty
print(s)
s.push('carrots')
print(s)
s.push('tomato')
s.push('bittermelon')
print(s)

# Whats at the top of the stack of snack veggies?
s.peek() # should be delicious bittermelon 
print(s.size())
print(s.pop()) # bye bye bittermelon
print(s.pop()) # bye bye tomato 
print(s.pop()) # bye bye carrots 
print(s.size())

# Nothing in the stack of snack
print(s)

# But what if we pop what is not there? 
print(s.pop()) # Index error, list is empty