from test_board import print_board

def solve(puzzle):

    solution = []
    print("old puzzle:")
    print_board(puzzle)

    for i in puzzle:
        solution.append(i)

    for x in solution:
        for i,y in enumerate(x):
            #print(str(i) + "," + str(y))
            if y == 0:
                x[i] = "*"

    keep_going = True
    count = 0
    num_sols = 1
    while(keep_going):
        count += 1
        print("count = " + str(count))
        keep_going = False #set to false initially
        for j,x in enumerate(solution): #x is each list contained in solution, x indicates row
            for i,y in enumerate(x):    #y is each element in x, y indicates column
                #main loop to check each val
                #only do anything if val is = "*"
                if x[i] == '*':
                    possible_nums = [1,2,3,4,5,6,7,8,9]
                    #check col
                    for col in range(len(solution)):
                        if solution[j][col] in possible_nums:
                            possible_nums.remove(solution[j][col])
                    #check row
                    for row in range(len(solution)):
                        if solution[row][i] in possible_nums:
                            possible_nums.remove(solution[row][i])
                    #check cell
                    for row in range ((j//3) * 3, (j//3) * 3 + 3):
                        for col in range ((i//3) * 3, (i//3) * 3 +3):
                            if solution[row][col] in possible_nums:
                                possible_nums.remove(solution[row][col])

                    print("* at" + str(j) + "," + str(i) + "can be these nums:" + str(possible_nums))
                    #if only one possibility, just change it!
                    if (len(possible_nums) == 1):
                        keep_going = True #found something to fix, keep going true
                        solution[j][i] = possible_nums[0]
                    if (len(possible_nums) == 0):
                        print("Error! Error! this should never happen!")









    print("solution done, here is what has been solved:")

    print("solution:")
    print_board(solution)
    return solution


def cell_indexes(x,y):
    return False