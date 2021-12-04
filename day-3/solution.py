
solutionInput = solutionInput.replace(' ','')
solutionInput = solutionInput.split(',')


def recurse(i, occurencesOfZero, occurencesOfOne, binaryNumber):
    if occurencesOfZero + occurencesOfOne == len(solutionInput):
        if occurencesOfOne > occurencesOfZero:
            binaryNumber = binaryNumber + "1"
            occurencesOfOne = 0
            occurencesOfZero = 0
        else:
            binaryNumber = binaryNumber + "0"
            occurencesOfZero = 0
            occurencesOfOne = 0

    if i == len(solutionInput[0]):
        return binaryNumber

    for item in solutionInput:
        if item[i] == '1':
            occurencesOfOne = occurencesOfOne + 1
        else:
            occurencesOfZero = occurencesOfZero + 1

    return recurse(i + 1, occurencesOfOne ,occurencesOfZero ,binaryNumber)


print(recurse(0,0,0,""))
print(1503 * 2592)



