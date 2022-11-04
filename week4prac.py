# list
friends = ['Suha', 'Saira', 'Sana']
for friend in friends:
	print('Assalam-Olaikum ', friend)
print('Best wishes to you all!')	
print()
print(len(friends))
print()
print(range(len(friends)))





# Manipulation Lists
print()
# Concatenating Lists using +
print('Added new friend using +')
newFriends = ['Md', 'Suhel', 'Rana']

allFriends = friends + newFriends

print(allFriends)


# Lists can be sliced using:
print()
print('Lists can be sliced using:')
a = [9, 23, 34, 54, 39, 87, 90, 35, 74, 66]
print(a[1 : 4]) # upto index 4 but not including

print()
print(a[:5])

print()
print(a[:])

# Append which add things end of the list

# Creating a list from scratch and adding items using append method
print()
print('Created a list from scratch!')
b = list()
b.append('book')
b.append('99')
print(b)
b.append('love')
print('added the word love using append method!')
print(b)

# Is something in a list

print()
print('Looking for somrthing inside a list')
'book' in b
# if it is there then True if not False

# list to sort, here we had to make 99 as string because int and str can't sort.
print()
print('sorting list')
b.sort()
print(b)

print()
print('Built in function of list under variable a:')
print('Length of a variable list', len(a))
print('Max in a')
print('Min in a')
print('Sum of a')


Print('test for git')

print('test for new things after uploading into github through command line')

print('2nd update from github')
print('update from local machine line 77')