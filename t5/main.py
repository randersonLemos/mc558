import cProfile
import copy
import math
import pprint


def INITIALIZESINGLESOURCE( Adjs, s ):
    D = [math.inf] * len(Adjs)
    P = [None] * len(Adjs)
    D[s] = 100
    return D, P


def RELAX(u, v, D, P, W):
    if ( D[v] > D[u] + W[(u,v)] ) and ( D[u] + W[(u,v)] ) > 0 :  
        D[v] = D[u] + W[(u,v)]
        P[v] = u


def BELLMANNFORD(Adjs, W, s):
    D, P = INITIALIZESINGLESOURCE( Adjs, s )

    for i in range( len(Adjs) - 1 ):
        for (u,v) in W:
            RELAX( u, v, D, P , W)

    for (u,v) in W:
        if D[v] > D[u] + W[ (u,v) ]:
            return False, D, P
    return True, D, P

 
if __name__ == '__main__':
    import argparse; parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    file = args.file
    
    n = int( file.readline().strip() )
    E = list( map( int, file.readline().strip().split(' ') ) ) # Energy

    m = int( file.readline().strip() )
    Adjs = {}
    W    = {}
    for i in range(n):
        Adjs[i] = []

    for i in range(m):
        u, v = map( int, file.readline().strip().split(' ') )
        W[ (u,v)  ] = E[v]
        Adjs[u].append(v)

    ret, D, P = BELLMANNFORD( Adjs, W, 0 )
    
    if D[-1] != math.inf:
        print('possible')
    else:
        print('impossible')
