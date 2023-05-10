import copy
import math
import pprint


class Sets():
    def __init__(self):
        self.dict = {}
        self.weight= {}


    def make_set(self, elem):
        self.dict[elem] = set([elem])
        self.weight[elem] = 0


    def find_set(self, elem):
        for key in self.dict:
            _set = self.dict[key]
            if elem in _set:
                return key
        return None


    def union(self, u ,v, w ):
        uset = self.dict[u]
        vset = self.dict[v]

        uwei = self.weight[u]
        vwei = self.weight[v]

        uset = uset.union( vset )
        self.dict[u] = uset
        del self.dict[v]

        uwei = uwei + vwei
        self.weight[u] = uwei + w
        del self.weight[v]


    def __len__(self):
        return len(self.dict)


    def __repr__(self):
        return self.dict.__repr__()


def KRUSKAL( Adjs, W, k ):
    sets = Sets()
    A = set()

    for v in Adjs:
        sets.make_set(v)

    sW = sorted( W, key=W.get)

    for (u,v) in sW:        
        #print( sets, len(sets) )
        #print( sets.weight, len(sets.weight) )
        w = W[ (u, v) ]
        useed = sets.find_set( u ) 
        vseed = sets.find_set( v )
        if useed != vseed:
            sets.union( useed, vseed, w )
        #print( sets, len(sets) )
        #print( sets.weight, len(sets.weight) )
        #print('---')
        if len( sets ) == k:
            return sets


if __name__ == '__main__':
    #import argparse; parser = argparse.ArgumentParser()
    #parser.add_argument('--file', type=argparse.FileType('r'), required=True)
    #args = parser.parse_args()
    #file = args.file
    #n, m, k =  map( int, file.readline().strip().split(' ') ) # N -> computadores. M -> conexões, K -> Clusters

    n, m, k =  map( int, input().strip().split(' ') )
    
    W = {}
    Adjs = {}

    for i in range(n):
        Adjs[i] = []

    for i in range(m):
        x, y, w = map( int, input().strip().split(' ') )

        Adjs[x].append( y )
        W[ (x,y) ] = w

    sets = KRUSKAL( Adjs, W, k ) 

    print( sum( sets.weight.values() ) )
