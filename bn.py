import sys
from copy import *
from BayesianNetwork import *

def readInput(input):
    input_arr = input[1:]
    condition = []
    burglary = None
    earthquake = None
    alarm = None
    johnCalls = None
    maryCalls = None

    for i in input:
        if i[0] == 'B' and i[1] == 't':
            burglary = True
        elif i[0] == 'B' and i[1] == 'f':
            burglary = False

        if i[0] == 'E' and i[1] == 't':
            earthquake = True
        elif i[0] == 'E' and i[1] == 'f':
            earthquake = False

        if i[0] == 'A' and i[1] == 't':
            alarm = True
        elif i[0] == 'A' and i[1] == 'f':
            alarm = False

        if i[0] == 'J' and i[1] == 't':
            johnCalls = True
        elif i[0] == 'J' and i[1] == 'f':
            johnCalls = False

        if i[0] == 'M' and i[1] == 't':
            maryCalls = True
        elif i[0] == 'M' and i[1] == 'f':
            maryCalls = False

    givenConditionIndex = 0
    if input_arr.count('given'):
        givenConditionIndex = input_arr.index('given')
        for j in range(givenConditionIndex+1,len(input_arr)):
            condition.append(input_arr[j][0])

    return ([burglary,earthquake,alarm,johnCalls,maryCalls],condition)

def createRow(ttable,input_condition):
    if input_condition.count(None) != 0:
        noneIndex = input_condition.index(None)
        t = deepcopy(input_condition)
        t[noneIndex] = True
        f = deepcopy(input_condition)
        f[noneIndex] = False
        createRow(ttable,t)
        createRow(ttable,f)
        return ttable
    else:
        ttable.append(input_condition)
        return ttable

def main(argv):

    first_condition,second_condition = readInput(argv)
    bn = BayesianNetwork()
    truth_table = createRow([],first_condition)
    final_probability = 0.00

    for row in truth_table:
        final_probability += bn.calculateProbability(row[0],row[1],row[2],row[3],row[4],second_condition)

    print 'Probability of given condition ('+str(argv[1:])+') is ::'+str('%.5f'%final_probability)

if __name__ == '__main__':
    main(sys.argv)