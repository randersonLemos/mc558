import copy
import math
import pprint


def DFS(Adjs, s, t):
    global tempo
    V = Adjs.keys()
    ini = {}; end = {}; cor = {}; pai = {}
    for v in V:
        ini[v] = math.inf; end[v] = math.inf; cor[v] = 'BRANCO'; pai[v] = None
    tempo = 0
    DFSVisit(Adjs, s, t, ini, end, cor, pai)
    return ini, end, cor, pai


def DFSVisit(Adjs, s, t, ini, end, cor, pai):
    global tempo
    tempo = tempo + 1
    ini[s] = tempo
    cor[s] = 'CINZA'
    for u, c in Adjs[s]:
        if ( cor[u] == 'BRANCO' ):
            pai[u] = s
            DFSVisit(Adjs, u, t, ini, end, cor, pai)
    tempo = tempo + 1
    end[s] = tempo
    cor[s] = 'PRETO'


def TopologicalSort( end ):
    ts = sorted( end, key=lambda x : end[x], reverse=True )
    return ts
     

def CountPaths(Adjs, TopSorLst, s, t):
    V = Adjs.keys()
    q = {}
    for v in V:
        q[v] = {0:0, 1:0, 2:0}
    q[s][0] = 1

    for u in TopSorLst:
        for v, c in Adjs[u]:
            if c == 0:
                q[v][0] = q[v][0] + q[u][0] + q[u][1] + q[u][2]
            if c == 1:
                q[v][1] = q[v][1] + q[u][0] + q[u][1]
            if c == 2:
                q[v][2] = q[v][2] + q[u][0]
    return q



if __name__ == '__main__':
    import argparse; parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    file = args.file
    n, m, s, t =  map( int, file.readline().strip().split(' ') )

    Adjs = {}
    for i in range(n):
        Adjs[i] = []

    for i in range(m):
        x, y, c = map( int, file.readline().strip().split(' ') )
        Adjs[x].append( (y, c) )
    
    ini, end, cor, pai = DFS(Adjs, s, t)

    TopSorLst = TopologicalSort(end)
   
    q = CountPaths(Adjs, TopSorLst, s, t)

    print( sum(q[t].values()) )
