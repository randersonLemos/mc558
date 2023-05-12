import copy
import math
import pprint


class SetWeighted:
    def __init__(self, elems, w):
        self.set = set( elems )
        self.weight = w


    def union(self, other, weight):
        self.set = self.set.union( other.set )
        self.weight = self.weight + other.weight + weight
        return self


    def __iter__(self):
        return self.set.__iter__()


    def __next__(self):
        return self.set.__next__()


    def __repr__(self):
        return '{} - {}'.format( self.weight, self.set )


class Sets():
    def __init__(self):
        self.dict = {}
        self.total_weight = 0


    def make_set(self, elem):
        self.dict[elem] = SetWeighted( [elem], 0 )


    def find_set(self, elem):
        return self.dict[ elem ]


    def union(self, u ,v, w ):
        uset = self.dict[u]
        vset = self.dict[v]

        uset = uset.union( vset, w )

        self.total_weight = self.total_weight + w

        for elem in vset:
            self.dict[elem] = uset


    def __len__(self):
        return len(self.dict)


    def __repr__(self):
        return self.dict.__repr__()


def KRUSKAL( Adjs, W, k ):
    sets = Sets()
    A = set()

    K = 0
    for v in Adjs:
        sets.make_set(v)
        K = K + 1

    sW = sorted( W, key=W.get)

    for (u,v) in sW:        
        w = W[ (u, v) ]
        uset = sets.find_set( u ) 
        vset = sets.find_set( v )
        if uset!= vset:
            sets.union( u, v, w )
            K = K - 1
        if K == k:
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

    print( sets.total_weight )
