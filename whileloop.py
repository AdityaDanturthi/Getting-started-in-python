#Simple while loop for printing Hello World 5 times"
i=0
while (i < 5):
    print("Hello World!")
    i += 1

#While loop for travering an array (Pop function removes the last element in the array first)
arr = [1,2,3,4,5,6,7,8,9,10]
while arr:
    print(arr.pop())

#While loop using continue keyword
# Prints all letters except 'a' and 't'
i=0
name= 'aditya'
while i<len(name):
    if name[i]=='a' or name[i]=='t':
        i += 1
        continue

    print('Current letter: ',name[i])
    i += 1



