# Set
If you do not care about order or duplication you came to the right page because Sets do not care about any of those. Sets use a special technique called **hashing**. A set is kind of like a **sparse list**. Meaning there is only one place a value can go inside the set. This is also why sets do not care about duplicates because there is only one spot. 

## Hashing
Hashing is an important tool with sets. Its like meat a potatoes, you can not have one with out the other. Python has a built in hash function to be used. Hashing is a special algorithm that converts non integer numbers into integers for the set to work on anything. 
```python
print(f"Hash of 3: {hash(3)}")
print(f"Hash of baby: {hash('baby')}")
print(f"Hash of 2594: {hash(2594)}")
print(f"Hash of hello: {hash('hello')}")
```
This code would result in:
![Hash_Code1](Picture/Hash_Code1.jpg)

Or the code can result in this:
![Hash_Code2](Picture/Hash_Code2.jpg)

Notice the string hashes changed between the two pictures. This is because the python `hash()` function will return a different value every time the code is ran. However it will stay consistent throughout the whole code. 

## Set in Python
### 1. Creating a Set
There are two ways to create an empty set in python:
```python
my_set = set() #This will create an empty set called "my_set"

my_set = {} #This will also create an empty set called my_set

#You can also create a set with values in the set
my_set = {1,2,3}
```
### 2. Adding to a Set
To add to a set you call the set name and use the `add()` function.
```Python
my_set.add(value) #This will add the value to the set
```
### 3. Removing from a Set
To remove from a set you call the set name and use the `remove()` function. 
```Python
my_set.remove(value) #This will remove the value from the set
```
### 4. Finding a Value
To find a specific value in a set we use a `if` and `in` operator.
```Python
if value in my_set: #This will check to see if the value is in the set
```
### 5. Finding the Size of the Set
To return the size of the set we use the `len()` function.
```Python
size = len(my_set) #This will determine how many items are in the set and save that value to the variable size
```
### 6. Mathematical operations
We can use sets to find the intersections (common values between two sets) and the union (combine all values in two sets).
```Python
my_set1 = {1,2,3}
my_set2 = {2,3,4}

#Find the intersection
my_set3 = intersection(my_set1, my_set2) #Returns {2,3}
#OR another way to write the function is:
my_set3 = my_set1 & my_set2 #Returns {2,3}

#Find the Union
my_set3 = union(my_set1, my_set2) #Returns {1,2,3,4}
#OR another way to write the function is:
my_set3 = my_set1 | my_set2 #Returns {1,2,3,4}
```
## Performance and Usage
The reason sets are so powerful because of their fast performance. The above operations can all be down in O(1) performance. This allows the user to create a set where they can look up a value, find unique results, and perform mathematical operations 

## Conflicts

## Example

## Problem to Solve