import random
def func():
    try:
        x = int(raw_input('Please enter an integer less than 20: '))
    if x > 20:

    l = random.sample(range(1,21),x)
    print l
    deets = []
    while len(l)>0:
        y = int(raw_input('Select a postion: '))-1
        while y + 1> len(l):
            y = int(raw_input('Out of range. Pick a number {} or smaller: '.format(len(l))))
            y = y-1
        deets.append(l[y])
        del l[y]
        print l
        print deets
func()
