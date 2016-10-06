#A ray of light comes in from the upper left corner of an MxN sized window, with 45˚ angled edges.
#The ray is reflected when it reaches the first or the last line, or the first or last column respectively.
#Display all the positions reached until the ray travels to a window corner.

#Input: M and N integers
#Output: matrix of MXN with the positions

#Example: 
#For M = 4 and N = 8 the reached positions are the following:
#The ray of light reaches the bottom right corner.
#Output for console should be the following:
#1,0,13,0,19,0,7,0
#0,2,0,12,0,6,0,8
#15,0,3,0,5,0,9,0
#0,16,0,4,0,10,0,22

import sys


##Emulate reading from a file
##--------------------------------------------------------------------------------------------------------------------
new_file = open('text.txt', "w")
new_file.write("4\n")
new_file.write("8\n")
new_file.close()
##--------------------------------------------------------------------------------------------------------------------


f = open('text.txt', 'r')   #sys.argv[1]
n =  int(f.readline())
m = int(f.readline())

v = []
#set up grid
for i in range(0,n):
    v.append([])
    for j in range(0,m):
        v[i].append(0)

##My code
##==================================================================================================================================
#limits of grid
#print(    v[n-1][m-1]    )

corner = False
pastn = 0
pastm = 0
currentn = 0
currentm = 0
currentdirection = "br"
counter = 2
v[0][0] = 1

while corner == False:
	#set currentn/m based on currentdirection and pastn/m
	if currentdirection == "tl":
		currentn = pastn -1
		currentm = pastm -1
	elif currentdirection == "tr":
		currentn = pastn -1
		currentm = pastm +1
	elif currentdirection == "bl":
		currentn = pastn +1
		currentm = pastm -1
	elif currentdirection == "br":
		currentn = pastn +1
		currentm = pastm +1

	#set current cell contents to keep track of path
	if ( (currentn >= 0 and currentn < n) and (currentm >= 0 and currentm < m) ):
		if v[currentn][currentm] == 0:
			v[currentn][currentm] = counter
		counter +=1

	#end loop or
	#check next cell in the currentdirection is valid
	if ( (currentn == 0 and (currentm == 0 or currentm == m-1)) or (currentn == n-1 and (currentm == 0 or currentm == m-1)) ):
		corner == True
		break
	elif currentdirection == "br":
		if currentn == n-1 and currentm < m:
			currentdirection = "tr"
		elif currentm == m-1 and currentn < n:
			currentdirection = "bl"
	elif currentdirection == "bl":
		if currentn == n-1 and currentm < m:
			currentdirection = "tl"
		elif currentm == 0 and currentn < n:
			currentdirection = "br"
	elif currentdirection == "tl":
		if currentn == 0 and currentm < m:
			currentdirection = "bl"
		elif currentm == 0 and currentn < n:
			currentdirection = "tr"
	elif currentdirection == "tr":
		if currentn == 0 and currentm < m:
			currentdirection = "br"
		elif currentm == m-1 and currentn < n:
			currentdirection = "tl"

	#keep data current
	pastn = currentn
	pastm = currentm
###==================================================================================================================================

for i in v:
    s = ''
    for j in range(0, len(i)-1):
        s += str(i[j]) + "\t"
    j += 1
    s += str(i[j])
    print(s)
