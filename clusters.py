import random
from math import sqrt

def readfile(filename):
    file_name = open(filename,'r')
    lines = []
    for line in file_name:
        lines.append(line)

    colnames = lines[0].strip().split()[1:]

    rownames = []
    data = []

    #for line in lines[1:]:
    for i in range(len(lines)-1):
#        print "here1"
        print line[1:]
        line = lines[1:][i]

        p=line.strip().split()
#        print "here2"
        rownames.append(p[0])
#        print "here3"
        data.append([float(x) for x in p[1:]])
#        print "here4"

def pearson(v1,v2):
    sum1 = sum(v1)
    sum2 = sum(v2)

    sum1Sq = sum([pow(v,2) for v in v1])
    sum2Sq = sum([pow(v,2) for v in v2])

    pSum = sum([v1[i]*v2[i] for i in range(len(v1))])

    num = pSum-(sum1*sum2/len(v1))
    den = sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
    if den == 0:
        return 0
    return 1.0 - float(num)/float(den)


def kcluster(rows,distance=pearson,k=4):
    ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows]))
           for i in range(len(rows))]

    clusters = [[random.random()*(rangers[i][1]-ranges[i][0])+ranges[i][0] for i in range(len(rows[0]))] for j in range(k)]

    lastmatches = None
    for t in range(100):
        print 'Iteration %d' % t
        bestmatches = [[] for j in range(k)]
        
        for j in range(len(rows)):
            rows = rows[j]
            bestmatch = 0
            for i in range(k):
                d = distance(clusters[i], row)
                if d < distance(clusters[bestmatch], row):
                    bestmatch = i
            bestmatches[bestmatch].append(j)

        if bestmatches == lastmatches: break
    lastmatches = bestmatches



