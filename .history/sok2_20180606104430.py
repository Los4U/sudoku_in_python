row1 = [0,0,0,0,0,0,0,0,0]
row2 = [0,0,0,5,0,6,0,0,0] 
row3 = [0,0,1,0,0,0,0,3,0] 

row4 = [0,9,5,0,0,0,2,0,0] 
row5 = [0,0,0,0,0,1,6,0,7] 
row6 = [1,0,6,0,0,9,0,0,5] 

row7 = [7,0,0,8,0,3,9,0,0] 
row8 = [0,3,8,9,0,0,0,2,0] 
row9 = [0,5,0,0,2,0,7,0,0] 

print(row1)
print(row2)
print(row3)
print("")
print(row4)
print(row5)
print(row6)
print("")
print(row7)
print(row8)
print(row9)

while True:
    x = input("Wprowadz x y z:") 
    try:
        if int(x[0])==1:
            row1[int(x[2])-1]=x[4]
            print("ok")
    except ValueError: # przechwytuje wyjątek literę i kończy program.
            print("Wprowadz cyfrę!")
            continue

    print(row1[0],row1[1],row1[2], sep='  ', end="  -  ")
    print(row1[3],row1[4],row1[5], sep='  ', end="  -  ")
    print(row1[6],row1[7],row1[8], sep='  ')

    print(row1[0],row1[1],row1[2], sep='  ', end="  -  ")
    print(row1[3],row1[4],row1[5], sep='  ', end="  -  ")
    print(row1[6],row1[7],row1[8], sep='  ')

    #print(str(*r11, sep='')  + "-" + str(r12) + " - " +  str(r13))
    print(row2)
    print(row3)
    print(""),
    
    print(row4)
    print(row5)
    print(row6)
    print("")
    print(row7)
    print(row8)
    print(row9)

#print(new)
#rds.insert(index, "is")