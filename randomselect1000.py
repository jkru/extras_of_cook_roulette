import random

def pickrandomnumbers():
    randomnumbers = {}
    while len(randomnumbers) < 1000:
        this_rand = random.randint(0,57691) 
        randomnumbers[this_rand] = randomnumbers.get(this_rand,0) + 1
    
    list_of_numbers = sorted(randomnumbers.keys())
    
    return [list_of_numbers, randomnumbers]

def makerandomlist(randomdict):
    f = open('unindexedrecipes.txt','r')
    g = open('trunc_100_unindexedrecipes.txt','w')
    check_same = {}
    for i, line in enumerate(f):
        if i in randomdict:
            check_same[line] = check_same.get(line,0)+1
            if check_same[line] < 2:
                g.write(line)
    g.close()
    f.close()
        


def main():
    randomlist, randomdict = pickrandomnumbers()
    makerandomlist(randomdict)

if __name__ == "__main__":
    main()

