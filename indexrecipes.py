def printthings():
    f = open("categorized.lst", 'r')
    g = open("indexedingredients.lst", 'w')
    for i, line in enumerate(f):
        #line = line.strip().split()
        g.write(str(i)+" "+line)


def main():
    printthings()

if __name__=="__main__":
    main()
