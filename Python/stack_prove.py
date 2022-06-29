def add(sentence):
    stack = []
    #Add characters to the stack
    for char in sentence:
        stack.append(char)
    return stack

def undo(stack):
    #If the stack is empty do not do anything
    if len(stack) == 0:
        return
    else:
        stack.pop()


#Test Cases
#Test 1
#Take a sentence and add to the stack
print("TEST 1")
sentence = "This is a test sentence"
stack = add(sentence)
print(stack) #Expected outcome ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e']
print("---------------")
print()

#Test 2
#The user wants to undo several characters and is left
#with the new sentence
print("TEST 2")
sentence = "This is a test sentence"
stack = add(sentence)
undo(stack)
undo(stack)
undo(stack)
undo(stack)
undo(stack)
undo(stack)
print(stack) #Expected outcome ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 's', 'e']
print("---------------")
print()

#Test 3
#Create a test scenario for when the user tries to undo from an
#empty stack
print("TEST 3")
sentence = "One"
stack = add(sentence)
undo(stack)
undo(stack)
undo(stack)
undo(stack)
print(stack) #Expected outcome []