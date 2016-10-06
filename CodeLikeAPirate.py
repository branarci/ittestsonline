#Find the largest perimeter of 1's in a grid
#and display the starting co-ordinates (top left corner of rectangle)

import sys

def convert_int(l):
    convert_l = []
    for i in l:
        convert_l.append(int(i))
    return convert_l


##Emulate reading from a file
##--------------------------------------------------------------------------------------------------------------------
new_file = open('text.txt', "w")
new_file.write("5\n")
new_file.write("5\n")

new_file.write("1 1 1 1 1\n")
new_file.write("1 0 1 0 1\n")
new_file.write("1 1 1 0 1\n")
new_file.write("0 0 1 0 1\n")
new_file.write("0 0 1 1 1\n")
new_file.close()
##--------------------------------------------------------------------------------------------------------------------


f = open('text.txt', 'r')
n = int(f.readline())
m = int(f.readline())
h = []
for i in range(0,n):
    h.append(convert_int(f.readline().split(" ")))

m1 = -1
n1 = -1

##My code
##--------------------------------------------------------------------------------------------------------------------
sin = -1
sim = -1
sinterceptn = -1
sinterceptm = -1

for currentn in range(0, n):
	for currentm in range(0, m):
		i = h[currentn][currentm]
		
		if i == 1:
			#list along m axis, checking n until broken i.e. =0
			FROMcurrentnTOn = []
			for tn in range(currentn, n):
				pn = h[tn][currentm]
				if pn == 1:
					FROMcurrentnTOn.append(tn)
				else:
					break
			
			#list along n axis, checking m until broken i.e. =0
			FROMcurrentmTOm = []
			for tm in range(currentm, m):
				pm = h[currentn][tm]
				if pm == 1:
					FROMcurrentmTOm.append(tm)
				else:
					break
			
			#finding intercept using the combo of lists above
			for interceptn in FROMcurrentnTOn:
				for interceptm in FROMcurrentmTOm:
					ti = h[interceptn][interceptm]
					
					if ti == 1 & ((currentm != interceptm) & (currentn != interceptn)):
						
						#making sure from the current n to the intercept n is complete i.e. all 1
						bn = True
						for tn2 in range(currentn, interceptn+1):
							pn2 = h[tn2][currentm]
							if pn2 == 0:
								bn = False
								break
						
						#making sure from the current m to the intercept m is complete i.e. all 1
						bm = True
						for tm2 in range(currentm, interceptm+1):
							pm2 = h[tm2][currentm]
							if pm2 == 0:
								bm = False
								break
						
						#only test area if the rect was complete
						if bn == True and bm == True:
							tarea = 0
							tarea = (interceptn - currentn) * (interceptm - currentm)
							
							storedarea = (sinterceptn - sin) * (sinterceptm - sim)
							
							#print("+++", tarea, storedarea)
							
							if tarea > storedarea:
								sin = currentn
								sim = currentm
								sinterceptn = interceptn
								sinterceptm = interceptm

m1 = sin
n1 = sim
###-------------------------------------------------------------------------------------------------------------------

print(str(m1)+','+str(n1))
