
'''
Building Bank Queue with User Inputted Names:
'''

names = []
for x in range(10):
    acceptedName = input("Enter a name: ")
    names.append(acceptedName)
    

'''
Dequeue / Pop Names:
'''
print(" ")
for x in range(10):
    print(names.pop(0))
