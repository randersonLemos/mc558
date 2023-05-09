import copy
import math
import pprint

def KRUSDAL:
    pass


if __name__ == '__main__':
    import argparse; parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    file = args.file
    n, m, k =  map( int, file.readline().strip().split(' ') ) # N -> computadores. M -> conexões, K -> Clusters
    
    W = {}
    Adjs = {}
    for i in range(n):
        Adjs[i] = []

    for i in range(m):
        x, y, w = map( int, file.readline().strip().split(' ') )
        Adjs[x].append( y )
        W[ (x,y) ] = w

    import IPython; IPython.embed()
    
    #ini, end, cor, pai = DFS(Adjs, s, t)

    #TopSorLst = TopologicalSort(end)
   
    #q = CountPaths(Adjs, TopSorLst, s, t)

    #print( sum(q[t].values()) )
