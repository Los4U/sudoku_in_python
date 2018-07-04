from random import randint

sudoku1 = [
    [5, 9, 8, 6, 1, 2, 3, 4, 7],
    [2, 1, 7, 9, 3, 4, 8, 6, 5],
    [6, 4, 3, 5, 8, 7, 1, 2, 9],
    [1, 6, 5, 4, 9, 8, 2, 7, 3],
    [3, 2, 9, 7, 6, 5, 4, 1, 8],
    [7, 8, 4, 3, 2, 1, 5, 9, 6],
    [8, 3, 1, 2, 7, 6, 9, 5, 4],
    [4, 7, 2, 8, 5, 9, 6, 3, 1],
    [9, 5, 6, 1, 4, 3, 7, 8, " "]
    ]

sudoku2 = [
    [9, 8, 7, 4, 3, 2, 5, 6, 1],
    [2, 4, 3, 5, 1, 6, 8, 7, 9],
    [5, 6, 1, 7, 9, 8, 4, 3, 2],
    [3, 9, 5, 6, 4, 7, 2, 1, 8],
    [8, 2, 4, 3, 5, 1, 6, 9, 7],
    [1, 7, 6, 2, 8, 9, 3, 4, 5],
    [7, 1, 2, 8, 6, 3, 9, 5, 4],
    [4, 3, 8, 9, 7, 5, 1, 2, 6],
    [' ', 5, ' ', ' ', 2, ' ', 7, ' ', ' ']
    ]

def printSudoku():
    i = 0
    while i < 10:
        if i == 0:
            print("    1 2 3   4 5 6   7 8 9")
            print("  -------------------------")    
        elif i == 3 or i == 6 or i == 9:
            print("  -------------------------")  
        spaceBar = "|"
        if i < 9:
            print('{2} {1} {0[0]} {0[1]} {0[2]} {1} {0[3]} {0[4]} {0[5]} {1} {0[6]} {0[7]} {0[8]} {1}'.format(sudoku1[i], spaceBar,i+1))
        i = i + 1



while True:  # prints Sudoku until is solved
    print("Your sudoku to solve:")
    printSudoku()
    print("Input 3 numbers in format a b c, np. 4 5 8")
    print(" a - row number")
    print(" b - column number ")
    print(" c - value")
    # vprint(" r - reset chart to start\n ")
    x = input("Input a b c: ")
    print("")

    numbers = " 0123456789"  # conditions of entering the numbers !
    if (len(x) != 5) or (str(x[0]) not in numbers) or (str(x[2]) not in numbers) or (
            str(x[4]) not in numbers) or (str(x[1]) != " ") or (str(x[3]) != " "):
        if x == "r":  # reset
            print(" Function reset() will be ready in Next Week")
        else:
            print("Error - wrong number format \n ")
            continue

    sudoku1[int(x[0])-1][int(x[2])-1] = int(x[4])

    column1 = 0
    column2 = 0

    try:
        i = 0
        list = []
        while i < 9:
            column = 0
            for item in sudoku1:
                column = column + item[i]
            list.append(column)
            #p rint(list)
            # print("Suma columny ", i, " = ", column)    
            i += 1

        is45 = 0    
        for listElement in list:
            if listElement == 45:
                is45 = is45 + 1    

        # print("Ile kolumen OK", is45)
        i = 0
        for item in sudoku1:
            if sum(item) == 45 and is45 == 9:
                i = i + 1
        if i == 9:
            printSudoku()
            print("@@@@@@@@@@ YOU WIN @@@@@@@@@@")
            break

    except TypeError:
        print()