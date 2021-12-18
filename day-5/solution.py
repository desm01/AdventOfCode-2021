solutionInput = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


#Replace whitespace and arrow. Create a list of lists where each inner list contains a set of two co-ordinates.
solutionInput = [element.replace(" ", "").split('->') for element in solutionInput.splitlines()] 

w, h = 1000, 1000
grid = [[0 for x in range(w)] for y in range(h)] 


for element in solutionInput:
    left = element[0].split(',')
    right = element[1].split(',')

    if left[0] == right[0]:
        pointer = int(min(left[1], right[1]))
        end = int(max(left[1], right[1]))

        while(pointer <= end):
        
            grid[int(left[0])][pointer] = grid[int(left[0])][pointer] + 1
            
            pointer = pointer + 1


    if left[1] == right[1]:
        pointer = int(min(left[0], right[0]))
        end = int(max(left[0], right[0]))

        while(pointer <= end):
            grid[pointer][int(left[1])] = grid[pointer][int(left[1])] + 1
            
            pointer = pointer + 1

count = 0
for row in grid:
    for a in row:
        if a > 1:
            count = count + 1

print(count)
