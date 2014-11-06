import random
from math import sqrt


def make_data_list():
    alldata = open("formattedforclusters.txt",'r')
    rows = []
    alldata.next()
    for entry in alldata:
        rows.append(entry.split()[1:])
    return rows

def init_clusters(rows,k=4):
    #"""creates a list of lists that contain random numbers from 0 to 1 for each possible food item"""

    clusters = []
    #print len(rows[0])
    for j in range(k):
        temp_cluster = []
        for i in range(len(rows[0])):
            temp_cluster.append(random.random())
        clusters.append(temp_cluster)
    return clusters

def assign_centroids(rows, clusters,k=4):
    lastmatches = None
    for t in range(100):
        print "Iteration %d " % t
        bestmatches = [[] for i in range(k)]

        for j, row in enumerate(rows):
            bestmatch = 0
            for i in range(k):
                dist = pearson_distance(clusters[i], row)
                if dist < pearson_distance(clusters[bestmatch],row):
                    bestmatch = i
                bestmatches[bestmatch].append(j)
        if bestmatches == lastmatches:
            break
        lastmatches = bestmatches

        for i in range(k):
            avgs = [0.0]*(len(row))
            if len(bestmatches[i])>0:
                for rowid in bestmatches[i]:
                    for m in range(len(rows[rowid])):
                        avgs[m]+=rows[rowid][m]
                for j in range(len(avgs)):
                    avgs[j]/=len(bestmatches[i])
                clusters[i] = avgs
    return bestmatches

def pearson_distance(v1,v2):
    # Takes in a list of pairwise ratings and produces a pearson similarity
#something about pairs versus pair.
    for i in range(len(v2)):
        v2[i] = float(v2[i])
    for i in range(len(v1)):
        v1[i] = float(v1[i])

    sum1 = sum(v1)
    sum2 = sum(v2)
    
    sum1Sq = sum([pow(v,2) for v in v1])
    sum2Sq = sum([pow(v,2) for v in v2])

    pSum = sum([v1[i]*v2[i] for i in range(len(v1))])
    num = pSum-(sum1*sum2/len(v1))
    den = sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
    if den == 0:
        return 0
    return 1-(num/den)

def main():
    list_of_occurrences  = make_data_list()
    list_of_initial_clusters = init_clusters(list_of_occurrences)
    best_matches = assign_centroids(list_of_occurrences, list_of_initial_clusters)
if __name__ == "__main__":
    main()
