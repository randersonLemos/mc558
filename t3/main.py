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
    new_allowed_edges = [0, 1, 2] # VERDE, AMARELO, VERMELHO
    DFSVisit(Adjs, s, t, ini, end, cor, pai, new_allowed_edges)
    return ini, end, cor, pai


def DFSVisit(Adjs, s, t, ini, end, cor, pai, allowed_edges):
    global tempo
    tempo = tempo + 1
    ini[s] = tempo
    cor[s] = 'CINZA'
    for u, c in Adjs[s]:
        if ( cor[u] == 'BRANCO' ) and ( c in allowed_edges ):
            if c == 0:
                new_allowed_edges = [0, 1, 2]
            elif c == 1:
                new_allowed_edges = [0, 1]
            elif c == 2:
                new_allowed_edges = [0]
            else:
                raise Exception('Number out of the range!')
            pai[u] = s
            DFSVisit(Adjs, u, t, ini, end, cor, pai, new_allowed_edges)
    tempo = tempo + 1
    end[s] = tempo
    cor[s] = 'PRETO'


def TopologicalSort( end ):
    return sorted( end, key=lambda x : end[x], reverse=True )
     

def CountPaths(Adjs, topsor, s, t):
    import IPython; IPython.embed()


        


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

    topsor = TopologicalSort(end)

    

    #trail, color = computeEulerianTrail( adjs )
    #
    #stg = 'Não possui trilha Euleriana alternante'
    #if trail: 
    #    stg  = ' '.join(map( str, trail) )
    #    #stg += '\n'
    #    #stg += ' '.join(map( str, color) )

    #print( stg )


