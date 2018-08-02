#Tested locally with Python 2.6.2 on OS X 10.6.0
words = []

input = open('A-small.in','r')
output = open('A-small.out','w')
nums = input.next().split(' ')
L = int(nums[0])
D = int(nums[1])
N = int(nums[2])

words = []
for i in range(0,D):
    words.append(input.next()[0:L])

for i in range(0,N):
    tokens = []
    possible = 0
    inToken = False
    counter = 0
    for j in range(0,L):
        tokens.append("")
    for char in input.next():
        if counter == L:
            break
        if char is '(':
            inToken = True
            continue
        if char is ')':
            inToken = False
            counter+=1
            continue
        if inToken is True:
            tokens[counter]+=char
        if inToken is False:
            tokens[counter]+=char
            counter+=1
    for word in words:
        counter = -1
        truth = True
        for char in word:
            counter += 1
            if char not in tokens[counter]:
                truth = False
                break
        if truth is True:
            possible+=1
    output.write("Case #"+str(i+1)+": "+str(possible)+"\n")

        
