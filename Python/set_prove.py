#Create a function that will get rid of duplicates
def create_set(list):
    #Create an empty set
    new_set = set()
    #Add each name in the list to the set
    for name in list:
        new_set.add(name)
    #Return the new set
    return new_set

#Create a function that will find intersection
def intersection(set1, set2):
    intersection_set = set1 & set2
    return intersection_set

#Test
front_door = ["James", "Frank", "Karen", "Raymond", "Dave", "Linda", "Matt", "Mathew", "Mark", "Luke", "Skywalker", "Stephanie", "Dave", "Fred", "Paul", "Raymond"]
back_door = ["Frankie", "Marco", "Frankie", "Jason", "Bob", "Mike", "Frankie", "Curtis", "Daisy", "Frankie", "Linda", "Karen", "Karen", "Ted", "Barney", "Ross"]
front_door_set = create_set(front_door)
back_door_set = create_set(back_door)
print(intersection(front_door_set, back_door_set)) #Expected: {'Karen', 'Linda'}