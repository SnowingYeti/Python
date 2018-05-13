import sys

def moon_weight ():
    print ('What is your weight?')
    weight = int (sys.stdin.readline())
    print ('What is moon koef?')
    koef = float (sys.stdin.readline())
    print ('How many years?')
    years = int (sys.stdin.readline())

    for y in range (years):
        moon_weight = weight + koef
        print ('In %s year your weight is %s' % (y, moon_weight))
        weight = moon_weight
        
moon_weight()
